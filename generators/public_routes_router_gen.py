import os
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
import mean_gen_config as gen_cfg

TEMPLATE_DIR = os.path.join("public", "routes")
TEMPLATE_NAME = "router.js"

def generate(model, gen_dir):

    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("templates", TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_NAME)

    for block in model.blocks:
        if block.__class__.__name__ == 'PartType':
            itemName = block.namePiece.partname
            itemName_pl = itemName + gen_cfg.PLURAL

            rendered = template.render({'item': itemName.lower(), 'items': itemName_pl.lower()})

            file_path = os.path.join(gen_dir, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, TEMPLATE_NAME)
            with open(file_name, "w+") as f:
                f.write(rendered)
                print('generated ' + file_name)