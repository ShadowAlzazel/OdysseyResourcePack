# item_data.py
"""
Central list of item names used by generate_assets.py.

There are two "targets" this data feeds:

  ITEM_DEFINITIONS -> data/<namespace>/items/<item>.json
                       (the item model *definition*, referenced by the
                       minecraft:item_model component on the actual item,
                       e.g. "minecraft:item_model": "odyssey:alaska_blackfish")

  ITEM_MODELS       -> assets/<namespace>/models/item/<category>/<item>.json
                       (the classic parent/texture model file)

Both are organized as {category: [item names]}. The category controls the
model path written inside each generated file:
"odyssey:item/<category>/<item>". That string has to match wherever the
actual model file physically lives, so if an item appears in both
ITEM_DEFINITIONS and ITEM_MODELS, give it the same category in both places
-- generate_assets.py's verify() step will flag it if you don't.

Edit item names here -- generate_assets.py only reads from this file, so
there's a single place to add/remove/rename an item instead of editing two
scripts.
"""

# ---------------------------------------------------------------------------
# ITEM DEFINITIONS  (data/<namespace>/items/<item>.json)
# ---------------------------------------------------------------------------
ITEM_DEFINITIONS = {
    "arcane": [
        "amplify_rune", "ball_rune", "beam_rune", "bolt_rune", "break_rune",
        "convergence_rune", "differ_rune", "direct_rune", "heal_rune",
        "kernel_rune", "missile_rune", "nearby_rune", "next_rune",
        "origin_rune", "pick_up_rune", "point_rune", "self_rune",
        "size_rune", "slice_rune", "swap_rune", "teleport_rune",
        "trace_rune", "wall_rune", "zone_rune",
    ],
    "generic": [
        # Ingredients
        "spell_scroll", "arcane_book", "alexandrite", "anodized_titanium_ingot",
        "coagulated_blood", "ectoplasm", "heated_titanium_ingot", "iridium_ingot",
        "irradiated_rod", "irradiated_shard", "jade", "jovianite", "kunzite",
        "mithril_ingot", "neptunian", "ruby", "silver_ingot", "silver_nugget",
        "soul_quartz", "soul_steel_ingot", "titanium_ingot", "warden_entrails",
        "crystal_alloy_ingot",
        # Misc
        "ancient_tablet", "blazing_rocket", "explosive_arrow", "irradiated_fruit",
        "shadow_trial_key", "crystalline_potion",
        # Smithing
        "imperial_armor_trim_smithing_template", "voyager_armor_trim_smithing_template",
        "leaf_armor_trim_smithing_template", "danger_armor_trim_smithing_template",
        "ring_armor_trim_smithing_template", "cross_weapon_trim_smithing_template",
        "spine_weapon_trim_smithing_template", "wings_weapon_trim_smithing_template",
        "trace_weapon_trim_smithing_template", "jewel_weapon_trim_smithing_template",
        "iridium_upgrade_template", "mithril_upgrade_template", "soul_steel_upgrade_template",
        "titanium_upgrade_template", "blade_part_upgrade_template", "handle_part_upgrade_template",
        "pommel_part_upgrade_template", "hilt_part_upgrade_template", "empty_part_upgrade_template",
        "crystal_alloy_upgrade_template", "voyager_part_pattern", "danger_part_pattern",
        "seraph_part_pattern", "marauder_part_pattern", "crusader_part_pattern",
        "vandal_part_pattern", "imperial_part_pattern", "fancy_part_pattern",
        "humble_part_pattern", "empty_part_pattern", "mastercrafted_tool_template",
        # Enchanting
        "blank_tome", "gilded_book", "tome_of_avarice", "tome_of_banishment",
        "tome_of_discharge", "tome_of_embrace", "tome_of_euphony", "tome_of_expenditure",
        "tome_of_extraction", "tome_of_harmony", "tome_of_imitation", "tome_of_infusion",
        "tome_of_polymerization", "tome_of_promotion", "tome_of_replication",
        # Glyphic
        "clay_dowel", "clay_key", "clay_skull", "clay_totem", "clay_orb", "clay_rods",
        "glazed_dowel", "glazed_key", "glazed_skull", "glazed_totem", "glazed_orb", "glazed_rods",
        # Food
        "allium_jade_boba_tea", "bacon", "berry_tart", "brisket", "chocolate_mochi",
        "coffee", "cooked_brisket", "cornflower_ceylon_boba_tea", "crystal_candy",
        "dog_milk_bone", "dog_sizzle_crisp", "dog_spinach", "earl_lily_boba_tea",
        "fish_n_chips", "french_toast", "fruit_bowl", "green_apple", "matcha_melon_boba_tea",
        "oolong_orchid_boba_tea", "salmon_nigiri", "salmon_roll", "shoyu_ramen",
        "spider_eye_boba", "thai_tulip_boba_tea",
    ],
    "fish": [
        "anchovy",
        "arapaima",
        "armoured_catfish",
        "axolotl",
        "bass",
        "black_seabass",
        "blind_cave_fish",
        "blind_minnow",
        "bluegill",
        "bujurqui",
        "carp",
        "catfish",
        #"cod",
        "crappie",
        "echo_fish",
        "european_eel",
        "flounder",
        "flying_fish",
        "freshwater_pufferfish",
        "gar",
        "guppy",
        "gurnard",
        "herring",
        "humpback_whitefish",
        "lamprey",
        "mahi_mahi",
        "mediterranean_killifish",
        "monkfish",
        "muskellunge",
        "northern_pike",
        "oarfish",
        "opah",
        "painted_moray",
        "pale_fish",
        "piranha",
        #"pufferfish",
        "rainbow_wrasse",
        "salmon",
        "shad",
        "siberian_sturgeon",
        "skate",
        "spoonhead_sculpin",
        "striped_perch",
        "sturgeon",
        "swordfish",
        #"tropical_fish",
        "tunisian_barb",
        "walleye",
        "wolffish",
    ]
}

# ---------------------------------------------------------------------------
# ITEM MODELS  (assets/<namespace>/models/item/<category>/<item>.json)
# ---------------------------------------------------------------------------
ITEM_MODELS = {
    "generic": [
        # Ingredients
        "arcane_book", "spell_scroll", "arcane_pen", "alexandrite", "anodized_titanium_ingot",
        "coagulated_blood", "ectoplasm", "heated_titanium_ingot", "iridium_ingot",
        "irradiated_rod", "irradiated_shard", "jade", "jovianite", "kunzite",
        "mithril_ingot", "neptunian", "ruby", "silver_ingot", "silver_nugget",
        "soul_quartz", "soul_steel_ingot", "titanium_ingot", "warden_entrails",
        "crystal_alloy_ingot",
        # Misc
        "ancient_tablet", "blazing_rocket", "explosive_arrow", "irradiated_fruit",
        "shadow_trial_key", "crystalline_potion", "scroll_open", "scroll_closed",
        # Smithing
        "imperial_armor_trim_smithing_template", "voyager_armor_trim_smithing_template",
        "leaf_armor_trim_smithing_template", "danger_armor_trim_smithing_template",
        "ring_armor_trim_smithing_template", "cross_weapon_trim_smithing_template",
        "spine_weapon_trim_smithing_template", "wings_weapon_trim_smithing_template",
        "trace_weapon_trim_smithing_template", "jewel_weapon_trim_smithing_template",
        "iridium_upgrade_template", "mithril_upgrade_template", "soul_steel_upgrade_template",
        "titanium_upgrade_template", "blade_part_upgrade_template", "handle_part_upgrade_template",
        "pommel_part_upgrade_template", "hilt_part_upgrade_template", "empty_part_upgrade_template",
        "crystal_alloy_upgrade_template", "voyager_part_pattern", "danger_part_pattern",
        "seraph_part_pattern", "marauder_part_pattern", "crusader_part_pattern",
        "vandal_part_pattern", "imperial_part_pattern", "fancy_part_pattern",
        "humble_part_pattern", "empty_part_pattern", "mastercrafted_tool_template",
        # Enchanting
        "blank_tome", "gilded_book", "tome_of_avarice", "tome_of_banishment",
        "tome_of_discharge", "tome_of_embrace", "tome_of_euphony", "tome_of_expenditure",
        "tome_of_extraction", "tome_of_harmony", "tome_of_imitation", "tome_of_infusion",
        "tome_of_polymerization", "tome_of_promotion", "tome_of_replication",
        # Glyphic
        "clay_dowel", "clay_key", "clay_skull", "clay_totem", "clay_orb", "clay_rods",
        "glazed_dowel", "glazed_key", "glazed_skull", "glazed_totem", "glazed_orb", "glazed_rods",
        # Food
        "allium_jade_boba_tea", "bacon", "berry_tart", "brisket", "chocolate_mochi",
        "coffee", "cooked_brisket", "cornflower_ceylon_boba_tea", "crystal_candy",
        "dog_milk_bone", "dog_sizzle_crisp", "dog_spinach", "earl_lily_boba_tea",
        "fish_n_chips", "french_toast", "fruit_bowl", "green_apple", "matcha_melon_boba_tea",
        "oolong_orchid_boba_tea", "salmon_nigiri", "salmon_roll", "shoyu_ramen",
        "spider_eye_boba", "thai_tulip_boba_tea",
    ],
    
    "fish": [
        "anchovy",
        "arapaima",
        "armoured_catfish",
        "axolotl",
        "bass",
        "black_seabass",
        "blind_cave_fish",
        "blind_minnow",
        "bluegill",
        "bujurqui",
        "carp",
        "catfish",
        #"cod",
        "crappie",
        "echo_fish",
        "european_eel",
        "flounder",
        "flying_fish",
        "freshwater_pufferfish",
        "gar",
        "guppy",
        "gurnard",
        "herring",
        "humpback_whitefish",
        "lamprey",
        "mahi_mahi",
        "mediterranean_killifish",
        "monkfish",
        "muskellunge",
        "northern_pike",
        "oarfish",
        "opah",
        "painted_moray",
        "pale_fish",
        "piranha",
        #"pufferfish",
        "rainbow_wrasse",
        "salmon",
        "shad",
        "siberian_sturgeon",
        "skate",
        "spoonhead_sculpin",
        "striped_perch",
        "sturgeon",
        "swordfish",
        #"tropical_fish",
        "tunisian_barb",
        "walleye",
        "wolffish",
    ]
}

# ---------------------------------------------------------------------------
# NOT WIRED UP YET -- kept here for reference. These need generation logic
# different from the simple "one flat model per item" template the two
# functions above use, so they're intentionally left out of
# ITEM_DEFINITIONS / ITEM_MODELS for now.
# ---------------------------------------------------------------------------

# "scroll" appears to have evolved into two states (see scroll_open /
# scroll_closed in ITEM_MODELS["generic"]). Probably needs a custom
# definition (e.g. a minecraft:select on some state/component) rather than
# a single flat model.
COMPOSITE_ITEMS = [
    "scroll",
]

# Marked "DO NOT USE" in the original script -- likely custom full 3D
# models rather than a simple parent/texture model.
MODELED_WEAPONS = [
    "abzu_blade", "shogun_lightning", "excalibur", "frost_fang", "elucidator",
    "knight_breaker", "the_dragon_slayer",
]