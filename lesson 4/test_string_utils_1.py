from string_utils import StringUtils
import pytest

text = StringUtils ()

# позитивные тесты

def test_cap ():
    assert text.capitilize(" mARi") == " MARi" and text.capitilize("m12a ri ") == "M12a ri " and text.capitilize("mari") == "Mari" and text.capitilize("Mari") == "Mari"

def test_trim ():
    assert text.trim("   marina") == "marina" and text.trim("MaR12i3") == "MaR12i3" and text.trim("M  aRi") == "M  aRi" and text.trim("MaRi ") == "MaRi "

def test_to_list ():
    assert text.to_list("1,1,0:1:3", ":") == ["1,1,0", "1", "3"] and text.to_list("1-2", "-") == ["1", "2"] and text.to_list("a,n,7") == ["a", "n", "7"]

def test_contains ():
    assert text.contains("Ma1ri Po", "Ma1") == True and text.contains("Ma r2iPo", "ur2") == False

def test_del_symbol():
    assert text.delete_symbol("Mar1 ina2", "a") == "Mr1 in2" and text.delete_symbol("Mar12ina", "2i") == "Mar1na"

def test_starts_with():
    assert text.starts_with("M1arinaPo", "M1") == True and text.starts_with("MarinaPo", "m") == False and text.starts_with("Mar2inaPo", "Mar1") == False

def test_end_with():
    assert text.end_with("Mari2", "i2") == True and text.end_with("Mari", "Mari") == True and text.end_with("Mari ", " ") == True and text.end_with("Mari 2", " 1") == False

def test_is_empty():
    assert text.is_empty("123") == False and text.is_empty(" tex t ") == False

def test_list_to_string():
    assert text.list_to_string([1, 2,3]) == "1, 2, 3" and text.list_to_string(["2", "a"]) == "2, a" and text.list_to_string([2, "a", 1]) == "2, a, 1"

# негативные тесты 
#@pytest.mark.negative

def test_negative_cap ():
    assert text.capitilize("") == "" 

def test_negative_cap_ ():
    assert text.capitilize(" ") == " "

def test_negative_cap_none ():
    assert text.capitilize(None) == None # AttributeError


def test_negative_trim ():
    assert text.trim("") == "" 
    
def test_negative_trim_ ():
    assert text.trim("  ") == "" 
    
def test_negative_trim_none ():
    assert text.trim(None) == None # AttributeError


def test_negative_to_list ():
    assert text.to_list("1,1,0:1:3", "") == ["1", "1", "0:1:3"] # ValueError: empty separator

def test_negative_to_list_ ():
    assert text.to_list("1-2", " ") == ["1-2"]

def test_negative_to_list_none ():
    assert text.to_list("a,n,7", None) == ["a", "n", "7"] # AssertionError ['a,n,7']


def test_negative_contains ():
    assert text.contains("MariPo", "") == True 

def test_negative_contains_empty_all ():
    assert text.contains("", "") == True 
    
def test_negative_contains_ ():
    text.contains(" ", " ") == True
    
def test_negative_contains_none ():
    assert text.contains("MariPo", None) == False #  TypeError: must be str, not NoneType

def test_negative_contains_none_ ():
    assert text.contains(None) == False # TypeError missing 1 required positional argument: 'symbol'


def test_negative_del_symbol ():
    assert text.delete_symbol("Mar1ina2", "") == "Mar1ina2" 

def test_negative_del_symbol_empty_all ():
    assert text.delete_symbol("", "") == "" 
    
def test_negative_del_symbol_ ():
    assert text.delete_symbol(" ", " ") == "" 
    
def test_negative_del_symbol_none ():
    assert text.delete_symbol("None", None) == "None" # TypeError: must be str, not NoneType

def test_negative_del_symbol_none_ ():
    assert text.delete_symbol(None) == "" # TypeError: StringUtils.delete_symbol() missing 1 required positional argument: 'symbol'


def test_negative_starts_with ():
    assert text.starts_with(" MarinaPo", "") == False # AssertionError
    
def test_negative_starts_with_ ():
    assert text.starts_with(" ", " ") == True 
    
def test_negative_starts_with_none ():
    assert text.starts_with(" MarinaPo", None) == False # TypeError: startswith first arg must be str or a tuple of str, not NoneType

def test_negative_starts_with_none ():
    assert text.starts_with(None) == False # TypeError


def test_negative_end_with ():
    assert text.end_with("", "") == True 

def test_negative_end_with_ ():
    assert text.end_with(" ", " ") == True
    
def test_negative_end_with_none ():
    assert text.end_with(" MarinaPo", None) == False # TypeError: endswith first arg must be str or a tuple of str, not NoneType

def test_negative_end_with_none_ ():
    assert text.end_with(None) == False # TypeError: StringUtils.end_with() missing 1 required positional argument: 'symbol'


def test_negative_is_empty ():
    assert text.is_empty("") == True 
    
def test_negative_is_empty_ ():
    assert text.is_empty(" ") == True 
    
def test_negative_is_empty_none ():
    assert text.is_empty(None) == True #  AttributeError: 'NoneType' object has no attribute 'startswith'


def test_negative_list_to_string_none ():
    assert text.list_to_string([]) == ""
    
@pytest.mark.negative 
def test_negative_list_to_string_ ():
    assert text.list_to_string([ ]) == "" 
    
