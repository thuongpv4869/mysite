#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from pj_utils import env
import sys
import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

    from django.conf import settings

    if settings.DEBUG and env.bool('DJANGO_DEBUG_VSCODE', False):
        if env.bool('RUN_MAIN', False) or os.environ.get('WERKZEUG_RUN_MAIN'):
            import debugpy
            debugpy.listen(("0.0.0.0", 5678))
            print('Attached!')

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
