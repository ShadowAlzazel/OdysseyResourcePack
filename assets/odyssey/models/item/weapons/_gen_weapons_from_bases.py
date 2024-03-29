import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# TODO model texturing
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
            # Write the text to opened file
            with open(filename, 'w') as file:
                file.write(text)
        
        
# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print(f"Will Create {len(tool_types) * len(materials)} tool combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_tool_files() 
        
# Main
if __name__ == "__main__":
    main()