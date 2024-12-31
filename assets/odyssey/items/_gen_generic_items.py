import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

ITEMS = [
    # Ingredients
    "arcane_book",
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
    "warden_entrails",
    "crystal_alloy_ingot",
    # Misc
    "ancient_tablet",
    "blazing_rocket",
    "explosive_arrow",
    "irradiated_fruit",
    "shadow_trial_key",
    "crystalline_potion",
    # Smithing
    "imperial_armor_trim_smithing_template",
    "voyager_armor_trim_smithing_template",
    "leaf_armor_trim_smithing_template",
    "danger_armor_trim_smithing_template",
    "ring_armor_trim_smithing_template",
    "cross_weapon_trim_smithing_template",
    "spine_weapon_trim_smithing_template",
    "wings_weapon_trim_smithing_template",
    "trace_weapon_trim_smithing_template",
    "jewel_weapon_trim_smithing_template",
    "iridium_upgrade_template",
    "mithril_upgrade_template",
    "soul_steel_upgrade_template",
    "titanium_upgrade_template",
    "blade_part_upgrade_template",
    "handle_part_upgrade_template",
    "pommel_part_upgrade_template",
    "hilt_part_upgrade_template",
    "empty_part_upgrade_template",
    "crystal_alloy_upgrade_template",
    "voyager_part_pattern",
    "danger_part_pattern",
    "seraph_part_pattern",
    "marauder_part_pattern",
    "crusader_part_pattern",
    "vandal_part_pattern",
    "imperial_part_pattern",
    "fancy_part_pattern",
    "humble_part_pattern",
    "empty_part_pattern",
    "mastercrafted_tool_template",
    # Enchanting 
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
    # Glyphic
    "clay_dowel",
    "clay_key",
    "clay_skull",
    "clay_totem",
    "clay_orb",
    "clay_rods",
    "glazed_dowel",
    "glazed_key",
    "glazed_skull",
    "glazed_totem",
    "glazed_orb",
    "glazed_rods",
    # Food
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

COMPOSITE_ITEMS = [
    "scroll"
]

# DO NOT USE
MODELED_WEAPONS = [
    "abzu_blade",
    "shogun_lightning",
    "excalibur",
    "frost_fang",
    "elucidator",
    "knight_breaker",
    "the_dragon_slayer"
]

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
    generate_files(ITEMS, "generic")    

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