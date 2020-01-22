from jinja2 import Environment


class TestAutoIndentExtension(object):
    
    def test_autoindent(self):
        env = Environment(extensions=['j2exts.autoindent'])
        tmpl = env.from_string("""{% autoindent 4 %}sometext{%endautoindent%}""")
        
        output = tmpl.render()
        
        assert output == "    sometext"
    
    def test_autoindent_multiline(self):
        env = Environment(extensions=['j2exts.autoindent'])
        
        multiline_text = """Foo\nBar\nBaz"""
        
        tmpl = env.from_string("""{% autoindent 4 %}
    {{somevar}}
    {% endautoindent %}""")
        
        output = tmpl.render(somevar=multiline_text)
        assert output == """
    Foo
    Bar
    Baz
    """
