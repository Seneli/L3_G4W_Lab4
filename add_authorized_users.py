from backend import Backend
from mydbconfig import *
backend = Backend(config, email, firstname, lastname)

backend.add_authorized_users('alexandrejanellegood@cmail.carleton.ca')
backend.add_authorized_users('my_group_mate2_email@cmail.carleton.ca')