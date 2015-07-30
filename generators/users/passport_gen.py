import os
import mean_gen_config
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

TEMPLATE_NAME = "passport.js"

def generate(model):
    env = Environment(trim_blocks=True, lstrip_blocks=True,
                      loader=PackageLoader(mean_gen_config.TEMPLATES_DIR,
                                           mean_gen_config. USERS_TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_NAME)
    rendered = template.render()

    users_dir = os.path.join(mean_gen_config.GEN_DIR, mean_gen_config.GEN_DIR_USERS)
    if not os.path.exists(users_dir):
        os.makedirs(users_dir)

    file_name = os.path.join(users_dir, TEMPLATE_NAME)
    with open(file_name, "w+") as f:
        f.write(rendered)
        print(mean_gen_config.GENERATED_MESSAGE + mean_gen_config.DEFAULT_USER_GENERATED_MESSAGE + file_name)
