# -*- coding: utf-8 -*-
import json
from client import GenParkCreativeAgent

agent = GenParkCreativeAgent()

# 1. Freytag's Pyramid 5-Act Dramatic Arc
arc = agent.model_freytag_pyramid_dramaturgy(total_duration_sec=45.0)
print(f"Dramatic Arc: Total={arc['total_duration_sec']}s | AvgTension={arc['average_tension']} | Peak Climax at {arc['climax_peak_sec']}s")
for s in arc["timeline_samples"][::4]:
    print(f"  {s['timestamp_sec']}s ({s['progress_pct']}%): {s['act_name']} -> Tension: {s['tension_score']}")

# 2. Multi-Aspect Ratio Reframe & Safe Zone Geometry
reframe = agent.calculate_aspect_ratio_reframe_matrix(
    source_width=1920,
    source_height=1080,
    target_aspect="9:16",
    safe_zone_pct=0.15
)
print()
print(f"Reframe to 9:16: Mode={reframe['reframe_mode']} | Retained={reframe['pixel_retention_pct']}%")
print(f"  Crop Box: {reframe['crop_box']}")
print(f"  Action Safe Zone: {reframe['safe_zone_box']}")

# 3. Cinematic 3D LUT Color Grading Simulation
lut_res = agent.calculate_color_grading_lut_transform([0.2, 0.3, 0.4], lut_profile="teal_and_orange")
print()
print(f"Teal & Orange LUT: In={lut_res['input_rgb']} -> Out={lut_res['output_rgb']} (Shift: {lut_res['chromatic_shift_vector']})")
