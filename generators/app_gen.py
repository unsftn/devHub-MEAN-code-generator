import os
import mean_gen_config

def generate(model, gen_dir):

    parts = [block for block in model.blocks if block.__class__.__name__ == "PartType"]

    for part in parts:
        part_pl = part.namePiece.partname.lower() + mean_gen_config.PLURAL
        part_dir = os.path.join(mean_gen_config.GEN_DIR, part_pl)
        if not os.path.exists(part_dir):
            os.makedirs(part_dir)
