import pytest
import snakeparser


def test_project_defines_author_and_version():
    assert hasattr(snakeparser, '__author__')
    assert hasattr(snakeparser, '__version__')
