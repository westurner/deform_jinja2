# -*- coding: utf-8 -*-

import colander
import deform
import deform_jinja2
import deform_jinja2.translator
import unittest

from colander import Invalid, _
from deform.exception import ValidationFailure
from pyramid import testing
from deform_jinja2.translator import PyramidTranslator
import translationstring

class TestTranslation(unittest.TestCase):
    def setUp(self):
        request = testing.DummyRequest()
        settings={'deform_jinja2.template_search_path':'deform_jinja2:uni_templates'}
        self.config = testing.setUp(request=request, settings=settings)
        self.config.include('deform_jinja2')
        
    def runTest(self):
        # runTest() defined to allow TestTranslation() in console
        pass # pragma no cover
        
    def test_translation(self):
        invalid = None
        # From colander.Range():
        def translate_error(node, value):
            min_err = _(_('${val} is less than minimum value ${min}'), 
                        mapping={'val':'value', 'min':'min'})
            raise Invalid(node, min_err)
        class TestSchema(colander.MappingSchema):
            s = colander.SchemaNode(colander.String(), missing="", validator=translate_error)
        f = deform.Form(TestSchema())
        try:
            a = f.validate([('s', 'invalid')]) # validator not called if missing
        except ValidationFailure, e:
            invalid = e.render()
        assert invalid, "ValidationFailure was not raised"
        assert "ctrlHolder" in invalid, "uni-form template was not used"
        assert "value is less than minimum value min" in invalid
        
    def excercise_translator(self, t):
        assert t.gettext('term') == 'term'
        assert t.ngettext('term', 'terms', 2) == 'terms'
        assert t.ngettext(_('term'), _('terms'), 1) == 'term'
        assert t.ngettext(_('term'), _('terms'), 2) == 'terms'      

    def test_pyramid_translator(self):        
        t = PyramidTranslator()
        _ = translationstring.TranslationStringFactory('deform')
        self.excercise_translator(t)
                
    def test_dummy_translator(self):
        dt = deform_jinja2.DummyTranslator()
        self.excercise_translator(dt)
        
    def test_default_translator_is_dummy(self):
        rf = deform_jinja2.jinja2_renderer_factory() # coverage
        assert rf.env.globals['gettext'] == deform_jinja2.DummyTranslator().gettext
        assert rf.env.globals['ngettext'] == deform_jinja2.DummyTranslator().ngettext
        