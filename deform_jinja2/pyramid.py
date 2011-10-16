from pkg_resources import resource_filename
from deform_jinja2 import jinja2_renderer_factory
from pyramid import i18n
from pyramid.threadlocal import get_current_request

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

jinja2_template_dir = resource_filename('deform_jinja2', 'templates/')
jinja2_renderer = jinja2_renderer_factory(jinja2_template_dir,
    translator=GetTextWrapper())

