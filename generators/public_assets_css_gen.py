import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
import mean_gen_config
import generators.utils.public_views_models as models
import generators.utils.filters as filters

TEMPLATE_DIR = os.path.join("public", "assets", "css")
TEMPLATE_NAME = "css.css"

def generate(model):

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("templates", TEMPLATE_DIR))
    #dodajemo filter pod nazivom inputType
    env.filters["inputType"] = filters.inputType
    template = env.get_template(TEMPLATE_NAME)

    for block in model.blocks:
        if block.__class__.__name__ == 'PartType':
            itemName = block.namePiece.partname
            itemName_pl = itemName + mean_gen_config.PLURAL
            props = block.propertiesPiece.properties

            properties = [models.Property(prop.name, prop.type, prop.visibility) for prop in props]


            item = models.Item(itemName)
            item.properties = properties

            rendered = template.render({'items': itemName_pl.lower()})

            file_path = os.path.join(mean_gen_config.GEN_DIR, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, itemName_pl.lower() + '.css')
            with open(file_name, "w+") as f:
                f.write(rendered)
                print(mean_gen_config.GENERATED_MESSAGE + file_name)
