from deform_jinja2.translator import PyramidTranslator
from deform_jinja2 import jinja2_renderer_factory

jinja2_renderer = jinja2_renderer_factory(search_paths=('deformdemo:templates/',), translator=PyramidTranslator())
