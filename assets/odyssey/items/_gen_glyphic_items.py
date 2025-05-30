import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Glyph material can never be changed, tablet can
# Glyph material denotes the level of the ENSCRIBED glyph and its power/stats
GLYPH_MAP = {
    #'glyphpiece': ["brick", "silver"], # Flat -> turns into brick when fired
    'glyphsherd': ["brick", "diamond"],  # Flat (denotes original)
    #'minor_glyph': ["brick", "silver"], # Flat -> turns into brick when fired
    #'major_glyph': ["tuff", "diamond"],  # Flat * 1.5  
    #'nether_glyph': ["nether_brick", "gold"],  # Percent +10% 
    #'ancient_glyphsherd': ["deepslate", "mithril"]  # Percent +20% 
}

GLYPHS = [
    "assault", 
    "break",
    #"feather", 
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
def create_tablet_selecter(tablet: str):
    tablet_selecter_obj = {
        "type": "minecraft:select",
        "cases": [],
        "fallback": {
            "type":"minecraft:model",
            "model": f'odyssey:item/glyphs/{tablet}_tablet'
        },
        "property": "minecraft:custom_model_data",
        "index": 2
    } 
    return tablet_selecter_obj


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


def create_case_tablet(tablet: str):
    tablet_obj = {
        "model": {
            "type": "minecraft:model",
            "model": f'odyssey:item/glyphs/{tablet}_tablet'
        },
        "when": f'{tablet}'
    }
    return tablet_obj


def create_tablet_obj(tablet: str):
    tablet_obj = {
        "type": "minecraft:model",
        "model": f'odyssey:item/glyphs/{tablet}_tablet'
    }
    return tablet_obj


def create_glyph_obj(glyph: str, material: str):
    tablet_obj = {
        "type": "minecraft:model",
        "model": f'odyssey:item/glyphs/{glyph}_glyph_{material}'
    }
    return tablet_obj


# generate files for glyphs item
def generate_composite_glyph(glyphic_item: str, tablet: str, material: str):
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
    # Write to file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as f:
        f.write(text)
        

def generate_single_glyph(category: str, glyph: str, tablet: str, material: str):
    filename = f'{glyph}_{category}.json'
    # create objs
    json_obj = create_parent_obg()
    tablet_obj = create_tablet_obj(tablet)
    glyph_obj = create_glyph_obj(glyph, material)
    # Merge
    model_list = [tablet_obj, glyph_obj]
    json_obj["model"]["models"] = model_list
    # Write to file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as f:
        f.write(text)


# poulate files
def populate_files():
    # Generate files for glyphs items
    for category, glyphs_parts in GLYPH_MAP.items():
        tablet = glyphs_parts[0]
        material = glyphs_parts[1]
        for glyph in GLYPHS:
            generate_single_glyph(category, glyph, tablet, material)
       
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