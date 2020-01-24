import os
import re

from jinja2 import nodes
from jinja2.ext import Extension


class AnnotateBlockExtension(Extension):
    tags = {'annotateblock'}

    def __init__(self, environment):
        super(AnnotateBlockExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]
    
        body = parser.parse_statements(['name:endannotateblock'], drop_needle=True)
    
        return nodes.CallBlock(self.call_method('_annotate', args), [], [], body).set_lineno(lineno)

    def _annotate(self, header, caller):
        
        body = caller()
        
        if not header or body is None or not body.strip():
            return body
        
        lines = body.split(os.linesep)
        
        # find first indention level
        indent = ""
        for l in lines:
            m = re.match(r'^(\s+)[^\s]+', l, flags=re.IGNORECASE | re.UNICODE)
            if m:
                indent = m.group(1)
                break
        
        return f'{indent}{header}{os.linesep}{body}'
