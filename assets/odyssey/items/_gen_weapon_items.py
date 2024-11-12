import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

WEAPONS = [
    "broadsword",
    "longsword",
    "katana"
]

MATERIALS = [
    'wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite',
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril'
]

WEAPON_PARTS = {
    "longsword": [
        ["blade",
         "big_blade",
         "fancy_blade",
         "imperial_blade",
         "marauder_blade",
         "crusader_blade",
         "vandal_blade",
         "seraph_blade",
         "voyager_blade"],
        ["handle"],
        ["hilt",
         "fancy_hilt",
         "imperial_hilt",
         "voyager_hilt",
         "marauder_hilt",
         "crusader_hilt",
         "danger_hilt",
         "vandal_hilt",
         "seraph_hilt"],
        ["pommel",
         "imperial_pommel",
         "fancy_pommel",
         "marauder_pommel",
         "vandal_pommel",
         "crusader_pommel",
         "seraph_pommel",
         "danger_pommel",
         "voyager_pommel"]
    ],
    "katana": [
        ["blade",
         "seraph_blade",
         "imperial_blade",
         "fancy_blade",
         "voyager_blade"],
        ["handle"],
        ["hilt",
         "seraph_hilt",
         "imperial_hilt",
         "fancy_hilt",
         "voyager_hilt"],
        ["pommel",
         "seraph_pommel",
         "imperial_pommel",
         "fancy_pommel",
         "voyager_pommel"]
    ],
    "broadsword": [
        ["blade",
         "fancy_blade",
         "big_blade"],
        ["handle"],
        ["hilt",
         "fancy_hilt",
         "imperial_hilt",
         "voyager_hilt"],
        ["pommel",
         "fancy_pommel"]
    ],
}

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
def create_part_selecter_obj(weapon: str, material: str, part_name: str, index: int): 
    part_selecter_obj = {
        "type": "minecraft:select",
        "cases": [],
        "fallback": {
            "type":"minecraft:model",
            "model": f'odyssey:item/weapons/{weapon}/composite/{part_name}_{material}'
        },
        "property": "minecraft:custom_model_data",
        "index": index
    } 
    return part_selecter_obj

# Create part case obj
def create_case_obj(weapon: str, material: str, part_name: str):
    case_obj = {
        "model": {
            "type": "minecraft:model",
            "model": f'odyssey:item/weapons/{weapon}/composite/{part_name}_{material}'
        },
        "when": f'{part_name}'
    }
    return case_obj

# Create parts for the sub_models from the weapon parts list
def create_model_parts(weapon: str, material: str):
    # The first entry in WEAPON_PARTS is the fallback part
    global WEAPON_PARTS
    list_count = 1
    # Loop through all parts and append to select obj
    model_list = []
    for part_list in WEAPON_PARTS[weapon]:
        part_selecter_obj = create_part_selecter_obj(weapon, material, part_list[0], list_count)
        # Populate cases
        for part in part_list:
            case_obj = create_case_obj(weapon, material, part)
            part_selecter_obj["cases"].append(case_obj)
        list_count += 1
        model_list.append(part_selecter_obj)
        
    return model_list

# Generate files for list
def create_weapon_file(weapon: str, material: str):
    item_name = f'{material}_{weapon}'
    filename = f'{item_name}.json'
    # create objs
    json_obj = create_parent_obg()
    model_list = create_model_parts(weapon, material)
    json_obj["model"]["models"] = model_list
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text)   


# poulate files
def populate_files():
    # Generate files for weapon material combinations
    for weapon in WEAPONS:
        for material in MATERIALS:
            create_weapon_file(weapon, material)
        

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