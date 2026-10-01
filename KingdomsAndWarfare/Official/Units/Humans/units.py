from KingdomsAndWarfare.Units import Unit, Infantry, Artillery, Cavalry, Aerial
from KingdomsAndWarfare.Units.UnitEnums import Experience, Equipment, Tier
from ...Traits import Traits

human_infantry = Unit(
    "Human Infantry",
    Infantry,
    "Run-of-the-mill men-at-arms armed with swords and pikes.",
    "Human",
    Experience.REGULAR,
    Equipment.LIGHT,
    Tier.I,
    6,
    1,
    1,
    3,
    12,
    2,
    12,
    1,
    2,
    [Traits.ADAPTABLE]
)