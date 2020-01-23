import re

from jinja2 import nodes
from jinja2.ext import Extension


class StripWsExtension(Extension):
    """
    Usage:

    {% stripws %}
    
    {% endstripws %}
    """
    
    tags = {'stripws'}
    
    def __init__(self, environment):
        super(StripWsExtension, self).__init__(environment)

    def parse(self, parser):

        lineno = next(parser.stream).lineno
#        args = [parser.parse_expression()]
        args = []
    
        body = parser.parse_statements(['name:endstripws'], drop_needle=True)
   
        return nodes.CallBlock(self.call_method('_strip_ws', args), [], [], body).set_lineno(lineno)

    def _strip_ws(self, caller):
        block_content = caller()
        
        if block_content is None:
            return block_content

        return re.sub(r'(?:\n\s*\n(\s*)\n)+', '\n\n\1', block_content, flags=re.MULTILINE | re.UNICODE | re.IGNORECASE)
