from jinja2 import Environment


class TestStripWsExtension(object):
    
    def _render(self, template_string, **vars):
        env = Environment(extensions=['j2exts.stripws'])
        tmpl = env.from_string(template_string)
        return tmpl.render(**vars)

    def test_strip_ws_no_match(self):
        output = self._render("""{% stripws %}sometext{% endstripws %}""")
        assert output == "sometext"
    
    def test_single_newline(self):
        
        output = self._render("""{% stripws %}
        sometext{% endstripws %}""")
        assert output == "\n        sometext"
        
    def test_multiple_newlines(self):
        
        output = self._render("""{% stripws %}
        sometext
        
        
        someothertext{% endstripws %}""")
        assert output == "\n        sometext\n\n        someothertext"

    def test_dont_replace(self):
        output = self._render("""{% stripws %}\nfoo\n\n    bar{% endstripws %}""")
        assert output == "\nfoo\n\n    bar"

