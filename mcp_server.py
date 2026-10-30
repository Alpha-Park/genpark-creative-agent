# -*- coding: utf-8 -*-
"""
GenPark Creative Agent FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkCreativeAgent

mcp = FastMCP("genpark-creative-agent")
creative = GenParkCreativeAgent()

@mcp.tool()
def model_freytag_pyramid_dramaturgy(
    total_duration_sec: float = 60.0,
    acts_spec_json: Optional[str] = None
) -> str:
    """
    Models 5-act Freytag's Pyramid dramatic tension trajectory across video runtime.
    """
    acts = json.loads(acts_spec_json) if acts_spec_json else None
    res = creative.model_freytag_pyramid_dramaturgy(total_duration_sec, acts)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_aspect_ratio_reframe_matrix(
    source_width: int,
    source_height: int,
    target_aspect: str = "9:16",
    safe_zone_pct: float = 0.15
) -> str:
    """
    Calculates optimal crop bounding box and safe zones when reframing across aspect ratios.
    """
    res = creative.calculate_aspect_ratio_reframe_matrix(source_width, source_height, target_aspect, safe_zone_pct)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_color_grading_lut_transform(
    rgb_triplet_json: str,
    lut_profile: str = "teal_and_orange"
) -> str:
    """
    Simulates 3D cinematic color grading transform (RGB float values in range [0.0, 1.0]).
    """
    rgb = json.loads(rgb_triplet_json)
    res = creative.calculate_color_grading_lut_transform(rgb, lut_profile)
    return json.dumps(res, indent=2)

def main():
    print("Testing Creative Agent:")
    print(model_freytag_pyramid_dramaturgy(30.0))

if __name__ == "__main__":
    main()
