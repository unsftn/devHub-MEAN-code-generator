import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
import mean_gen_config

TEMPLATE_DIR = os.path.join("public", "controller")
TEMPLATE_NAME = "controller.js"

def generate(model):

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader(mean_gen_config.TEMPLATES_DIR , TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_NAME)

    for block in model.blocks:
        if block.__class__.__name__ == 'PartType':
            itemName = block.namePiece.partname
            itemName_pl = itemName + mean_gen_config.PLURAL

            rendered = template.render({'item': itemName.lower(), 'Items': itemName_pl, 'items': itemName_pl.lower()})

            file_path = os.path.join(mean_gen_config.GEN_DIR, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, TEMPLATE_NAME)
            with open(file_name, "w+") as f:
                f.write(rendered)
                print(mean_gen_config.GENERATED_MESSAGE + file_name)
