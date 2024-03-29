import os 
import json
from dataclasses import dataclass, field

abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

@dataclass(frozen=True, order=True)
class Material: 
    name: str = 'material' 
    item_model_pre: int = 12345 # 'custom_model_data' component [12345XX]
    item_override_pre: str = 'stone' # for finding the item id
    
    
@dataclass(frozen=True, order=True)
class ToolType: 
    name: str = 'weapon'  
    item_model_suf: int = 67 # 'custom_model_data' compnent [XXXXX67]
    item_override_suf: str = 'sword' # for finding the item id
    
materials = [
    # Minecraft
    Material('wooden', 69057, 'wooden'),
    Material('golden', 69057, 'golden'),
    Material('stone', 69057, 'stone'),
    Material('iron', 69057, 'iron'),
    Material('diamond', 69057, 'diamond'),
    Material('netherite', 69057, 'netherite'),
    # Odyssey
    Material('copper', 69055, 'golden'),
    Material('silver', 69063, 'iron'),
    Material('soul_steel', 69066, 'iron'),
    Material('titanium', 69068, 'iron'),
    Material('andonized_titanium', 69070, 'iron'),
    Material('iridium', 69071, 'iron'),
    Material('mithril', 69076, 'iron'),
]

tool_types = [
    ToolType('katana', 44, 'sword'),
]