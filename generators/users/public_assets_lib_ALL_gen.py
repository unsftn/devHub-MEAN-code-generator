import os
import mean_gen_config
import distutils.dir_util as dir_util

def generate(model):
    src =  os.path.join(*[mean_gen_config.TEMPLATES_DIR,
                          mean_gen_config.USERS_TEMPLATE_DIR,
                          mean_gen_config.USERS_PUBLIC_DIR,
                          mean_gen_config.USERS_PUBLIC_ASSETS_DIR,
                          mean_gen_config.USERS_PUBLIC_ASSETS_LIB_DIR])

    dest = os.path.join(*[mean_gen_config.GEN_DIR,
                          mean_gen_config.GEN_DIR_USERS,
                          mean_gen_config.USERS_PUBLIC_DIR,
                          mean_gen_config.USERS_PUBLIC_ASSETS_DIR,
                          mean_gen_config.USERS_PUBLIC_ASSETS_LIB_DIR])

    dir_util.copy_tree(src, dest)

    print(mean_gen_config.GENERATED_MESSAGE + mean_gen_config.DEFAULT_USER_GENERATED_MESSAGE + dest + os.sep + '*')
