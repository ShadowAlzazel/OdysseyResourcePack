import json
import os

# Set output directory directly to the script's folder
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# List of all buckler materials
MATERIALS = [
    "wooden",
    "golden",
    "iron",
    "diamond",
    "netherite",
    "copper",
    "silver",
    "soul_steel",
    "titanium",
    "anodized_titanium",
    "iridium",
    "mithril",
    "crystal_alloy",
]


def create_item_model_json(material: str) -> dict:
    """Returns the JSON structure for a conditional buckler item definition."""
    return {
        "model": {
            "type": "minecraft:condition",
            "on_false": {
                "type": "minecraft:model",
                "model": f"odyssey:item/equipment/buckler/variants/{material}",
            },
            "on_true": {
                "type": "minecraft:model",
                "model": f"odyssey:item/equipment/buckler/variants/{material}_blocking",
            },
            "property": "minecraft:using_item",
        }
    }


def generate_item_models():
    for mat in MATERIALS:
        item_model = create_item_model_json(mat)
        filename = os.path.join(OUTPUT_DIR, f"{mat}_buckler.json")

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(item_model, f, indent=2)

        print(f"Generated: {mat}_buckler.json")

    print(
        f"\nDone! Generated {len(MATERIALS)} item model files in '{OUTPUT_DIR}'."
    )


if __name__ == "__main__":
    generate_item_models()