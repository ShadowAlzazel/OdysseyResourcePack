import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

tool_types = [
    'sword', 'pickaxe', 'axe', 'shovel', 'hoe']
materials = [
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril']

# Function to create files
def create_tool_files():
    for i in range(len(materials)):
        for j in range(len(tool_types)):
            material = materials[i]
            tool_type = tool_types[j]
            # Create json obj to make interpolation easier
            filename = f'{material}_{tool_type}.json'
            # Differnt format for block bench models and base textures
            json_obj = {
                "parent": f"odyssey:item/tool/bases/{tool_type}",
                "textures": {
                    "layer0": f"odyssey:item/tool/base_{tool_type}_{material}"
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