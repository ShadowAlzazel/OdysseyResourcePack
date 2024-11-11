import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

WEAPON_NAME = "broadsword"

MATERIALS = [
    'wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite',
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril'
]

PARTS = [
    "big_blade",
    "blade",
    "fancy_blade",
    "fancy_hilt",
    "fancy_pommel",
    "handle",
    "hilt",
    "imperial_hilt",
    "longer_blade",
    "pommel",
    "thick_blade",
    "voyager_hilt"
]

# Generate file for composite part
def generate_composite_file(part: str, material: str, weapon_name: str):
    filename = f'composite/{part}_{material}.json'
    # create json obj
    json_obj = {
        "parent": f'odyssey:item/weapons/{weapon_name}/{part}',
        "textures": {
            "layer0": f'odyssey:item/weapon/composite/{weapon_name}/{part}_{material}'
        }
    }
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text) 

# Generate file for parent part
def generate_parent_file(part: str, weapon_name: str):
    filename = f'{part}.json'
    # create json obj
    json_obj = {
        "parent": "minecraft:item/handheld",
        "textures": {
            "layer0": f'odyssey:item/weapon/composite/{weapon_name}/{part}'
        }
    }
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text) 


# poulate files
def populate_files(weapon_name: str):
    global MATERIALS
    global PARTS
    # Generate base parent files
    for part in PARTS:
        generate_parent_file(part, weapon_name)
    
    # Generate files for all composite combinations
    for material in MATERIALS:
        for part in PARTS:
            generate_composite_file(part, material, weapon_name)
        

# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        populate_files(WEAPON_NAME) 
        
# Main
if __name__ == "__main__":
    main()