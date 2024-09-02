from celery import shared_task
import requests
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.exc import SQLAlchemyError

# Configure SQLAlchemy engine and metadata
DATABASE_URI = 'sqlite:///youtube_data.db'  # Replace with your actual database URI
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# Define a table for storing YouTube data
youtube_data_table = Table(
    'youtube_data', metadata,
    Column('id', Integer, primary_key=True),
    Column('video_id', String, unique=True),
    Column('title', String),
    Column('description', String),
    Column('channel_title', String)
)

# Create the table if it doesn't exist
metadata.create_all(engine)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def fetch_youtube_data(self, api_key, query, max_results=10):
    """
    Celery task to fetch data from the YouTube API, process it, and store it in a database.
    """
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={max_results}&q={query}&key={api_key}'

    try:
        # Fetch data from YouTube API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse JSON data
        data = response.json()

        # Process each video item in the data
        for item in data.get('items', []):
            video_id = item['id'].get('videoId')
            snippet = item.get('snippet', {})
            title = snippet.get('title')
            description = snippet.get('description')
            channel_title = snippet.get('channelTitle')

            # Store data in the database
            with engine.connect() as connection:
                ins = youtube_data_table.insert().values(
                    video_id=video_id,
                    title=title,
                    description=description,
                    channel_title=channel_title
                )
                try:
                    connection.execute(ins)
                except SQLAlchemyError as e:
                    print(f"Error storing data in the database: {e}")
        
        print(f"Successfully fetched and stored data for query: {query}")

    except requests.exceptions.RequestException as exc:
        # Retry the task on request failure
        print(f"Error fetching data from YouTube API: {exc}")
        raise self.retry(exc=exc)
