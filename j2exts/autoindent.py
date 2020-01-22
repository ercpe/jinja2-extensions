import os

from jinja2 import nodes
from jinja2.ext import Extension


class AutoIndentExtension(Extension):
    """
    Usage:
    
    {% autoindent 4 %}
    {% someothertag %}
    {% endautoindent %}
    """
    
    tags = {'autoindent'}

    def __init__(self, environment):
        super(AutoIndentExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]
        
        body = parser.parse_statements(['name:endautoindent'], drop_needle=True)

        return nodes.CallBlock(self.call_method('_autoindent', args), [], [], body).set_lineno(lineno)

    def _autoindent(self, indent, caller):
        
        def _do_indent():
            for line in caller().split(os.linesep):
                whitespaces = f"{' ' * indent}"
                if line and not line.startswith(whitespaces):
                    yield f"{whitespaces}{line}"
                else:
                    yield line
        
        return os.linesep.join(_do_indent())
