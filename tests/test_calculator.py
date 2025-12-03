from calculator.main import add,sub

def test_add():
    assert add(3, 2) == 5 # nosec B101
def test_sub():
    assert sub(5,4) == 1 # nosec B101
