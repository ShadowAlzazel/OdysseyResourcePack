#!/usr/bin/env python3
"""
generate_assets.py

Generates two kinds of files, both sourced from item_data.py:

  1. Item definitions -> data/<namespace>/items/<item>.json
       {"model": {"type": "minecraft:model", "model": "odyssey:item/<category>/<item>"}}

  2. Item models       -> assets/<namespace>/models/item/<category>/<item>.json
       {"parent": "minecraft:item/generated", "textures": {"layer0": "odyssey:item/<category>/<item>"}}

The two outputs stay in two separate folders on purpose -- they're
different systems -- but since both are read from the same item_data.py,
running this script also checks them against each other (verify()) so
they can't silently drift apart the way OLD_ITEMS/ITEMS had.

CONFIG -- check/edit before running:
  - NAMESPACE
  - ITEM_DEFINITIONS_DIR / ITEM_MODELS_DIR
    These default to <this script's folder>/data/odyssey/items and
    .../assets/odyssey/models/item, matching a combined data+resource
    pack layout with this script sitting at the pack root. Point them at
    your real folders if that's not where things live.

USAGE
    python generate_assets.py
    Always prints a consistency report first. Then, if the GENERATE list
    near the bottom of main() isn't empty, asks for confirmation and
    writes those files.
"""

import json
from pathlib import Path

import item_data  # item_data.py must sit next to this script

NAMESPACE = "odyssey"

SCRIPT_DIR = Path(__file__).resolve().parent
ITEM_DEFINITIONS_DIR = SCRIPT_DIR / "data" / "odyssey" / "items"
ITEM_MODELS_DIR = SCRIPT_DIR / "assets" / "odyssey" / "models" / "item"


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def write_item_definition(out_dir: Path, category: str, item_name: str) -> Path:
    obj = {
        "model": {
            "type": "minecraft:model",
            "model": f"{NAMESPACE}:item/{category}/{item_name}",
        }
    }
    path = out_dir / f"{item_name}.json"
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    return path


def write_item_model(out_dir: Path, category: str, item_name: str) -> Path:
    obj = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"{NAMESPACE}:item/{category}/{item_name}",
        },
    }
    category_dir = out_dir / category
    category_dir.mkdir(parents=True, exist_ok=True)
    path = category_dir / f"{item_name}.json"
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    return path


# target name -> (data dict from item_data.py, output dir, writer function)
TARGETS = {
    "item_definitions": (item_data.ITEM_DEFINITIONS, ITEM_DEFINITIONS_DIR, write_item_definition),
    "item_models": (item_data.ITEM_MODELS, ITEM_MODELS_DIR, write_item_model),
}


def generate(target: str, category: str):
    data, out_dir, writer = TARGETS[target]
    if category not in data:
        print(f"  ! '{category}' isn't a known category for target '{target}', skipping")
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    items = data[category]
    for item_name in items:
        path = writer(out_dir, category, item_name)
        print(f"  ok {path.relative_to(SCRIPT_DIR)}")
    print(f"Generated {len(items)} file(s) for {target}:{category}\n")


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def flatten(data: dict) -> dict:
    """{category: [items]} -> {item_name: category}."""
    flat = {}
    for category, items in data.items():
        for item_name in items:
            flat[item_name] = category
    return flat


def find_duplicates(data: dict) -> dict:
    """Item names that appear in more than one category of the same target."""
    seen = {}
    dupes = {}
    for category, items in data.items():
        for item_name in items:
            if item_name in seen and seen[item_name] != category:
                dupes.setdefault(item_name, {seen[item_name]}).add(category)
            seen[item_name] = category
    return dupes


def verify():
    definitions = flatten(item_data.ITEM_DEFINITIONS)
    models = flatten(item_data.ITEM_MODELS)

    def_names = set(definitions)
    model_names = set(models)

    missing_models = sorted(def_names - model_names)
    missing_definitions = sorted(model_names - def_names)
    category_mismatch = sorted(
        name for name in (def_names & model_names)
        if definitions[name] != models[name]
    )

    print("=== Consistency check (item_data.py) ===")

    if missing_models:
        print(f"\nHave a definition but no model ({len(missing_models)}):")
        for name in missing_models:
            print(f"  - {name}  [definitions:{definitions[name]}]")

    if missing_definitions:
        print(f"\nHave a model but no definition ({len(missing_definitions)}):")
        for name in missing_definitions:
            print(f"  - {name}  [models:{models[name]}]")

    if category_mismatch:
        print(f"\nCategory mismatch between definition and model ({len(category_mismatch)}):")
        for name in category_mismatch:
            print(f"  - {name}  definitions:{definitions[name]} vs models:{models[name]}")

    for target_name, data in (
        ("ITEM_DEFINITIONS", item_data.ITEM_DEFINITIONS),
        ("ITEM_MODELS", item_data.ITEM_MODELS),
    ):
        dupes = find_duplicates(data)
        if dupes:
            print(f"\n{target_name} lists an item in more than one category:")
            for name, categories in dupes.items():
                print(f"  - {name}  in {sorted(categories)}")

    if not (missing_models or missing_definitions or category_mismatch):
        print("\nEverything lines up.")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    verify()

    # Edit this list to choose what to (re)generate this run.
    # Each entry is (target, category):
    #   target   -> "item_definitions" or "item_models"
    #   category -> a key from the matching dict in item_data.py
    GENERATE = [
        ("item_definitions", "fish"),
        ("item_models", "fish"),
    ]

    if not GENERATE:
        return

    print("This will write/overwrite files for:")
    for target, category in GENERATE:
        print(f"  - {target}:{category}")
    print("Proceed? (y/n)")
    if input().strip().lower() != "y":
        print("Cancelled.")
        return

    for target, category in GENERATE:
        generate(target, category)


if __name__ == "__main__":
    main()