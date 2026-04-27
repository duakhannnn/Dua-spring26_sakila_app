# Name: Abdul Raffay Qasim
# Name: Team Member
# Date: 2026-04-23
# Minor improvement after PR review
# Added after review feedback
import os

class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """

   # Dua Shakeel - 25 april 

MYSQL_HOST = 'sakila-db-server'

CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

# Dua Shakeel - 25 -april

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
#Author:Urwah Taj
#Date: 2026-04-23
# Purpose: Database configuration for Sakila Flask Application

# Author: Team Member = Aliyah Cheema
# Date: 2026-04-23
# Purpose: Health check configuration merged from feature/add-healthcheck


import os

MYSQL_HOST = 'sakila-db-server'
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

try:
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
except ValueError:
    CONNECTION_TIMEOUT = 30

try:
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
except ValueError:
    HEALTH_CHECK_INTERVAL = 10

# minor improvement after PR review - Dua 