from utils.string_utils import string_repeater

def test_string_repeater():
    string = string_repeater("i", 7)
    expect = "iiiiiii"

    assert string == expect


