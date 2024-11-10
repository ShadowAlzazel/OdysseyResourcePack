import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# Edit these

WEAPON_NAME = "longsword"

MATERIALS = [
    "diamond",
    "mithril",
    "iridium",
    "netherite",
    "silver"
]

PARTS = [
    "imperial_blade",
    "blade",
    "fancy_blade",
    "handle",
    "hilt",
    "imperial_hilt",
    "pommel"
]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Generate file for composite part
def generate_composite_file(part: str, material: str, weapon_name: str):
    filename = f'composite/{part}_{material}.json'
    # create json obj
    json_obj = {
        "parent": f'odyssey:item/weapons/{weapon_name}/{part}',
        "textures": {
            "0": f'odyssey:item/weapon/composite/{weapon_name}/{part}_{material}',
            "particle": f'odyssey:item/weapon/composite/{weapon_name}/{part}_{material}'
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
    # Generate base parent files (only for static)
    #for part in PARTS:
    #    generate_parent_file(part, weapon_name)
    
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