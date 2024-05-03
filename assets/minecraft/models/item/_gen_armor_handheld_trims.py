import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

armor_material = [
    'leather', 'golden', 'chainmail', 'iron', 'diamond', 'netherite']
armor_type = [
    'chestplate', 'leggings', 'boots', 'helmet'
]
trims = {
    'alexandrite': 0.5501,
    'andonizedtitanium': 0.5502, 
    'iridium': 0.5503,
    'jade': 0.5504, 
    'jovianemerald': 0.5505,
    'kunzite': 0.5506, 
    'mithril': 0.5507, 
    'neptuniandiamond': 0.5508,
    'obsidian': 0.5509, 
    'ruby': 0.5510,
    'silver': 0.5511, 
    'soulquartz': 0.5512,
    'soulsteel': 0.5513, 
    'titanium': 0.5514,
    
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
def create_armor_trim_files():
    for trim, i in trims.items():
        for j in range(len(armor_material)):
            for k in range(len(armor_type)):
                mat = armor_material[j]
                ttyp = armor_type[k]
                write_to_global_obj(mat, ttyp, trim, i)
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
def write_to_global_obj(mat: str, ttyp: str, t: str, i: int):
    global FILE_OBJS
    filename = f'{mat}_{ttyp}'
    file_obj = get_or_create_file_obj(filename)
    trim = t
    # Check if darker
    if (trim == mat):
        trim = f'{t}_darker'
    # Create override to add
    if (trim in minecraft_trims):
        model = f"minecraft:item/{mat}_{ttyp}_{trim}_trim",
    else:
        model = f"odyssey:item/armor_trims/{mat}_{ttyp}_{trim}_trim",
    # Write to found file    
    override_obj = {
        "model": model,
        "predicate": {
            "trim_type": i
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
        create_armor_trim_files() 
        
# Main
if __name__ == "__main__":
    main()