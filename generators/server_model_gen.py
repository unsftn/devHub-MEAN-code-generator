import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
import mean_gen_config
import copy

TEMPLATE_DIR = os.path.join("server", "model")
TEMPLATE_NAME = "model.js"

def inputType(type):
    if type == "String":
        return "text"
    return "String"

def generate(model):

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("templates", TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_NAME)
    env.filters["inputType"] = inputType

    class Property(object):
        def __init__(self, name, type):
            self.name = name
            self.type = type

        @property
        def label(self):
            return self.name.capitalize()

        def __str__(self):
            return self.name + ":" + self.label


    class Item(object):

        def __init__(self, name):
            self.name = name
            self._properties = []

        @property
        def properties(self):
            return self._properties

        @properties.setter
        def properties(self, value):
            if not isinstance(value, list):
                raise TypeError("Properties must be a list!")
            self._properties = value


    for block in model.blocks:
        if block.__class__.__name__ == 'PartType':
            itemName = block.namePiece.partname
            itemName_pl = itemName + mean_gen_config.PLURAL
            props = block.propertiesPiece.properties

            properties = [Property(prop.name, prop.type) for prop in props]

            item = Item(itemName)
            item.properties = properties

            rendered = template.render({ 'item': item})

            file_path = os.path.join(mean_gen_config.GEN_DIR, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, "article.js")
            with open(file_name, "w+") as f:
                f.write(rendered)
                print(mean_gen_config.GENERATED_MESSAGE + file_name)
