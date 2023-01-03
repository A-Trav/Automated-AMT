"""
The smtp module: SMTP Admin alert.

Provides globals and functionality to support the applications admin alert
email needs.
"""

from flask_mail import Mail, Message
from traceback import format_exc
from Service.admin import get_admin_email
from app_logging import log

mail = Mail()

@log
def alert_admin_failure():
    msg = Message("Automated AMT - Manual resolution required",
                recipients=[get_admin_email()])
    assert msg.sender == '***REMOVED***'
    msg.body = format_exc()
    mail.send(msg)