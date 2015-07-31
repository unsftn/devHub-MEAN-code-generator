import os
import mean_gen_config
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

TEMPLATE_NAME = "meanUser.css"

def generate(model):
    users_template_dir =  os.path.join(*[mean_gen_config. USERS_TEMPLATE_DIR,
                                   mean_gen_config.USERS_PUBLIC_DIR,
                                   mean_gen_config.USERS_PUBLIC_ASSETS_DIR,
                                   mean_gen_config.USERS_PUBLIC_ASSETS_CSS_DIR])
    env = Environment(trim_blocks=True, lstrip_blocks=True,
                      loader=PackageLoader(mean_gen_config.TEMPLATES_DIR, users_template_dir))
    template = env.get_template(TEMPLATE_NAME)
    rendered = template.render()

    users_dir = os.path.join(mean_gen_config.GEN_DIR, mean_gen_config.GEN_DIR_USERS)
    if not os.path.exists(users_dir):
        os.makedirs(users_dir)

    users_public_dir = os.path.join(mean_gen_config.GEN_DIR,
                                               mean_gen_config.GEN_DIR_USERS,
                                               mean_gen_config.USERS_PUBLIC_DIR)
    if not os.path.exists(users_public_dir):
        os.makedirs(users_public_dir)

    users_public_assets_dir = os.path.join(mean_gen_config.GEN_DIR,
                                               mean_gen_config.GEN_DIR_USERS,
                                               mean_gen_config.USERS_PUBLIC_DIR,
                                               mean_gen_config.USERS_PUBLIC_ASSETS_DIR)
    if not os.path.exists(users_public_assets_dir):
        os.makedirs(users_public_assets_dir)

    users_public_assets_css_dir = os.path.join(mean_gen_config.GEN_DIR,
                                               mean_gen_config.GEN_DIR_USERS,
                                               mean_gen_config.USERS_PUBLIC_DIR,
                                               mean_gen_config.USERS_PUBLIC_ASSETS_DIR,
                                               mean_gen_config.USERS_PUBLIC_ASSETS_CSS_DIR)
    if not os.path.exists(users_public_assets_css_dir):
        os.makedirs(users_public_assets_css_dir)

    file_name = os.path.join(users_public_assets_css_dir, TEMPLATE_NAME)
    with open(file_name, "w+") as f:
        f.write(rendered)
        print(mean_gen_config.GENERATED_MESSAGE + mean_gen_config.DEFAULT_USER_GENERATED_MESSAGE + file_name)
