import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

SIGILS = [
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

SIGIL_MATERIALS = [
    "diamond",
    "silver"
    #"arcane",
    #"gold",
    #"mithril"
]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

def generate_sigil_file(sigil: str, material: str):
    filename = f'{sigil}_sigil_{material}.json'
    # Create an obj using the dictionary
    json_obj = {
        "parent": f"minecraft:item/generated",
        "textures": {
            "layer0": f'odyssey:item/runic/sigils/{sigil}_sigil_{material}'
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
            "layer0": f'odyssey:item/runic/tablets/{tablet}_tablet'
        }
    }
    # Convert
    text = json.dumps(json_obj, indent=2)
    # Write the text to opened file
    with open(filename, 'w') as file:
        file.write(text)

# Function to create files
def populate_files():
    for sigil in SIGILS:
        for material in SIGIL_MATERIALS:
            generate_sigil_file(sigil, material)
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