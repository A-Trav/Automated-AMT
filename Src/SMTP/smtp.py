"""
The smtp module: SMTP Admin alert.

Provides globals and functionality to support the applications admin alert
email needs.
"""

from flask_mail import Mail, Message
from traceback import format_exc
from Service.admin import get_admin_email
from Utils.app_logging import log

mail = Mail()
"""The SMTP mail server global"""

@log
def alert_admin_failure():
    """
    Emails the applications admin user with a callstack showing the latest exception that was encountered.
    """
    msg = Message("Automated AMT - Manual resolution required",
                recipients=[get_admin_email()])
    assert msg.sender == '***REMOVED***'
    msg.body = format_exc()
    mail.send(msg)