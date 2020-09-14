#!/bin/sh
cd /usr/src/app
gunicorn -c file:app/config.py "app:create_app()"
