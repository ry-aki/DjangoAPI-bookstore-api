#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)
"""connection = MySQLdb.connect(
    host     = 'us-east.connect.psdb.cloud',
    user     = 'ubasc9rjvwdyq20mt87m',
    passwd   = 'pscale_pw_3Gj4SZ3oWO68GgN2EvOAUDfPPRTZ96Eoi8mCkUbb18t',
    db       = 'bookstore',
    #ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
        "ca": "/etc/ssl/certs/ca-certificates.crt"
    })
"""
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAPI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()