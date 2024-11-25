from trello.views import qwerty, qwerty1, qwerty2, qwerty3, qwerty4, qwerty5


def test_qwerty():
    assert 5 == qwerty()


def test_qwerty1():
    assert 5 == qwerty1()


def test_qwerty2():
    assert 6 == qwerty2()


def test_qwerty3():
    assert 5 == qwerty3()


def test_qwerty4():
    assert 5 == qwerty4()


def test_qwerty5():
    assert 5 == qwerty5()
