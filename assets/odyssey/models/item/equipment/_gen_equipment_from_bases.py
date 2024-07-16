import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# TODO model texturing
# [Battleaxe(labrys)]
# Rework [Rapier], [Lance]

equipment_types = [
    'sword', 'pickaxe', 'axe', 'shovel', 'hoe']
materials = [
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril']

other_tools = ['shuriken']

# Function to create files
def create_tool_files():
    for i in range(len(materials)):
        for j in range(len(equipment_types)):
            mat = materials[i]
            ttyp = equipment_types[j]
            # Create json obj to make interpolation easier
            filename = f'{mat}_{ttyp}.json'
            # Differnt format for block bench models and base textures
            json_obj = {
                "parent": f"odyssey:item/equipment/bases/{ttyp}",
                "textures": {
                    "layer0": f"odyssey:item/equipment/base_{ttyp}_{mat}"
                }
            }
            text = json.dumps(json_obj, indent=2)
            # Write the text to opened file
            with open(filename, 'w') as file:
                file.write(text)
        
        
# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print(f"Will Create {len(equipment_types) * len(materials)} tool combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_tool_files() 
        
# Main
if __name__ == "__main__":
    main()