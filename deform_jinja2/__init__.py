from jinja2 import Environment
from jinja2 import FileSystemLoader
from pkg_resources import resource_filename

class DummyTranslator(object):
    @staticmethod
    def gettext(message):
        return message

    @staticmethod
    def ngettext(singular, plural, n):
        if n > 1:
            return plural

        return singular

class jinja2_renderer_factory(object):
    def __init__(self, search_paths=(), default_templates='deform_jinja2:templates',
            translator=None, extensions=[]):

        if 'jinja2.ext.i18n' not in extensions:
           extensions.append('jinja2.ext.i18n')

        self.env = Environment(extensions=extensions)
        self.env.loader = FileSystemLoader(())

        for path in search_paths:
            self.add_search_path(path)

        if translator == None:
            translator = DummyTranslator

        self.env.install_gettext_callables(translator.gettext, translator.ngettext)

        self.add_search_path(default_templates)

    def add_search_path(self, path):
        self.env.loader.searchpath.append(resource_filename(*(path.split(':'))))

    def __call__(self, tname, **kw):
        if not '.jinja2' in tname:
            tname += '.jinja2'

        template = self.env.get_template(tname)
        return template.render(**kw)
