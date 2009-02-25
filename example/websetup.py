from adminish import config

def setup_app(command, conf, vars):
    config.make_couchish_store(conf, 'example.model').sync_views()


