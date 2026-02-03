from pathlib import Path

import pytest


try:
    import pytest_doctestplus.plugin
    pytest_doctestplus
except ImportError:
    raise ImportError("Install pytest-doctestplus to run the tests")


pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    return Path(__file__).parent.resolve() / 'sphinx_math_dollar' / 'tests'
