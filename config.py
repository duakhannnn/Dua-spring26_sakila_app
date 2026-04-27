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

    # Database configuration
    MYSQL_HOST = 'sakila-db-server'
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    # Timeout settings
    try:
        CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    except ValueError:
        CONNECTION_TIMEOUT = 30

    try:
        HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
    except ValueError:
        HEALTH_CHECK_INTERVAL = 10

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

    # Author: Urwah Taj
    # Date: 2026-04-23
    # Purpose: Database configuration for Sakila Flask Application

    # Author: Team Member = Aliyah Cheema
    # Date: 2026-04-23
    # Purpose: Health check configuration merged from feature/add-healthcheck

    # minor improvement after PR review - Dua