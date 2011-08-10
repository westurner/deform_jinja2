import os
from mako.template import Template

class mako_renderer_factory(object):
    def __init__(self, directory, translator=None):
        self.directory = directory
        self.translate = translator

    def __call__(self, tname, **kw):
        filename = os.path.join(self.directory, tname) + '.mako'
        template = Template(filename=filename)
        return template.render(_=self.translate, **kw)
       
