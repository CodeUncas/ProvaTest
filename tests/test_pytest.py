import pytest
from ..SimulatePositions.provaTest import fakefunc
from ..SimulatePositions.provaTest import anotherfakefunc  
# FILE: SimulatePositions/test_provaTest.py


def test_fakefunc():
    assert fakefunc() == 1

def test_anotherfakefunc():
    assert anotherfakefunc() == 2