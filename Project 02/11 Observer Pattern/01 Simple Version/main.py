import os
os.system("clear")

from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

# register a new user
register_new_user("Khosro", "BestPasswordEva", "name@name.com")

# send a password reset message
password_forgotten("name@name.com")

# upgrade the plan
upgrade_plan("name@name.com")
