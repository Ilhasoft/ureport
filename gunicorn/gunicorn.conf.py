import multiprocessing


bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
threads = workers
name = 'ureport'
env = 'DJANGO_SETTINGS_MODULE=ureport.settings'
proc_name = 'ureport'
default_proc_name = proc_name
loglevel = 'debug'
accesslog = 'gunicorn.access'
errorlog = 'gunicorn.error'
timeout = 120
chdir = '/ureport'
capture_output = True
