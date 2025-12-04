from metrics import accuracy

def test_accuracy():
    assert accuracy(
        [0, 1, 1, 0],
        [0, 1, 0, 0]
    ) > 0.5