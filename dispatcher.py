from mean import mean_model
import importlib
import glob
import sys
import os
import mean_gen_config

current_dir = os.getcwd()
gen_dir = os.path.join(current_dir, mean_gen_config.GEN_DIR)
if not os.path.exists(gen_dir):
    os.makedirs(gen_dir)

model = mean_model('clue-example.mean')

modules = glob.glob(os.path.dirname(os.path.join(os.getcwd(), mean_gen_config.GENERATORS_DIR) + os.sep) + os.sep + "*.py")
generator_names = [os.path.basename(f)[:-3] for f in modules]
for name in generator_names:
    importlib.import_module(mean_gen_config.GENERATORS_DIR + '.' + name).generate(model)
