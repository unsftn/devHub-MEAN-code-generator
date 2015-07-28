from mean import mean_model
import importlib
import glob
import sys
import os

GENERATORS_DIR = "generators"

model = mean_model('clue-example.mean')

modules = glob.glob(os.path.dirname(os.path.join(os.getcwd(), GENERATORS_DIR) + os.sep) + os.sep + "*.py")
generator_names = [os.path.basename(f)[:-3] for f in modules]
for name in generator_names:
    importlib.import_module(GENERATORS_DIR + '.' + name).generate(model)
