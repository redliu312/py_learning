from .basic import * 
from .basic import fancy_get_name

def test_basic_p_decorate():
    decorated_get_name = p_decorate(get_name)
    assert decorated_get_name("simon") == "<p>simon</p>"

def test_fancy_p_decorate():
    assert fancy_get_name("simon") == "<p>simon</p>"
