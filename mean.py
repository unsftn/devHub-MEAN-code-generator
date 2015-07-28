import os
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

# Project setup
VISUALIZATION_DIR = "visualization"

# current_dir = os.path.dirname(__file__)
# __file__ is unbound in interactive mode
current_dir = os.getcwd()
visualization_dir = os.path.join(current_dir, VISUALIZATION_DIR)
if not os.path.exists(visualization_dir):
    os.makedirs(visualization_dir)

mean_mm = metamodel_from_file(os.path.join(current_dir, 'lang', 'mean.tx'))
metamodel_export(mean_mm, os.path.join(visualization_dir, 'mean_meta.dot'))

app = mean_mm.model_from_file(os.path.join(current_dir, 'examples',
                              'clue-example.mean'))
model_export(app, os.path.join(visualization_dir, 'clue-example.dot'))
