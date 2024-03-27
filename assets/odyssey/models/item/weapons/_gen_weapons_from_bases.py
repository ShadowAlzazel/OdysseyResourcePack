import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# TODO 
# Add [Polexe], [Battleaxe(labrys)]
# Rework [Rapier], [Lance]

tool_types = ['chakram', 'claymore', 'cutlass', 'dagger', 'halberd', 'katana', 'kunai', 'lance', 
                'longaxe', 'longsword', 'rapier', 'saber', 'scythe', 'sickle', 'spear', 'warhammer']
materials = ['wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite',
             'copper', 'silver', 'soul_steel', 'titanium', 'andonized_titanium', 'iridium', 'mithril']

# Function to create files
def create_tool_files():
    for i in range(len(materials)):
        for j in range(len(tool_types)):
            mat = materials[i]
            ttyp = tool_types[j]
            # Create json obj to make interpolation easier
            filename = f'{mat}_{ttyp}.json'
            json_obj = {
                "parent": f"odyssey:item/weapons/bases/{ttyp}",
                "textures": {
                    "0": f"odyssey:item/weapons/{ttyp}_texture_{mat}",
                    "particle": f"odyssey:item/weapons/{ttyp}_texture_{mat}"
                }
            }
            #text = f'{"parent": "odyssey:item/weapons/bases/{ttyp}", "textures": {"0": "odyssey:item/weapons/longaxe_texture_diamond", "particle": "odyssey:item/weapons/longaxe_texture_diamond"}}'
            text = json.dumps(json_obj)
            # Write the text to opened file
            with open(filename, 'w') as file:
                file.write(text)
            
# Prompt 
print("Confirm Creation of New files? This will overwrite old files.")
print(f"Will Create {len(tool_types) * len(materials)} tool combinations.")
print("Proceed (y/n) . . .")
answer = input()

# Input
if answer == "y":
    print("Ok")
    create_tool_files() 