from cipherkit.alphabets import ascii_basic
from cipherkit.alphabets import decimal
from cipherkit.alphabets import english
from cipherkit.alphabets import spanish


def test_alphabet_spanish():
    expected_alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    assert spanish() == expected_alphabet


def test_alphabet_english():
    expected_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert english() == expected_alphabet


def test_alphabet_decimal():
    expected_alphabet = "0123456789"
    assert decimal() == expected_alphabet


def test_alphabet_ascii_basic():
    expected_alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    assert ascii_basic() == expected_alphabet
