import mongoengine
def global_init():
    mongoengine.register_connection(alias='core', db='Rescue_Heroes')
