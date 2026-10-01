import pytest
from ..KingdomsAndWarfare.Official.Units.Humans.units import human_infantry

def test_human_infantry():
    assert human_infantry.attacks == 1
    assert human_infantry.damage == 1
    assert human_infantry.name == "Human Infantry"