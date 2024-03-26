import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# TODO 
# Add [Polexe], [Battleaxe(labrys)]
# Rework [Rapier], [Lance]

weapon_types = ['charkam', 'claymore', 'cutlass', 'dagger', 'halberd', 'katana', 'kunai', 'lance', 
                'longaxe', 'longsword', 'rapier', 'saber', 'scythe', 'sickle', 'spear', 'warhammer']
materials = ['wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite'
             'copper', 'mithril', 'soul_steel']

# Check 
print("Confirm Creation of New files? This will overwrite old files (y/n) . . .")
answer = inputs()

# Create files
if answer == "y":
    pass 


def create_files():
    for i in range(len(materials)):
        for j in range(len(weapon_types)):
            mat = materials[i]
            wtyp = weapon_types[j]
            # Create json obj to make interpolation easier
            filename = f'{mat}_{wtyp}.json'
            json_obj = {
                "parent": f"odyssey:item/weapons/bases/{wtyp}",
                "textures": {
                    "0": f"odyssey:item/weapons/{wtyp}_texture_{mat}",
                    "particle": f"odyssey:item/weapons/{wtyp}_texture_{mat}"
                }
            }
            #text = f'{"parent": "odyssey:item/weapons/bases/{wtyp}", "textures": {"0": "odyssey:item/weapons/longaxe_texture_diamond", "particle": "odyssey:item/weapons/longaxe_texture_diamond"}}'
            text = json.dumps(json_obj)
            # Write the text to opened file
            with open(filename, 'w') as file:
                file.write(text)
            