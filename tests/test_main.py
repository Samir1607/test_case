from main import hello, calculate


def test_hello():
    assert hello() == "Hello World"


def test_calculate():
    assert calculate() == 9
