__author__ = 'student2014'

import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

TEMPLATE_DIR = "public" + os.sep + "controller"

def generate(model):

    print('public ctrl gen')

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("templates", TEMPLATE_DIR))

    template = env.get_template("controller.js")
    rendered = template.render({'item': 'article', 'Items': 'Articles', 'items': 'articles'})
    print(rendered)