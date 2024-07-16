import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

rune_blanks = [
    'runesherd', 'runepeice']
rune_materials = [
    'copper', 'silver', 'soul_steel', 'titanium', 'anodized_titanium', 'iridium', 'mithril']
rune_sigils = [
    'assault', 'break', 'feather', 'finesse', 
    'force', 'gravity', 'guard', 
    'grasp', 'jump', 'range', 'size',
    'steadfast', 'swift', 'vitality'
]

rune_types = {
    'runesherd': 'diamond',
    'runepeice': 'silver',
    'greater_runesherd': 'mithril'
}

# Function to create files
def create_files():
    for i in range(len(rune_sigils)):
        sigil = rune_sigils[i]
        # Loop through types
        for blank, material in rune_types.items():
            filename = f'{sigil}_{blank}.json'
            # Create an obj using the dictionary
            json_obj = {
                "parent": f"minecraft:item/generated",
                "textures": {
                    "layer0": f"odyssey:item/runic/blanks/blank_{blank}",
                    "layer1": f"odyssey:item/runic/sigils/{sigil}_sigil_{material}"
                }
            }
            # Convert
            text = json.dumps(json_obj, indent=2)
            # Write the text to opened file
            with open(filename, 'w') as file:
                file.write(text)
    
        
# Main
def main():
    # Prompt 
    print("Confirm Creation of New files? This will overwrite old files.")
    print(f"Will Create {len(rune_types) * len(rune_sigils)} rune combinations.")
    print("Proceed (y/n) . . .")
    answer = input()
    # Input
    if answer == "y":
        print("Ok")
        create_files() 
        
# Main
if __name__ == "__main__":
    main()