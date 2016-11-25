
import os
import jinja2
import webapp2

import src.pages.base as base

JINJA_ENV = jinja2.Environment(
 loader=jinja2.FileSystemLoader(base.BASE_PATH),
 extensions=['jinja2.ext.autoescape'],
 autoescape=True)
 
class FunWithCoffeescriptAndBackbone1(webapp2.RequestHandler):
   """
   Displays article Fun with Coffeescript and Backbone.js (Part 1)
   """
   def get(self):
      template = JINJA_ENV.get_template('articles/fun_with_coffeescript_and_backbone/fun_with_coffeescript_and_backbone_1.html')
      self.response.write(template.render())
   #
#

app = webapp2.WSGIApplication([('/articles/fun_with_coffeescript_and_backbone_1', FunWithCoffeescriptAndBackbone1)])