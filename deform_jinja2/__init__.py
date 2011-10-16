from jinja2 import Environment
from jinja2 import FileSystemLoader
from pyramid.threadlocal import get_current_request
from translationstring import TranslationStringFactory
from pyramid.i18n import get_localizer

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

class GetTextWrapper(object):

    def __init__(self, domain='deform'):
        self.domain = domain

    def translate(self, term):
        if not hasattr(term, 'interpolate'): # not a translation string
            term = TranslationStringFactory(self.domain)(term)
        return get_localizer(get_current_request()).translate(term)

    def pluralize(self, term):
        if not hasattr(term, 'interpolate'): # not a translation string
            term = TranslationStringFactory(self.domain)(term)
        return get_localizer(get_current_request()).pluralize(term)


    def gettext(self, message):
        return self.translate(message)

    def ngettext(self, singular, plural, n):
        return self.pluralize(singular, plural, n)
