"""Tests for script.py"""

import pytest

from denoter import scripts


def test_main():
    # Smoke test
    with pytest.raises(TypeError):
        scripts.main(verbose=True)
