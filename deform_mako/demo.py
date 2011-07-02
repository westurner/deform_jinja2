from pkg_resources import resource_filename
from translationstring import TranslationStringFactory
from pyramid.i18n import get_localizer
from pyramid.threadlocal import get_current_request
from deform_mako import mako_renderer_factory

def translator(term, domain='deform'):
    if not hasattr(term, 'interpolate'): # not a translation string
        term = TranslationStringFactory(domain)(term)
    return get_localizer(get_current_request()).translate(term)

mako_template_dir = resource_filename('deform_mako', 'templates/')

mako_renderer = mako_renderer_factory(
    mako_template_dir,
    translator=translator,
    )

