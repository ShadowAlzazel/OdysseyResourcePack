import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# The four basic armor slots
armor_bases = [
    'chestplate', 'leggings', 'boots', 'helmet'
]

# The available materials for armor
minecraft_armor_materials = [
    'leather', 'golden', 'chainmail', 'iron', 'diamond', 'netherite'
]
odyssey_armor_materials = [
    'mithril', 'iridium', 'soul_steel', 'titanium', 'anodized_titanium',
    'copper', 'silver'
]
# The trim materials
odyssey_trims = [
    'alexandrite',
    'anodizedtitanium',
    'iridium',
    'jade', 
    'jovianite',
    'kunzite', 
    'mithril', 
    'neptunian',
    'obsidian', 
    'ruby',
    'silver', 
    'soulquartz',
    'soulsteel', 
    'titanium'
]
minecraft_trims = [
    "quartz",
    "iron",
    "netherite",
    "redstone",
    "copper",
    "gold",
    "emerald",
    "diamond",
    "lapis",
    "amethyst",
    "resin"
]

# Function to create files
def create_armor_trim_files():
    # Loop through all vanilla armor to create custom trim items
    for i in range(len(minecraft_armor_materials)):
        for j in range(len(armor_bases)):
            for k in range(len(odyssey_trims)):
                mat = minecraft_armor_materials[i]
                base = armor_bases[j]
                trim = odyssey_trims[k]
                key = "minecraft"
                write_armor_trim_file(mat, base, trim, key)
    # Loop through all odyssey armor to create trims
    all_trims = odyssey_trims + minecraft_trims
    for i in range(len(odyssey_armor_materials)):
        for j in range(len(armor_bases)):
            for k in range(len(all_trims)):
                mat = odyssey_armor_materials[i]
                base = armor_bases[j]
                trim = all_trims[k]
                key = "odyssey"
                write_armor_trim_file(mat, base, trim, key)
    # Create base model files
    for i in range(len(odyssey_armor_materials)):
        for j in range(len(armor_bases)):
            mat = odyssey_armor_materials[i]
            base = armor_bases[j]
            write_base_trim_file(mat, base)
                
def write_base_trim_file(material: str, base: str):
    filename = f'{material}_{base}.json'
     # Create json_obj
    json_obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f'odyssey:item/armor/{material}_{base}',
        }
    }
    text = json.dumps(json_obj, indent=2)
    # Write the text to opened file
    with open(filename, 'w') as file:
        file.write(text)

def write_armor_trim_file(material: str, base: str, trim_name: str, key: str):
    filename = f'{material}_{base}_{trim_name}_trim.json'
    trim_id = trim_name
    # Create Darker
    if trim_name == material:
        trim_id = f"{trim_name}_darker"
    # Create layer0
    if key == "odyssey":
        layer0 = f"{key}:item/armor/{material}_{base}"
    else:
        layer0 = f"minecraft:item/{material}_{base}"
    # Create json_obj
    json_obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": layer0,
            "layer1": f"minecraft:trims/items/{base}_trim_{trim_id}",
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
        create_armor_trim_files() 
        
# Main
if __name__ == "__main__":
    main()