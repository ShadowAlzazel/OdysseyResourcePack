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

MATERIALS = [
    'wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite',
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril'
]

# All patterns
WEAPON_TRIMS = [
    "jewel",
    "spine",
    "wings",
    "cross",
    "trace"
]

#Name to namespace
TRIM_MATERIAL_MAP = {
    'alexandrite': "odyssey",
    'anodized_titanium': "odyssey", 
    'iridium': "odyssey",
    'jade': "odyssey", 
    'jovianite': "odyssey",
    'kunzite': "odyssey", 
    'mithril': "odyssey", 
    'neptunian': "odyssey",
    'obsidian': "odyssey", 
    'ruby': "odyssey",
    'silver': "odyssey", 
    'soul_quartz': "odyssey",
    'soul_steel': "odyssey", 
    'titanium': "odyssey",
    
    "quartz": "minecraft",
    "iron": "minecraft",
    "netherite": "minecraft",
    "redstone": "minecraft",
    "copper": "minecraft",
    "gold": "minecraft",
    "emerald": "minecraft",
    "diamond": "minecraft",
    "lapis": "minecraft",
    "amethyst": "minecraft",
    "resin": "minecraft"
}

# Starter set for the 9 basic parts
WEAPON_PART_SETS = [
    "crusader",
    "danger",
    "fancy",
    "humble",
    "imperial",
    "marauder",
    "seraph",
    "vandal",
    "voyager"
]

ALL_BLADES = ["blade"] + [f'{x}_blade' for x in WEAPON_PART_SETS]
ALL_HILTS = ["hilt"] + [f'{x}_hilt' for x in WEAPON_PART_SETS]
ALL_POMMELS = ["pommel"] + [f'{x}_pommel' for x in WEAPON_PART_SETS]

# --------------------------------------------------------------------------

# broadsword excluded since 2D
WEAPONS = [
    "longsword",
    "cutlass",
    "claymore",
    "dagger",
    "sickle",
    "saber",
    "kriegsmesser",
    "katana",
]

WEAPON_PARTS = {
    "longsword": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "cutlass": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "claymore": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "dagger": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "sickle": [ ["blade"], ["handle"], ["hilt"], ["pommel"]],
    "saber": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "kriegsmesser": [ ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
    "katana": [ALL_BLADES, ["handle"], ALL_HILTS, ALL_POMMELS],
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
            "layer0": f'odyssey:item/weapon/{weapon_name}/{part}_{material}'
        }
    }
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as f:
        f.write(text) 
        
        
# Generate parent file that all materials inherit
def generate_parent_file(name: str, weapon_name: str):
    filename = f'{weapon_name}/{name}.json'
    # create json obj
    json_obj = {
        "parent": f'odyssey:item/weapons/{weapon_name}/_base',
        "textures": {
            "layer0": f'odyssey:item/weapon/{weapon_name}/{name}'
        }
    }
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as f:
        f.write(text) 


# Generate file for composite part
def generate_trim_file(trim_name: str, material: str, weapon_name: str):
    filename = f'{weapon_name}/trims/{trim_name}_{material}_trim.json'
    # create json obj
    json_obj = {
        "parent": f'odyssey:item/weapons/{weapon_name}/{trim_name}_trim',
        "textures": {
            "layer0": f'odyssey:item/weapon/{weapon_name}/{trim_name}_trim_{material}'
        }
    }
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as f:
        f.write(text) 


# poulate files
def populate_files():
    # Loop throgh all weapons
    for weapon in WEAPONS:
        # create dir if does not exist
        if not os.path.exists(weapon):
            os.makedirs(weapon)
        if not os.path.exists(f'{weapon}/composite'):
            os.makedirs(f'{weapon}/composite')
        if not os.path.exists(f'{weapon}/trims'):
            os.makedirs(f'{weapon}/trims')
        # Generate files for base parts and material parts
        for material in MATERIALS:
            part_list = WEAPON_PARTS[weapon]
            # Create one list to loop through materials
            combined_parts = list(itertools.chain(*part_list))
            for part in combined_parts:
                generate_composite_file(part, material, weapon)
                generate_parent_file(part, weapon)
        # TRIMS
        # Generate for trims
        if weapon == "longsword" or weapon == "kriegsmesser": # Test
            for trim in WEAPON_TRIMS:
                generate_parent_file(f'{trim}_trim', weapon)
                for material, namespace in TRIM_MATERIAL_MAP.items():
                    generate_trim_file(trim, material, weapon)

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