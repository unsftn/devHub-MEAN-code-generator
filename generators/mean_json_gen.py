import os
import mean_gen_config
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

TEMPLATE_NAME = "mean.json"

def generate(model):
    parts = [block for block in model.blocks if block.__class__.__name__ == "PartType"]

    for part in parts:
        part_pl = part.namePiece.partname.lower() + mean_gen_config.PLURAL
        part_dir = os.path.join(mean_gen_config.GEN_DIR, part_pl)
        if not os.path.exists(part_dir):
            os.makedirs(part_dir)

        env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader(mean_gen_config.TEMPLATES_DIR, '.'))
        template = env.get_template(TEMPLATE_NAME)
        rendered = template.render()

        file_name = os.path.join(part_dir, TEMPLATE_NAME)
        with open(file_name, "w+") as f:
            f.write(rendered)
            print(mean_gen_config.GENERATED_MESSAGE + file_name)
