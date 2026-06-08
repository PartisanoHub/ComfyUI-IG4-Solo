import comfy.samplers

class _CondOnlyGuider(comfy.samplers.CFGGuider):
    """Positive conditioning only."""

    def set_conds(self, positive):
        self.inner_set_conds({"positive": positive})


class IG4Solo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "conditioning": ("CONDITIONING",),
                "mode": (
                    ["cond_only", "minimal_cfg", "cfg"],
                    {"default": "cond_only"},
                ),
            },
            "optional": {
                "guidance": (
                    "FLOAT",
                    {
                        "default": 1.05,
                        "min": 1.0,
                        "max": 15.0,
                        "step": 0.01,
                    },
                ),
                "negative": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("GUIDER",)
    RETURN_NAMES = ("guider",)
    FUNCTION = "get_guider"
    CATEGORY = "ideogram/optimize"

    def get_guider(
        self,
        model,
        conditioning,
        mode="cond_only",
        guidance=1.05,
        negative=None,
    ):

        # Fastest mode: positive branch only
        if mode == "cond_only":
            g = _CondOnlyGuider(model)
            g.set_conds(conditioning)
            g.set_cfg(1.0)

            print(
                "[IG4] cond_only "
                "(positive conditioning only)"
            )

            return (g,)

        # Small CFG using a null negative
        if mode == "minimal_cfg":
            null_negative = [[None, {}]]

            g = comfy.samplers.CFGGuider(model)
            g.set_conds(conditioning, null_negative)
            g.set_cfg(guidance)

            print(
                f"[IG4] minimal_cfg "
                f"(cfg={guidance:.2f}, null negative)"
            )

            return (g,)

        # Standard CFG
        if negative is None:
            raise ValueError(
                "CFG mode requires a negative conditioning input."
            )

        g = comfy.samplers.CFGGuider(model)
        g.set_conds(conditioning, negative)
        g.set_cfg(guidance)

        print(
            f"[IG4] cfg "
            f"(cfg={guidance:.2f})"
        )

        return (g,)


NODE_CLASS_MAPPINGS = {
    "IG4Solo": IG4Solo,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IG4Solo": "IG4 Solo",
}