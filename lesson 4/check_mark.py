from string_utils import StringUtils
import pytest

text = StringUtils ()

@pytest.mark.parametrize('some_text, simbol, res', 
[('mari', 'i', True), ('mar45i', 'r12', False)])
def test_end_with(some_text, simbol, res):
    assert text.end_with(some_text, simbol) == res 

@pytest.mark.negative
def test_negative_del_symbol_ ():
    assert text.delete_symbol(" ", " ") == "" 