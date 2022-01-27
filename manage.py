#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv


def main():
    """Run administrative tasks."""

    if os.environ.get('STATUS') == "Production": # In the production stage in Heroku, environment variables are taken from Heroku's environment
        pass                                     # No need to invoke the dotenv module
    else:
        dotenv.read_dotenv()    # This method is needed to read the environment variables from local .env file
                                # If I am testing my app locally, the os.environ.get('STATUS') will have the value of none before the if statement,
                                # which will allow the else body to execute and set the environment variables to be read by os module in settings.py

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
