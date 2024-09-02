from tasks import fetch_youtube_data

# Replace with your YouTube API key and query
api_key = 'AIzaSyBbqXDFb7RrNLnNqxHsrqxLsrjC3uHmTGM'
query = 'Python programming'

# Call the Celery task
fetch_youtube_data.delay(api_key, query)
