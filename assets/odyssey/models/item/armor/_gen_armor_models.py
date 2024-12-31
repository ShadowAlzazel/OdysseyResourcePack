import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    
# The four basic armor slots
ARMOR_MODELS = [
    'chestplate', 'leggings', 'boots', 'helmet'
]

# The available materials for armor
VANILLA_ARMOR_MATERIALS = [
    'leather', 'golden', 'chainmail', 'iron', 'diamond', 'netherite'
]
ODYSSEY_ARMOR_MATERIALS = [
    'mithril', 'iridium', 'soul_steel', 'titanium', 'anodized_titanium',
    'copper', 'silver', 'crystal_alloy'
]

# The trim materials
ODYSSEY_TRIMS = [
    'alexandrite',
    'anodized_titanium',
    'iridium',
    'jade', 
    'jovianite',
    'kunzite', 
    'mithril', 
    'neptunian',
    'obsidian', 
    'ruby',
    'silver', 
    'soul_quartz',
    'soul_steel', 
    'titanium',
    'crystal_alloy'
]
VANILLA_TRIMS = [
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

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
                
def create_base_armor_model(material: str, base: str):
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


def create_armor_trim(material: str, base: str, trim_name: str, namespace: str):
    filename = f'{material}_{base}_{trim_name}_trim.json'
    trim_id = trim_name
    # Vars
    has_overlay = material == "leather"
    if trim_name == material:
        trim_id = f"{trim_name}_darker"
    # Create layer0
    if namespace == "odyssey":
        layer0 = f"{namespace}:item/armor/{material}_{base}"
    else:
        layer0 = f"minecraft:item/{material}_{base}"
    # Create json_obj
    json_obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": layer0,
            "layer1": f'minecraft:trims/items/{base}_trim_{trim_id}',
        }
    }
    # Overlay
    if has_overlay:
        json_obj["textures"]["layer1"] = f'{layer0}_overlay'
        json_obj["textures"]["layer2"] = f'minecraft:trims/items/{base}_trim_{trim_id}'
    
    # Write the text to opened file
    text = json.dumps(json_obj, indent=2)
    with open(filename, 'w') as file:
        file.write(text)


# Function to create files
def populate_files():
    all_trims = ODYSSEY_TRIMS + VANILLA_TRIMS
    for model in ARMOR_MODELS:
        #  Loop through all odyssey armor to create all trim models and base models
        for odyssey_material in ODYSSEY_ARMOR_MATERIALS:
            # Base armor model (no trim)
            create_base_armor_model(odyssey_material, model)
            # Armor trim file
            namespace = "odyssey"
            for trim in all_trims:
                create_armor_trim(odyssey_material, model, trim, namespace)
        # Loop through all vanilla armor to create odyssey trim models
        for vanilla_material in VANILLA_ARMOR_MATERIALS:
            namespace = "minecraft"
            for trim in ODYSSEY_TRIMS:
                create_armor_trim(vanilla_material, model, trim, namespace)
            

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