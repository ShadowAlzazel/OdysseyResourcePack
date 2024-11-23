import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

GLYPHS = [
    "assault", 
    "break",
    "feather", 
    "finesse", 
    "force", 
    "gravity", 
    "guard", 
    "grasp", 
    "jump", 
    "range",
    "size",
    "steadfast",
    "swift", 
    "vitality",
    "unknown"
]

TABLETS = [
    "brick",
    "clay",
    "tuff",
    "nether_brick",
    "deepslate"
]

GLYPH_MATERIALS = [
    "diamond",
    "silver"
    #"arcane",
    #"gold",
    #"mithril"
]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

def generate_glyph_file(glyph: str, material: str):
    filename = f'{glyph}_glyph_{material}.json'
    # Create an obj using the dictionary
    json_obj = {
        "parent": f"minecraft:item/generated",
        "textures": {
            "layer0": f'odyssey:item/glyphs/{glyph}_glyph_{material}'
        }
    }
    # Convert
    text = json.dumps(json_obj, indent=2)
    # Write the text to opened file
    with open(filename, 'w') as file:
        file.write(text)


def generate_tablet_file(tablet: str):
    filename = f'{tablet}_tablet.json'
    # Create an obj using the dictionary
    json_obj = {
        "parent": f"minecraft:item/generated",
        "textures": {
            "layer0": f'odyssey:item/glyphs/{tablet}_tablet'
        }
    }
    # Convert
    text = json.dumps(json_obj, indent=2)
    # Write the text to opened file
    with open(filename, 'w') as file:
        file.write(text)

# Function to create files
def populate_files():
    for glyph in GLYPHS:
        for material in GLYPH_MATERIALS:
            generate_glyph_file(glyph, material)
    for tablet in TABLETS:
        generate_tablet_file(tablet)
            
       
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