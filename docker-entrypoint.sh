#!/bin/bash
set -e

case $1 in
    supervisor)
        /usr/bin/supervisord -n -c supervisor-app.conf
    ;;
    celery)
        export QUEUE_NAME=$3
        /usr/bin/supervisord -n -c celery.conf
    ;;
esac

exec "$@"