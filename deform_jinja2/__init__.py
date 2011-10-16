from jinja2 import Environment
from jinja2 import FileSystemLoader

class jinja2_renderer_factory(object):

    def __init__(self, directory, extensions=[], translator=None):
        self.directory = directory
        self.translator = translator
        self.extensions = extensions

        if 'jinja2.ext.i18n' not in self.extensions:
            self.extensions.append('jinja2.ext.i18n')


    def __call__(self, tname, **kw):
        jinja_env = Environment(extensions=self.extensions)
        jinja_env.loader = FileSystemLoader(self.directory)
        jinja_env.install_gettext_callables(self.translator.gettext, self.translator.ngettext)

        template = jinja_env.get_template(tname + '.jinja2')

        return template.render(**kw)
