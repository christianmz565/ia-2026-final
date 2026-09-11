from .color_transfer import *
from .naive_composition import *

__all__ = [
    'color_transfer', 'get_composite_image', 'OPAScoreModel', 
    'HarmonyScoreModel', 'InharmoniousLocalizationModel',
    'ImageHarmonizationModel', 'PainterlyHarmonizationModel',
    'FOPAHeatMapModel', 'FOSScoreModel',
    'KontextBlendingHarmonizationModel',
    'ShadowGenerationModel', 'ReflectionGenerationModel',
    'OSInsertModel'
]

def __getattr__(name: str):
    if name == 'OPAScoreModel':
        from .opa_score import OPAScoreModel
        return OPAScoreModel
    elif name == 'HarmonyScoreModel':
        from .harmony_score import HarmonyScoreModel
        return HarmonyScoreModel
    elif name == 'InharmoniousLocalizationModel':
        from .inharmonious_region_localization import InharmoniousLocalizationModel
        return InharmoniousLocalizationModel
    elif name == 'ImageHarmonizationModel':
        from .image_harmonization import ImageHarmonizationModel
        return ImageHarmonizationModel
    elif name == 'PainterlyHarmonizationModel':
        from .painterly_image_harmonization import PainterlyHarmonizationModel
        return PainterlyHarmonizationModel
    elif name == 'FOPAHeatMapModel':
        from .fopa_heat_map import FOPAHeatMapModel
        return FOPAHeatMapModel
    elif name == 'FOSScoreModel':
        from .fos_score import FOSScoreModel
        return FOSScoreModel
    elif name == 'KontextBlendingHarmonizationModel':
        from .kontext_blending_harmonization import KontextBlendingHarmonizationModel
        return KontextBlendingHarmonizationModel
    elif name == 'ShadowGenerationModel':
        from .shadow_generation import ShadowGenerationModel
        return ShadowGenerationModel
    elif name == 'ReflectionGenerationModel':
        from .reflection_generation import ReflectionGenerationModel
        return ReflectionGenerationModel
    elif name == 'OSInsertModel':
        from .os_insert import OSInsertModel
        return OSInsertModel
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
