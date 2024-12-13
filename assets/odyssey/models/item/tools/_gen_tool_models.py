import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# Master File for ALL TOOLS
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

TOOL_TYPES = [
    "sword",
    "pickaxe",
    "axe", 
    "shovel", 
    "hoe"
]

MATERIALS = [
    "copper",
    "silver",
    "soul_steel",
    "titanium", 
    "anodized_titanium",
    "iridium",
    "mithril"
]

# Function to create files
def create_tool_files():
    for tool in TOOL_TYPES:
        # Create dir if missing 
        if not os.path.exists(tool):
            os.makedirs(tool)
        # Loop per material
        for material in MATERIALS:
            # Create json obj to make interpolation easier
            filename = f'{tool}/{material}_{tool}.json'
            # Differnt format for block bench models and base textures
            json_obj = {
                "parent": f"odyssey:item/tools/{tool}/_base",
                "textures": {
                    "layer0": f"odyssey:item/tool/{tool}_{material}"
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
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_tool_files() 
        
# Main
if __name__ == "__main__":
    main()