"""
The app_args module: Command line args.

Provides functionality to determine what configuration the application has 
been run with via command line arguments.
"""

import sys

def check_debug_arg():
    """
    Checks the command line arguments that the Flask application was run with to determine if the 
    -debug argument was passed.

    :return: Boolean representation of whether the command line arg was found
    :rtype: Boolean
    """
    if (len(sys.argv) > 1) and ('-debug' in sys.argv):
        return True
    return False

def check_admin_arg():
    """
    Checks the command line arguments that the Flask application was run with to determine if the 
    -set-admin argument was passed.

    :return: Boolean representation of whether the command line arg was found
    :rtype: Boolean
    """
    if (len(sys.argv) > 1) and ('-set-admin' in sys.argv):
        return True
    return False
        