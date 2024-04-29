from celery import Celery
from celery.utils.log import get_logger
from src.config import Config

logger = get_logger(__name__)
app = Celery('tasks')
app.config_from_object(Config)



if __name__ == '__main__':
  args = ['worker', '--loglevel=INFO']
  app.worker_main(argv=args)