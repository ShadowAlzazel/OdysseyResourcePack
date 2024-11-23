import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Glyph material can never be changed, table can
GLYPH_MAP = {
    'minor_glyph': ["clay", "silver"], # Flat -> turns into brick when fired retains silver
    'glyphsherd': ["brick", "diamond"]  # Flat (diamond denotes original)
}

GLYPHS = [
    "assault", 
    "break",
    "feather", 
    "finesse", 
    "force", 
    "gravity", 
    "guard", 
    "grasp", 
    "jump", 
    "range",
    "size",
    "steadfast",
    "swift", 
    "vitality",
    "unknown" # has no stats
]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Create case obj
def create_parent_obg(): 
    parent_obj = {
        "model": {
            "type": "minecraft:composite",
            "models": []
        }
    } 
    return parent_obj

# Create select model obj that chooses model
def create_glyph_selecter(material: str):
    glyph_selecter_obj = {
        "type": "minecraft:select",
        "cases": [],
        "fallback": {
            "type":"minecraft:model",
            "model": f'odyssey:item/glyphs/unknown_glyph_{material}'
        },
        "property": "minecraft:custom_model_data",
        "index": 1
    } 
    return glyph_selecter_obj

# Create part case obj
def create_case_glyph(glyph: str, material: str):
    case_obj = {
        "model": {
            "type": "minecraft:model",
            "model": f'odyssey:item/glyphs/{glyph}_glyph_{material}'
        },
        "when": f'{glyph}'
    }
    return case_obj

def create_tablet_obj(tablet: str):
    tablet_obj = {
        "type": "minecraft:model",
        "model": f'odyssey:item/glyphs/{tablet}_tablet'
    }
    return tablet_obj

# generate files for glyphs item
def generate_files(glyphic_item: str, tablet: str, material: str):
    filename = f'{glyphic_item}.json'
    # create objs
    json_obj = create_parent_obg()
    tablet_obj = create_tablet_obj(tablet)
    # Create glyph selecter model
    glyph_selecter_obj = create_glyph_selecter(material)
    for glyph in GLYPHS:
        case_obj = create_case_glyph(glyph, material)
        glyph_selecter_obj["cases"].append(case_obj)
    # Merge
    model_list = [tablet_obj, glyph_selecter_obj]
    json_obj["model"]["models"] = model_list
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text)


# poulate files
def populate_files():
    # Generate files for glyphs items
    for glyphic_item, glyphs_parts in GLYPH_MAP.items():
        tablet = glyphs_parts[0]
        material = glyphs_parts[1]
        generate_files(glyphic_item, tablet, material)
       
# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        populate_files() 
        
# Main
if __name__ == "__main__":
    main()