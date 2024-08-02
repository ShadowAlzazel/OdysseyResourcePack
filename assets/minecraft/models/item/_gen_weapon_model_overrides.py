import os 
import json
from dataclasses import dataclass

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

@dataclass(frozen=True, order=True)
class Material: 
    name: str = 'material' 
    item_model_pre: int = 12345 # 'custom_model_data' component [12345XX]
    item_override_pre: str = 'stone' # for finding the item id
    
    
@dataclass(frozen=True, order=True)
class ToolType: 
    name: str = 'weapon'  
    item_model_suf: int = 67 # 'custom_model_data' compnent [XXXXX67]
    item_override_suf: str = 'sword' # for finding the item id
 
FILE_OBJS = {}
    
materials = [
    # Minecraft
    Material('wooden', 69051, 'wooden'),
    Material('golden', 69052, 'golden'),
    Material('stone', 69053, 'stone'),
    Material('copper', 69055, 'golden'), # Needs to be here cuz order matters
    Material('iron', 69057, 'iron'),
    Material('diamond', 69058, 'diamond'),
    Material('netherite', 69059, 'netherite'),
    # Odyssey
    Material('silver', 69063, 'iron'),
    Material('soul_steel', 69066, 'iron'),
    Material('titanium', 69068, 'iron'),
    Material('anodized_titanium', 69070, 'iron'),
    Material('iridium', 69071, 'iron'),
    Material('mithril', 69076, 'iron'),
]

tool_types = [
    # Other
    ToolType('shuriken', 1, 'iron_nugget'),
    # Vanilla Base
    ToolType('sword', 5, 'sword'),
    ToolType('pickaxe', 6, 'pickaxe'),
    ToolType('axe', 7, 'axe'),
    ToolType('shovel', 8, 'shovel'),
    ToolType('hoe', 9, 'hoe'),
    # Swords
    ToolType('katana', 44, 'sword'),
    ToolType('claymore', 45, 'sword'),
    ToolType('dagger', 46, 'sword'),
    ToolType('rapier', 47, 'sword'),
    ToolType('cutlass', 48, 'sword'),
    ToolType('saber', 49, 'sword'),
    ToolType('sickle', 50, 'sword'),
    ToolType('chakram', 51, 'sword'),
    ToolType('kunai', 52, 'sword'),
    ToolType('longsword', 53, 'sword'),
    ToolType('arm_blade', 54, 'sword'),
    # Shovels
    ToolType('spear', 74, 'shovel'),
    ToolType('halberd', 75, 'shovel'),
    ToolType('lance', 76, 'shovel'),
    # Axe
    ToolType('longaxe', 85, 'axe'),
    ToolType('poleaxe', 86, 'axe'),
    ToolType('glaive', 87, 'axe'),
    ToolType('battlesaw', 88, 'axe'),
    # Pickaxe
    ToolType('warhammer', 11, 'pickaxe'),
    # Hoe
    ToolType('scythe', 92, 'hoe')
]

other_tools = [
    'shuriken'
]

# To Create Parent object file header
def create_parent_file_obj(filename: str):
    parent_obj = {
        "parent": "minecraft:item/handheld",
        "textures": {
            "layer0": f"minecraft:item/{filename}"
        },
        "overrides": []
    }    
    return parent_obj

# Get parent file obg from global var or create new
def get_or_create_file_obj(filename: str):
    global FILE_OBJS
    if filename in FILE_OBJS.keys():
        return FILE_OBJS[filename]
    else:
        new_obj = create_parent_file_obj(filename)
        FILE_OBJS[filename] = new_obj        
        return FILE_OBJS[filename]

# Function to create files
def create_model_files():
    global FILE_OBJS
    # Loop over all to create in memory
    for i in range(len(materials)):
        for j in range(len(tool_types)):
            # Create variables for names
            mat: Material = materials[i]
            ttyp: ToolType = tool_types[j]
            item_name = f'{mat.name}_{ttyp.name}'
            # Get model and file to write in
            # -----------------------------------------------------------------------
            # Other tools
            if ttyp.name in other_tools:
                custom_model = (mat.item_model_pre * 100) + (ttyp.item_model_suf)
                filename = ttyp.item_override_suf
                file_obj = get_or_create_file_obj(filename)
            # Odyssey Tools
            else:
                custom_model = (mat.item_model_pre * 100) + (ttyp.item_model_suf)
                filename = f'{mat.item_override_pre}_{ttyp.item_override_suf}'
                # If base name matches file name skip as it is vanilla tool
                if item_name == filename:
                    continue
                file_obj = get_or_create_file_obj(filename)
            # -----------------------------------------------------------------------
            # Set Folder name space
            item_space = "weapons"
            if ttyp.name == ttyp.item_override_suf:
                item_space = "equipment"
            # Create override to add
            override_obj = {
                "model": f"odyssey:item/{item_space}/{item_name}",
                "predicate": {
                    "custom_model_data": custom_model
                }
            }
            # Add override to "overrides list"
            file_obj["overrides"].append(override_obj)
            #print(file_obj)
            #print(f"Loc: {hex(id(file_obj))}")
    # -----------------------------------------------------------------------                
    # Figure out how to add special textures here        
    # -----------------------------------------------------------------------        
    # Add All file obj after loop to now overwrite previous 
    for file_key in FILE_OBJS:
        text = json.dumps(FILE_OBJS[file_key], indent=2)
        #print(file_key)
        #print(text)
        filename = f"{file_key}.json"
        with open(filename, 'w') as file:
            file.write(text)
    print(f"Overwrote {len(FILE_OBJS)} files.")
    
# Main
def main():
    global FILE_OBJS
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print(f"Will Create {len(tool_types) * len(materials)} tool combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Running...")
        create_model_files() 
        print("Finished!")
                 
# Main
if __name__ == "__main__":
    main()