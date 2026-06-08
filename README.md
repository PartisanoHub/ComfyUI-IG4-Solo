# ComfyUI IG4 Solo

A lightweight, optimized custom guider node for ComfyUI. 

`IG4 Solo` provides precise control over conditioning modes, allowing you to switch between `cond_only`, `minimal_cfg`, and standard `cfg` modes. It is designed to be highly efficient and is perfect for advanced users looking to implement staged guidance workflows.

## Features
* **Three Optimized Modes:** Easily toggle between `cond_only` (pure positive), `minimal_cfg` (subtle guidance), and `cfg` (standard) modes.
* **Staged Guidance Ready:** Designed to pair perfectly with `CFGOverride` nodes for advanced "natural-to-sharp" sampling transitions.
* **Lightweight:** Clean, efficient code with no unnecessary dependencies.

## Installation

### Option 1: ComfyUI Manager (Recommended)
1. Open **ComfyUI Manager** in your browser.
2. Click **Install via Git URL**.
3. Paste the following URL:
   `https://github.com/PartisanoHub/ComfyUI-IG4-Solo`
4. Click **OK** and restart ComfyUI.

### Option 2: Manual (CLI)
1. Open your terminal or command prompt.
2. Navigate to your ComfyUI `custom_nodes` folder:
   `cd path/to/ComfyUI/custom_nodes`
3. Clone this repository:
   `git clone https://github.com/PartisanoHub/ComfyUI-IG4-Solo`
4. Restart ComfyUI.

## Usage
1. Add the **IG4 Solo** node to your workflow.
2. Connect the `GUIDER` output to your Sampler node.
3. For advanced results, use it in combination with a `CFGOverride` node to apply higher CFG values only during the final percentage of the sampling process (e.g., 80%–100%).

---
*Created with ❤️ for the ComfyUI community.*
