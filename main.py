#!/usr/bin/env python
import os
import jinja2
import webapp2
import sys
from properties import check_hair_color, check_face_shape, check_eyes_color, check_gender, check_race

reload(sys)
sys.setdefaultencoding("utf-8")

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

    def post(self):
        character = self.request.get("dna")
        hair_color = check_hair_color(character)
        face_shape = check_face_shape(character)
        eyes_color = check_eyes_color(character)
        gender = check_gender(character)
        race = check_race(character)

        params = {"barva_las": hair_color, "obraz": face_shape, "barva_oci": eyes_color, "spol": gender, "rasa": race}
        return self.render_template("index.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
