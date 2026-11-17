---
name: genpark-creative-agent
description: Batch media generator and brand-style image pipeline.
---
# genpark-creative-agent

An open-source GenPark alternative to anlah AI: CanArt.

Feed it your brand's image assets. The agent fine-tunes a local LoRA model and automatically generates cohesive product photography, ad banners, and short-form video sequences locally via ComfyUI/FFmpeg workflows.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.
