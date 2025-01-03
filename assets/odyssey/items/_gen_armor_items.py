import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Creating odyssey armor with trims
ODYSSEY_ARMOR_MATERIALS = [
    'mithril', 'iridium', 'soul_steel', 'titanium', 'anodized_titanium',
    'copper', 'silver', 'crystal_alloy'
]
ARMOR_MODELS = [
    'chestplate', 'leggings', 'boots', 'helmet'
]

#Name to namespace
MATERIAL_MAP = {
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
    'crystal_alloy': "odyssey",
    
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

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

FILE_OBJS = {}

# To Create Parent object file header
def create_parent_file_obj(filename: str, has_overlay: bool=False):
    parent_obj = {
        "model": {
            "type": "minecraft:select",
            "cases": [],
            "fallback": {
                "type":"minecraft:model",
                "model": f'odyssey:item/armor/{filename}'
            },
            "property": "minecraft:trim_material"
        }
    } 
    # Add leather dye tint
    if has_overlay:
        pass
    return parent_obj


# Get parent file obg from global var or create new
def get_or_create_file_obj(filename: str, has_overlay: bool=False):
    global FILE_OBJS
    if filename in FILE_OBJS.keys():
        return FILE_OBJS[filename]
    else:
        new_obj = create_parent_file_obj(filename, has_overlay)
        FILE_OBJS[filename] = new_obj        
        return FILE_OBJS[filename]


# Seperate write function to 
def write_to_global_obj(material: str, base: str, material_name: str, namespace: int):
    global FILE_OBJS
    filename = f'{material}_{base}'
    has_overlay = material == "leather"
    file_obj = get_or_create_file_obj(filename, has_overlay)
    # Check for darker
    #if (material_name == material or gold_on_gold):
    #    trim = f'{material_name}_darker'
    # Create model case obj 
    model_obj = {
        "model": {
            "type": "minecraft:model",
            "model": f'odyssey:item/armor/{material}_{base}_{material_name}_trim'
        },
        "when": f'{namespace}:{material_name}'
    }        
    # Add override to "cases list"
    file_obj["model"]["cases"].append(model_obj)           
  
      
# Function to populate files
def populate_files():
    for name, namespace in MATERIAL_MAP.items():
        for j in range(len(ODYSSEY_ARMOR_MATERIALS)):
            for k in range(len(ARMOR_MODELS)):
                mat = ODYSSEY_ARMOR_MATERIALS[j]
                base = ARMOR_MODELS[k]
                write_to_global_obj(mat, base, name, namespace)
    # -----------------------------------------------------------------------    
    # Add All file obj after loop to now overwrite previous 
    for file_key in FILE_OBJS:
        text = json.dumps(FILE_OBJS[file_key], indent=2)
        filename = f"{file_key}.json"
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
        populate_files() 
        
# Main
if __name__ == "__main__":
    main()