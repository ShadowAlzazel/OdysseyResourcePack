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

# broadsword excluded since 2D
WEAPONS = [
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
        if not os.path.exists(f'{weapon}/composite'):
            os.makedirs(f'{weapon}/composite')
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