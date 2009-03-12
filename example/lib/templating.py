"""
Templating support library and renderer configuration.
"""

from restish import templating

class Templating(templating.Templating):
    """
    Application-specific templating implementation.

    Overriding "args" methods makes it trivial to push extra, application-wide
    data to the templates without any assistance from the resource.
    """

    def __init__(self, app_conf):
        renderer = make_renderer(app_conf)
        templating.Templating.__init__(self, renderer)


def make_renderer(app_conf):
    """
    Create and return a restish.templating "renderer".
    """

    # Uncomment for an example of Mako templating support.
    import pkg_resources
    import os.path
    from restish.contrib.makorenderer import MakoRenderer
    return MakoRenderer(
            directories=[
                pkg_resources.resource_filename('example', 'templates'),
                pkg_resources.resource_filename('formish', 'templates/mako'),
                pkg_resources.resource_filename('adminish', 'templates'),
                ],
            module_directory=os.path.join(app_conf['cache_dir'], 'templates'),
            input_encoding='utf-8', output_encoding='utf-8',
            default_filters=['unicode', 'h']
            )


