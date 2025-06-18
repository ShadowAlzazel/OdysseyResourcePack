import os 
import json

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

RUNE_ITEMS = [
    "amplify_rune",
    "ball_rune",
    "beam_rune",
    "bolt_rune",
    "break_rune",
    "convergence_rune",
    "differ_rune",
    "direct_rune",
    "heal_rune",
    "kernel_rune",
    "missile_rune",
    "nearby_rune",
    "next_rune",
    "origin_rune",
    "pick_up_rune",
    "point_rune",
    "self_rune",
    "size_rune",
    "slice_rune",
    "swap_rune",
    "teleport_rune",
    "trace_rune",
    "wall_rune",
    "zone_rune"
]

def create_rune_mark_json(rune_name):
    """Create JSON structure for rune mark"""
    mark_name = rune_name.replace("_rune", "_rune_mark")
    return {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"odyssey:item/arcane/{mark_name}"
        }
    }

def create_rune_json(rune_name):
    """Create JSON structure for rune"""
    mark_name = rune_name.replace("_rune", "_rune_mark")
    return {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": "odyssey:item/arcane/blank_rune",
            "layer1": f"odyssey:item/arcane/{mark_name}"
        }
    }

def generate_files():
    """Generate all rune and rune mark JSON files"""

    for rune_name in RUNE_ITEMS:
        # Generate rune mark file
        mark_name = rune_name.replace("_rune", "_rune_mark")
        mark_json = create_rune_mark_json(rune_name)
        
        #mark_file_path = os.path.join("rune_marks", f"{mark_name}.json")
        mark_file_path = f"{mark_name}.json"
        with open(mark_file_path, 'w', encoding='utf-8') as f:
            json.dump(mark_json, f, indent=2)
        
        print(f"Created: {mark_file_path}")
        
        # Generate rune file
        rune_json = create_rune_json(rune_name)
        
        rune_file_path = f"{rune_name}.json"
        with open(rune_file_path, 'w', encoding='utf-8') as f:
            json.dump(rune_json, f, indent=2)
        
        print(f"Created: {rune_file_path}")

if __name__ == "__main__":
    print("Generating rune and rune mark JSON files...")
    generate_files()
    print(f"\nGeneration complete! Created {len(RUNE_ITEMS)} rune files and {len(RUNE_ITEMS)} rune mark files.")