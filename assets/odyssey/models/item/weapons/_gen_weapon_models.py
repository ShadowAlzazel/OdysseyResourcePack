import os 
import json
import itertools

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# Master File for ALL weapons
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

WEAPONS = [
    "longsword"
]
# broadsword excluded since 2D

MATERIALS = [
    "diamond",
    "mithril",
    "iridium",
    "netherite",
    "silver",
    "iron"
]

WEAPON_PARTS = {
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
     "longsword": [
        ["blade",
         "big_blade",
         "fancy_blade",
         "imperial_blade"],
        ["handle"],
        ["hilt",
         "fancy_hilt",
         "imperial_hilt",
         "voyager_hilt"],
        ["pommel"]
    ]
}

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Generate file for composite part
def generate_composite_file(part: str, material: str, weapon_name: str):
    filename = f'{weapon_name}/composite/{part}_{material}.json'
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
def populate_files():
    global MATERIALS
    global WEAPON_PARTS
    global WEAPONS
    # Generate files for weapon material combinations
    for weapon in WEAPONS:
        # create dir if does not exist
        if not os.path.exists(weapon):
            os.makedirs(weapon)
        # Loop for weapon
        for material in MATERIALS:
            part_list = WEAPON_PARTS[weapon]
            combined_parts = list(itertools.chain(*part_list))
            for part in combined_parts:
                generate_composite_file(part, material, weapon)
        

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