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

FILE_OBJS = {}

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


# Seperate write function to 
def write_to_global_obj(mat: str, ttyp: str, trim: str, i: int):
    global FILE_OBJS
    filename = f'{mat}_{ttyp}'
    file_obj = get_or_create_file_obj(filename)
    # Create override to add
    override_obj = {
        "model": f"minecraft:item/iron_chestplate_quartz_trim",
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