import pytest

from projectname import square


def test_main():
    assert square(2) == 4
    assert square(0) == 0
