from jinja2 import Environment
from jinja2 import FileSystemLoader
from pyramid import i18n
from pyramid.threadlocal import get_current_request

class jinja2_renderer_factory(object):
    def csrf_token(self):
        return get_current_request().session.get_csrf_token()

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
        kw['csrf_token'] = self.csrf_token()

        return template.render(**kw)

class GetTextWrapper(object):

    def __init__(self, domain="deform"):
        self.domain = domain

    @property
    def localizer(self):
        return i18n.get_localizer(get_current_request())

    def gettext(self, message):
        return self.localizer.translate(message,
                                        domain=self.domain)

    def ngettext(self, singular, plural, n):
        return self.localizer.pluralize(singular, plural, n,
                                        domain=self.domain)
