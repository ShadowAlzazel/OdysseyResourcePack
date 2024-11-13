import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

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
    "mithril_ingot",
    "neptunian",
    "ruby",
    "silver_ingot",
    "silver_nugget",
    "soul_quartz",
    "soul_steel_ingot",
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

RUNIC = [
    "clay_dowel",
    "clay_key",
    "clay_skull",
    "clay_totem",
    "clay_orb",
    "clay_rods",
    "glazed_runic_dowel",
    "glazed_runic_key",
    "glazed_runic_skull",
    "glazed_runic_totem",
    "glazed_runic_orb",
    "glazed_runic_rods",
]

OTHER = [
    "ancient_tablet",
    "arcane_armor_trim_smithing_template",
    "blazing_rocket",
    "danger_armor_trim_smithing_template",
    "explosive_arrow",
    "imperial_armor_trim_smithing_template",
    "iridium_upgrade_template",
    "irradiated_fruit"
]

ARCANE = [
    "arcane_book",
    "blank_tome",
    "gilded_book",
    "tome_of_avarice",
    "tome_of_banishment",
    "tome_of_discharge",
    "tome_of_embrace",
    "tome_of_euphony",
    "tome_of_expenditure",
    "tome_of_extraction",
    "tome_of_harmony",
    "tome_of_imitation",
    "tome_of_infusion",
    "tome_of_polymerization",
    "tome_of_promotion",
    "tome_of_replication",
]

ITEM_LIST = OTHER + RUNIC + MATERIALS + FOODS + ARCANE 

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# Generate files for list
def generate_files(item_list: list, category: str):
    for item_name in item_list:
        filename = f'{item_name}.json'
        # create json obj
        json_obj = {
            "model": {
                "type": "minecraft:model",
                "model": f'odyssey:item/generic/{item_name}'
            }     
        }
        # Write the text to opened file
        text = json.dumps(json_obj, indent=2)
        with open(filename, 'w') as file:
            file.write(text)


# poulate files
def populate_files():
    # Generate files for all basic item categories
    #item_categories = {
    #    "materials": MATERIALS,
    #    "foods": FOODS,
    #    "other": OTHER
    #}
    #for category, item_list in item_categories.items():
    #    generate_files(item_list, category)
    item_list = ITEM_LIST
    generate_files(item_list, "generic")    

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