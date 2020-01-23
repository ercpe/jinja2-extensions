from jinja2 import Environment


class TestAnnotateBlockExtension(object):
    
    def _render(self, template_string, **vars):
        env = Environment(extensions=['j2exts.annotateblock'])
        tmpl = env.from_string(template_string)
        return tmpl.render(**vars)
    
    def test_empty_body(self):
        output = self._render("""{% annotateblock 'Some text here' %}{% endannotateblock %}""")
        assert output == ""

        output = self._render("""{% annotateblock 'Some text here' %}\n\n{% endannotateblock %}""")
        assert output == "\n\n"

        output = self._render("""{% annotateblock 'Some text here' %}\n              \n{% endannotateblock %}""")
        assert output == "\n              \n"

    def test_add_annotation(self):
        output = self._render("""{% annotateblock 'Some text here' %}some body{% endannotateblock %}""")
        assert output == "Some text here\nsome body"

    def test_add_annotation_with_spaces(self):
        output = self._render("""{% annotateblock 'Some text here' %}      some indented body{% endannotateblock %}""")
        assert output == "      Some text here\n      some indented body"
