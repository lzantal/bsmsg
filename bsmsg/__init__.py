VERSION = '0.1.0'
# overwrite built in message tags to use bootstrap classes
from django.contrib.messages import constants as msg_const

MESSAGE_TAGS = {
    msg_const.DEBUG: 'alert-dark',
    msg_const.INFO: 'alert-info',
    msg_const.SUCCESS: 'alert-success',
    msg_const.WARNING: 'alert-warning',
    msg_const.ERROR: 'alert-danger',
}
