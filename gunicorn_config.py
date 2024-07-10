# gunicorn_config.py


#Heroku
import os

workers = 3  # adjust based on your dyno type
worker_class = 'gthread'  # or 'sync' for simple configurations
threads = 2  # number of threads per worker, adjust as needed

#Local:

#bind = '127.0.0.1:8000'
#workers = 3
#worker_class = 'uvicorn.workers.UvicornWorker'
