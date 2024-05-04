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
trims = [
    'alexandrite',
    'anodizedtitanium' ,
    'iridium',
    'jade', 
    'jovianemerald',
    'kunzite', 
    'mithril', 
    'neptuniandiamond',
    'obsidian', 
    'ruby',
    'silver', 
    'soulquartz',
    'soulsteel', 
    'titanium',
]

# Function to create files
def create_armor_trim_files():
    for i in range(len(armor_material)):
        for j in range(len(armor_type)):
            for k in range(len(trims)):
                mat = armor_material[i]
                atyp = armor_type[j]
                trim = trims[k]
                write_armor_trim_file(mat, atyp, trim)
                

def write_armor_trim_file(mat: str, atyp: str, trim: str):
    filename = f'{mat}_{atyp}_{trim}_trim.json'
    json_obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"minecraft:item/{mat}_{atyp}",
            "layer1": f"minecraft:trims/items/{atyp}_trim_{trim}",
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
    print(f"Will Create {len(armor_type) * len(armor_material) * len(trims)} armor trim files.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_armor_trim_files() 
        
# Main
if __name__ == "__main__":
    main()