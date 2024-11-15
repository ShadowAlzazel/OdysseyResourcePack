import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Sigil material can never be changed
RUNIC_MAP = {
    'runepiece': ["clay", "silver"], # Flat -> turns into brick when fired retains silver
    'runesherd': ["brick", "diamond"]  # Flat (diamond denotes original)
}

SIGILS = [
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
def create_sigil_selecter(material: str):
    sigil_selecter_obj = {
        "type": "minecraft:select",
        "cases": [],
        "fallback": {
            "type":"minecraft:model",
            "model": f'odyssey:item/runic/unknown_sigil_{material}'
        },
        "property": "minecraft:custom_model_data",
        "index": 1
    } 
    return sigil_selecter_obj

# Create part case obj
def create_case_sigil(sigil: str, material: str):
    case_obj = {
        "model": {
            "type": "minecraft:model",
            "model": f'odyssey:item/runic/{sigil}_sigil_{material}'
        },
        "when": f'{sigil}'
    }
    return case_obj

def create_tablet_obj(tablet: str):
    tablet_obj = {
        "type": "minecraft:model",
        "model": f'odyssey:item/runic/{tablet}_tablet'
    }
    return tablet_obj

# generate files for rune item
def generate_files(rune_item: str, tablet: str, material: str):
    filename = f'{rune_item}.json'
    # create objs
    json_obj = create_parent_obg()
    tablet_obj = create_tablet_obj(tablet)
    # Create sigil selecter model
    sigil_selecter_obj = create_sigil_selecter(material)
    for sigil in SIGILS:
        case_obj = create_case_sigil(sigil, material)
        sigil_selecter_obj["cases"].append(case_obj)
    # Merge
    model_list = [tablet_obj, sigil_selecter_obj]
    json_obj["model"]["models"] = model_list
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text)


# poulate files
def populate_files():
    # Generate files for rune items
    for rune_item, rune_parts in RUNIC_MAP.items():
        tablet = rune_parts[0]
        material = rune_parts[1]
        generate_files(rune_item, tablet, material)
       
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