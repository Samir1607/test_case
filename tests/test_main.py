import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import hello, calculate


def test_hello():
    assert hello() == "Hello World"


def test_calculate():
    assert calculate() == 9
