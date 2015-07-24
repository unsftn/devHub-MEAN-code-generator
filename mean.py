from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

mean_mm = metamodel_from_file(
    './lang/mean.tx')
metamodel_export(mean_mm, 'mean_meta.dot')

app = mean_mm.model_from_file('./examples/clue-example.mean')
model_export(app, 'clue-example.dot')
