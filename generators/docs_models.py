import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
import mean_gen_config
import generators.utils.filters as filters


TEMPLATE_DIR = os.path.join("docs")
TEMPLATE_NAME = "models.js"

def inputType(type):
    if type == "String":
        return "string"
    elif type.__class__.__name__ == 'Reference':
        return 'Reference'
    return "string"

def generate(model):

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("templates", TEMPLATE_DIR))
    env.filters["inputType"] = filters.inputType
    template = env.get_template(TEMPLATE_NAME)

    class Property(object):
        def __init__(self, name, type):
            self.name = name
            self.type = type

        @property
        def label(self):
            return self.name.capitalize()

        def __str__(self):
            tip = self.type
            if self.type.__class__.__name__ == 'Reference':
                tip = 'Reference'
            return self.name + ":" + tip + ":" + self.label


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

            rendered = template.render({'item': item})

            file_path = os.path.join(mean_gen_config.GEN_DIR, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, TEMPLATE_NAME)
            with open(file_name, "w+") as f:
                f.write(rendered)
                print(mean_gen_config.GENERATED_MESSAGE + file_name)