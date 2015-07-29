import os
import mean_gen_config
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

def mean_model(file_name):
    """Generates program model from '/examples' and returns it."""

    # current_dir = os.path.dirname(__file__)
    # __file__ is unbound in interactive mode
    current_dir = os.getcwd()
    visualization_dir = os.path.join(current_dir, mean_gen_config.VISUALIZATION_DIR)
    if not os.path.exists(visualization_dir):
        os.makedirs(visualization_dir)

    mean_mm = metamodel_from_file(os.path.join(current_dir, 'lang', 'mean.tx'))
    metamodel_export(mean_mm, os.path.join(visualization_dir, 'mean_meta.dot'))

    app = mean_mm.model_from_file(os.path.join(current_dir, 'examples',
                                               file_name))
    model_export(app, os.path.join(visualization_dir, 'clue-example.dot'))

    return app
