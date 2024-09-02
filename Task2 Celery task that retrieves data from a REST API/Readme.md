
### 3. Steps to Run the Project

1. **Create the Project Directory and Files**

   - Navigate to your desired directory and create the main project folder:
   
     ```bash
     mkdir youtube_data_project
     cd youtube_data_project
     ```

   - Create all the necessary files:

     ```bash
     touch celery_config.py tasks.py app.py requirements.txt README.md
     mkdir database logs
     ```

2. **Install Dependencies**

   - Run the following command to install the required libraries:

     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Redis Broker**

   - Make sure Redis is installed and running. Start Redis with:

     ```bash
     redis-server
     ```

4. **Run the Celery Worker**

   - Start the Celery worker:

     ```bash
     celery -A celery_config worker --loglevel=info --logfile=logs/celery_worker.log
     ```

5. **Trigger the Task**

   - Run the `app.py` script to initiate the task:

     ```bash
     python app.py
     ```

### Additional Configuration

- **Logging**: Logs are saved in `logs/celery_worker.log` for monitoring. You can customize the logging behavior by modifying the Celery worker command.
- **Database Configuration**: Adjust the `DATABASE_URI` in `tasks.py` if you prefer a different database (e.g., PostgreSQL, MySQL).

By following these instructions, you will have a fully functional project that integrates Celery with the YouTube API, performs tasks asynchronously, and stores the data in a local SQLite database. If you need any further customization or clarification, let me know!
