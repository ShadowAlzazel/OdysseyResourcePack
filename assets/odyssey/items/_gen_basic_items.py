import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

MATERIALS = [
    "alexandrite",
    "anodized_titanium_ingot",
    "coagulated_blood",
    "ectoplasm",
    "heated_titanium_ingot",
    "iridium_ingot",
    "irradiated_rod",
    "irradiated_shard",
    "jade",
    "jovianite",
    "kunzite",
    "neptunian",
    "ruby",
    "silver_ingot",
    "silver_nugget",
    "titanium_ingot",
    "warden_entrails"
]

FOODS = [
    "allium_jade_boba_tea",
    "bacon",
    "berry_tart",
    "brisket",
    "chocolate_mochi",
    "coffee",
    "cooked_brisket",
    "cornflower_ceylon_boba_tea",
    "crystal_candy",
    "dog_milk_bone",
    "dog_sizzle_crisp",
    "dog_spinach",
    "earl_lily_boba_tea",
    "fish_n_chips",
    "french_toast",
    "fruit_bowl",
    "green_apple",
    "matcha_melon_boba_tea",
    "oolong_orchid_boba_tea",
    "salmon_nigiri",
    "salmon_roll",
    "shoyu_ramen",
    "spider_eye_boba",
    "thai_tulip_boba_tea",
]

# Generate files for list
def generate_files(item_list: list, category: str):
    for item_name in item_list:
        filename = f'{item_name}.json'
        # create json obj
        json_obj = {
            "model": {
                "type": "minecraft:model",
                "model": f'odyssey:item/{category}/{item_name}'
            }     
        }
        # Write the text to opened file
        text = json.dumps(json_obj, indent=2)
        with open(filename, 'w') as file:
            file.write(text)


# poulate files
def populate_files():
    # Generate files for all basic item categories
    item_categories = {
        "materials": MATERIALS,
        "foods": FOODS
    }
    for category, item_list in item_categories.items():
        generate_files(item_list, category)
        

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