# -*- coding: utf-8 -*-
"""
GenPark Creative Agent Client
Zero-dependency Freytag's Pyramid narrative dramaturgy curve modeler,
multi-aspect ratio crop/safe-zone reframe solver, and 3D LUT color grading matrix transformer.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkCreativeAgent:
    """
    Models video/story tension curves, solves multi-platform reframe crop geometry,
    and calculates color grading transforms.
    """

    ASPECT_RATIOS = {
        "9:16": (9.0, 16.0),    # TikTok / IG Reels / YouTube Shorts
        "1:1": (1.0, 1.0),      # Instagram Square Feed
        "16:9": (16.0, 9.0),    # Landscape / Desktop Video
        "4:5": (4.0, 5.0)       # Portrait Social Feed
    }

    def model_freytag_pyramid_dramaturgy(
        self,
        total_duration_sec: float = 60.0,
        acts_spec: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Models 5-act Freytag's Pyramid dramatic tension trajectory across video runtime:
        1. Exposition -> 2. Inciting / Rising -> 3. Climax -> 4. Falling -> 5. Resolution
        """
        if total_duration_sec <= 0:
            raise ValueError("Duration must be positive.")

        # Default standard dramatic arc proportions
        default_acts = [
            {"act": "Exposition & Hook", "start_pct": 0.0, "end_pct": 0.15, "tension_start": 0.25, "tension_end": 0.40},
            {"act": "Rising Action & Conflict", "start_pct": 0.15, "end_pct": 0.55, "tension_start": 0.40, "tension_end": 0.85},
            {"act": "Climax / Turning Point", "start_pct": 0.55, "end_pct": 0.70, "tension_start": 0.85, "tension_end": 1.00},
            {"act": "Falling Action & Momentum", "start_pct": 0.70, "end_pct": 0.88, "tension_start": 0.80, "tension_end": 0.50},
            {"act": "Resolution & CTA", "start_pct": 0.88, "end_pct": 1.00, "tension_start": 0.50, "tension_end": 0.30}
        ]
        acts = acts_spec or default_acts

        timeline_samples = []
        num_samples = 20
        step_dt = total_duration_sec / float(num_samples)

        for i in range(num_samples + 1):
            t_sec = round(i * step_dt, 1)
            t_ratio = min(1.0, t_sec / total_duration_sec)

            # Find matching act
            matched_act = acts[-1]
            for act in acts:
                if act["start_pct"] <= t_ratio <= act["end_pct"]:
                    matched_act = act
                    break

            # Interpolate tension inside act
            act_len = max(0.01, matched_act["end_pct"] - matched_act["start_pct"])
            local_t = (t_ratio - matched_act["start_pct"]) / act_len
            # Smooth sine easing for organic tension build
            eased_local = math.sin(local_t * math.pi / 2.0)
            tension = matched_act["tension_start"] + (matched_act["tension_end"] - matched_act["tension_start"]) * eased_local

            timeline_samples.append({
                "timestamp_sec": t_sec,
                "progress_pct": round(t_ratio * 100.0, 1),
                "act_name": matched_act["act"],
                "tension_score": round(max(0.0, min(1.0, tension)), 3)
            })

        avg_tension = sum(s["tension_score"] for s in timeline_samples) / len(timeline_samples)
        climax_ts = [s["timestamp_sec"] for s in timeline_samples if s["tension_score"] >= 0.95]

        return {
            "total_duration_sec": total_duration_sec,
            "average_tension": round(avg_tension, 3),
            "climax_peak_sec": climax_ts[0] if climax_ts else round(0.65 * total_duration_sec, 1),
            "act_count": len(acts),
            "timeline_samples": timeline_samples
        }

    def calculate_aspect_ratio_reframe_matrix(
        self,
        source_width: int,
        source_height: int,
        target_aspect: str = "9:16",
        safe_zone_pct: float = 0.15
    ) -> Dict[str, Any]:
        """
        Calculates optimal crop bounding box and safe zones when reframing across aspect ratios.
        """
        if source_width <= 0 or source_height <= 0:
            raise ValueError("Dimensions must be positive.")

        target_w_ratio, target_h_ratio = self.ASPECT_RATIOS.get(target_aspect, (9.0, 16.0))
        target_aspect_val = target_w_ratio / target_h_ratio
        source_aspect_val = source_width / float(source_height)

        if source_aspect_val > target_aspect_val:
            # Source is wider than target: crop width (pillar reframe)
            crop_h = source_height
            crop_w = int(round(crop_h * target_aspect_val))
            crop_x = int(round((source_width - crop_w) / 2.0))
            crop_y = 0
            reframe_mode = "CENTER_CROP_HORIZONTAL"
        else:
            # Source is taller than target: crop height
            crop_w = source_width
            crop_h = int(round(crop_w / target_aspect_val))
            crop_x = 0
            crop_y = int(round((source_height - crop_h) / 2.0))
            reframe_mode = "CENTER_CROP_VERTICAL"

        # Action Safe Zone (e.g. 15% margin from edges for UI buttons/captions)
        safe_margin_x = int(round(crop_w * safe_zone_pct))
        safe_margin_y = int(round(crop_h * safe_zone_pct))

        safe_zone_box = {
            "x": crop_x + safe_margin_x,
            "y": crop_y + safe_margin_y,
            "w": crop_w - 2 * safe_margin_x,
            "h": crop_h - 2 * safe_margin_y
        }

        return {
            "source_dimensions": {"width": source_width, "height": source_height},
            "target_aspect_ratio": target_aspect,
            "reframe_mode": reframe_mode,
            "crop_box": {"x": crop_x, "y": crop_y, "width": crop_w, "height": crop_h},
            "safe_zone_pct": safe_zone_pct,
            "safe_zone_box": safe_zone_box,
            "pixel_retention_pct": round(100.0 * (crop_w * crop_h) / (source_width * source_height), 1)
        }

    def calculate_color_grading_lut_transform(
        self,
        rgb_triplet: List[float],
        lut_profile: str = "teal_and_orange"
    ) -> Dict[str, Any]:
        """
        Simulates 3D cinematic color grading transform (RGB float values in range [0.0, 1.0]).
        """
        if len(rgb_triplet) != 3:
            raise ValueError("RGB triplet must contain exactly 3 floats.")

        r, g, b = [max(0.0, min(1.0, val)) for val in rgb_triplet]
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

        if lut_profile == "teal_and_orange":
            # Push shadows (low luminance) toward cyan/teal, highlights toward warm amber/orange
            if luminance < 0.5:
                # Shadows: cool teal
                factor = (0.5 - luminance) * 0.4
                r_out = max(0.0, r - factor * 0.5)
                g_out = min(1.0, g + factor * 0.2)
                b_out = min(1.0, b + factor * 0.6)
            else:
                # Highlights: warm orange
                factor = (luminance - 0.5) * 0.4
                r_out = min(1.0, r + factor * 0.6)
                g_out = min(1.0, g + factor * 0.2)
                b_out = max(0.0, b - factor * 0.4)
        elif lut_profile == "monochrome_noir":
            # High-contrast black & white
            contrast = 1.3
            mono = max(0.0, min(1.0, 0.5 + (luminance - 0.5) * contrast))
            r_out, g_out, b_out = mono, mono, mono
        else: # natural neutral
            r_out, g_out, b_out = r, g, b

        # Post-grading saturation & contrast
        lum_out = 0.2126 * r_out + 0.7152 * g_out + 0.0722 * b_out

        return {
            "lut_profile": lut_profile,
            "input_rgb": [round(c, 3) for c in rgb_triplet],
            "input_luminance": round(luminance, 3),
            "output_rgb": [round(r_out, 3), round(g_out, 3), round(b_out, 3)],
            "output_luminance": round(lum_out, 3),
            "chromatic_shift_vector": [round(r_out - r, 3), round(g_out - g, 3), round(b_out - b, 3)]
        }
