import pytest
from ..SimulatePositions.provaTest import fakefunc
from ..SimulatePositions.provaTest import another_fakefunc

# FILE: SimulatePositions/test_provaTest.py


def test_fakefunc():
    assert fakefunc() == 1

def test_another_fakefunc():
    assert another_fakefunc() == 2