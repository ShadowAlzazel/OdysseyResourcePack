import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

armor_materials = [
    'mithril', 'iridium', 'soul_steel', 'titanium', 'anodized_titanium',
    'copper', 'silver'
]
armor_bases = [
    'chestplate', 'leggings', 'boots', 'helmet'
]
trim_value_map = {
    'alexandrite': 0.0001,
    'anodizedtitanium': 0.0002, 
    'iridium': 0.0003,
    'jade': 0.0004, 
    'jovianemerald': 0.0005,
    'kunzite': 0.0006, 
    'mithril': 0.0007, 
    'neptuniandiamond': 0.0008,
    'obsidian': 0.0009, 
    'ruby': 0.0010,
    'silver': 0.0011, 
    'soulquartz': 0.0012,
    'soulsteel': 0.0013, 
    'titanium': 0.0014,
    
    "quartz": 0.1,
    "iron": 0.2,
    "netherite": 0.3,
    "redstone": 0.4,
    "copper": 0.5,
    "gold": 0.6,
    "emerald": 0.7,
    "diamond": 0.8,
    "lapis": 0.9,
    "amethyst": 1.0,
}
minecraft_trims = [
    "quartz", "iron", "netherite", "redstone", "copper",
    "gold", "emerald", "diamond", "lapis", "amethyst"
]

FILE_OBJS = {}

# To Create Parent object file header
def create_parent_file_obj(filename: str, has_overlay: bool=False):
    parent_obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"odyssey:item/armor/{filename}"
        },
        "overrides": []
    } 
    if has_overlay:
        parent_obj['textures']['layer1'] = f"minecraft:item/{filename}_overlay"
       
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

# Function to create files
def create_armor_files():
    for name, value in trim_value_map.items():
        for j in range(len(armor_materials)):
            for k in range(len(armor_bases)):
                mat = armor_materials[j]
                base = armor_bases[k]
                write_to_global_obj(mat, base, name, value)
    # -----------------------------------------------------------------------    
    # Add All file obj after loop to now overwrite previous 
    for file_key in FILE_OBJS:
        print(file_key)
        text = json.dumps(FILE_OBJS[file_key], indent=2)
        filename = f"{file_key}.json"
        with open(filename, 'w') as file:
            file.write(text)
    print(f"Overwrote {len(FILE_OBJS)} files.")


# Seperate write function to 
def write_to_global_obj(material: str, base: str, trim_name: str, trim_value: int):
    global FILE_OBJS
    filename = f'{material}_{base}'
    has_overlay = material == "leather"
    file_obj = get_or_create_file_obj(filename, has_overlay)
    trim = trim_name
    # Check for darker
    gold_on_gold = material == "golden" and t == "gold"
    if (trim_name == material or gold_on_gold):
        trim = f'{trim_name}_darker'
    # Create trim predicate model
    #if (trim_name in minecraft_trims):
    #    model = f"minecraft:item/{material}_{base}_{trim}_trim"
    #else:
    #    model = f"odyssey:item/armor_trims/{material}_{base}_{trim}_trim"
    model = f"odyssey:item/armor_trims/{material}_{base}_{trim}_trim"
    # Write to found file    
    override_obj = {
        "model": model,
        "predicate": {
            "trim_type": trim_value
        }
    }        
    # Add override to "overrides list"
    file_obj["overrides"].append(override_obj)           
        
# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    #print(f"Will Create {len(tool_types) * len(materials)} tool combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_armor_files() 
        
# Main
if __name__ == "__main__":
    main()