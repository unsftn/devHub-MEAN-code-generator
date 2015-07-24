from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

# Project setup
visualization_dir = "./visualization"
if not os.path.exists(visualization_dir):
    os.makedirs(visualization_dir)

mean_mm = metamodel_from_file('./lang/mean.tx')
metamodel_export(mean_mm, visualization_dir + '/mean_meta.dot')

app = mean_mm.model_from_file('./examples/clue-example.mean')
model_export(app, visualization_dir + '/clue-example.dot')
