#guincorn config

# django WSGI app path in pattern MODULE_NAME:VARIABLE_NAME

wsgi_app = "project.wsgi:application"

# granularity of error log outputs

loglevel = "debug"

# the number of worker processes for handling requests

workers = 2

# socket to bind

bind = "0.0.0.0:8000"

# restart workers when code changes (dev only)

reload = True

# write acess and error log to file

accesslog = errorlog = "/var/log/gunicorn/dev.log"

# Redirect stdout/stderr to log file

capture_output = True

# PID file so you can easily fetch process ID

pidfile = "/var/run/gunicorn/dev.pid"

# Daemonize the Gunicorn process (detach and enter background)

daemon = True
