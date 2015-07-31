import os
import mean_gen_config as gen_cfg
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader, FileSystemLoader

TEMPLATE_DIR = os.path.join("server", "controller")
TEMPLATE_NAME = "controller.js"


def generate(model):
    templateLoader = Environment(loader=PackageLoader("templates", TEMPLATE_DIR))
    template = templateLoader.get_template(TEMPLATE_NAME)
    for block in model.blocks:
        if block.__class__.__name__ == 'PartType':
            itemName = block.namePiece.partname
            itemName_pl = itemName + gen_cfg.PLURAL
            createAction = "create"
            editAction = "update"
            deleteAction = "delete"
            readAction = "read"
            rendered = template.render({'Item' : itemName,'item': itemName.lower(), 'Items': itemName_pl, 'items': itemName_pl.lower(),
                                    'createAction': createAction, 'editAction': editAction,
                                    "deleteAction": deleteAction, 'readAction': readAction})
            file_path = os.path.join(gen_cfg.GEN_DIR, itemName_pl.lower(), TEMPLATE_DIR)
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            file_name = os.path.join(file_path, TEMPLATE_NAME)
            with open(file_name, "w+") as f:
                f.write(rendered)
                print(gen_cfg.GENERATED_MESSAGE + file_name)
