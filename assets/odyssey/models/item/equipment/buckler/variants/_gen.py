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


def create_model_json(parent_path: str, texture_path: str) -> dict:
    """Returns the JSON dictionary structure for a buckler model."""
    return {
        "parent": parent_path,
        "textures": {"0": texture_path, "particle": texture_path},
    }


def generate_buckler_models():
    for mat in MATERIALS:
        texture_key = f"odyssey:item/equipment/buckler/texture_{mat}"

        # 1. Base / Standard Model
        base_model = create_model_json(
            parent_path="odyssey:item/equipment/buckler/base",
            texture_path=texture_key,
        )
        base_filename = os.path.join(OUTPUT_DIR, f"{mat}.json")

        with open(base_filename, "w", encoding="utf-8") as f:
            json.dump(base_model, f, indent=2)

        # 2. Blocking Model
        blocking_model = create_model_json(
            parent_path="odyssey:item/equipment/buckler/base_blocking",
            texture_path=texture_key,
        )
        blocking_filename = os.path.join(OUTPUT_DIR, f"{mat}_blocking.json")

        with open(blocking_filename, "w", encoding="utf-8") as f:
            json.dump(blocking_model, f, indent=2)

        print(f"Generated: {mat}.json and {mat}_blocking.json")

    print(f"\nDone! Generated {len(MATERIALS) * 2} files in '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    generate_buckler_models()