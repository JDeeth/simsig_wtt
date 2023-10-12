import pytest

import app


def test_changeme_add():
    assert app.add(2, 2) == 4
