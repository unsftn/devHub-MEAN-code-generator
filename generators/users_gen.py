import importlib
import glob
import sys
import os
import mean_gen_config

def generate(model):
    '''Used as dispatcher for users package.'''

    users_generators_dir = os.path.join(mean_gen_config.GENERATORS_DIR , mean_gen_config.USERS_GENERATORS_DIR)
    modules = glob.glob(os.path.dirname(users_generators_dir + os.sep) + os.sep + "*.py")
    generator_names = [os.path.basename(f)[:-3] for f in modules]
    for name in generator_names:
        importlib.import_module(mean_gen_config.GENERATORS_DIR + '.' +
                                mean_gen_config.USERS_GENERATORS_DIR + '.' + name).generate(model)
