from pkg_resources import resource_filename
from deform_jinja2 import jinja2_renderer_factory
from deform_jinja2 import GetTextWrapper

jinja2_template_dir = resource_filename('deform_jinja2', 'uni_templates/')
jinja2_renderer = jinja2_renderer_factory(jinja2_template_dir,
    translator=GetTextWrapper())

