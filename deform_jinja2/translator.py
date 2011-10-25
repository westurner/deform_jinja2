from pyramid.threadlocal import get_current_request
from translationstring import TranslationStringFactory
from pyramid.i18n import get_localizer

class PyramidTranslator(object):

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

