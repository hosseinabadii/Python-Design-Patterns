import os
os.system("clear")

from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_event_handlers
from api.email_listener import setup_email_event_handlers

from api.user import register_new_user, password_forgotten, reset_password
from api.plan import upgrade_plan

# initialize the event structure
setup_slack_event_handlers()
setup_log_event_handlers()
setup_email_event_handlers()


# register a new user
register_new_user("Khosro", "BestPassword", "name@name.com")

# send a password reset message
password_forgotten("name@name.com")

# upgrade the plan
upgrade_plan("name@name.com")
