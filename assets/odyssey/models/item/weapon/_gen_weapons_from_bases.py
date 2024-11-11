import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

weapon_types = [
    'chakram', 'claymore', 'cutlass', 'dagger', 'halberd', 'katana', 'kunai', 'lance', 
    'longaxe', 'longsword', 'rapier', 'saber', 'scythe', 'sickle', 'spear', 'warhammer',
    'poleaxe', 'shuriken', 'glaive', 'battlesaw', 'arm_blade', 'zweihander']
materials = [
    'wooden', 'golden', 'stone', 'iron', 'diamond', 'netherite',
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril']

other_tools = ['shuriken']

# Function to create files
def create_tool_files():
    for i in range(len(materials)):
        for j in range(len(weapon_types)):
            material = materials[i]
            weapon_type = weapon_types[j]
            # Create json obj to make interpolation easier
            filename = f'{material}_{weapon_type}.json'
            # Differnt format for block bench models and base textures
            if weapon_type in other_tools:
                json_obj = {
                "parent": f"odyssey:item/weapon/bases/{weapon_type}",
                "textures": {
                    "layer0": f"odyssey:item/weapon/{weapon_type}_base_{material}",
                    }
                }
            else:
                json_obj = {
                    "parent": f"odyssey:item/weapon/bases/{weapon_type}",
                    "textures": {
                        "0": f"odyssey:item/weapon/{weapon_type}_texture_{material}",
                        "particle": f"odyssey:item/weapon/{weapon_type}_texture_{material}"
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
    print(f"Will Create {len(weapon_types) * len(materials)} tool combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_tool_files() 
        
# Main
if __name__ == "__main__":
    main()