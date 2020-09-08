import pytest
from lib.compilermgr import * 

@pytest.fixture(scope="module")
def compiler_gen():
    return compilermgr("sample/c.json")

def test_generate(compiler_gen):
    compiler_cmd = compiler_gen.generate()
    assert compiler_cmd != "gcc-8 -g3 -rdynamic %s -o -lpthread -lm"
