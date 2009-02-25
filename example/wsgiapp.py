"""
WSGI/PasteDeploy application bootstrap module.
"""
import pkg_resources
from restish.app import RestishApp

import repoze.who.config
from wsgiapptools import cookies, flash

import adminish
from example.resource import root


def make_app(global_conf, **app_conf):
    """
    PasteDeploy WSGI application factory.

    Called by PasteDeply (or a compatable WSGI application host) to create the
    example WSGI application.
    """
    app = RestishApp(root.Root())
    app = repoze.who.config.make_middleware_with_config(app, global_conf, app_conf['repoze.who.ini'])
    app = setup_environ(app, global_conf, app_conf)
    # General "middleware".
    app = flash.flash_middleware_factory(app)
    app = cookies.cookies_middleware_factory(app)
    return app


def setup_environ(app, global_conf, app_conf):
    """
    WSGI application wrapper factory for extending the WSGI environ with
    application-specific keys.
    """
    from example.lib.templating import Templating
    templating = Templating(app_conf)

    def application(environ, start_response):
        environ['restish.templating'] = templating
        environ['couchish'] = adminish.config.make_couchish_store(app_conf, 'example.model')
        environ['adminish'] = adminish.config.make_adminish_config(environ['couchish'].config.types)
        return app(environ, start_response)

    return application


