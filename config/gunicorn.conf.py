import multiprocessing
from pj_utils import env


bind = "0.0.0.0:8000"

wsgi_app = "config.wsgi:application"

DEFAULT_WORKERS = multiprocessing.cpu_count() * 2 + 1
DEFAULT_THREADS = multiprocessing.cpu_count() * 2 + 1

workers = env.int('GUNICORN_WORKERS', DEFAULT_WORKERS)
threads = env.int('GUNICORN_THREADS', DEFAULT_THREADS)

loglevel = env.str('GUNICORN_LOGLEVEL', 'info')
reload = env.bool('GUNICORN_RELOAD', False)
capture_output = env.bool('GUNICORN_CAPTURE_OUTPUT', False)

# accesslog = errorlog = "/var/log/gunicorn/dev.log"

# pidfile = "/var/run/gunicorn/dev.pid"
# daemon = True
