from cipherkit.alphabets import english
from cipherkit.ciphers import Caesar
from cipherkit.ciphers import Reverse


# This test was taken from: Hacking Secret ciphers with Python
def test_reverse_cipher_mode():
    expected_hidden_text = ".daed era meht fo owt fi ,terces a peek nac eerhT"
    plain_text = "three can keep a secret, if two of them are dead."

    assert Reverse.cipher(plain_text) == expected_hidden_text.upper()


def test_reverse_decipher_mode():
    expected_plain_text = "three can keep a secret, if two of them are dead."
    hidden_text = ".daed era meht fo owt fi ,terces a peek nac eerhT"

    assert Reverse.decipher(hidden_text) == expected_plain_text


def test_caesar_cipher_mode():
    expected_hidden_text = "avkhz shz bupkhklz yljpipyhu hwvfv hlylv.".upper()
    plain_text = "Todas las unidades recibiran apoyo aereo."
    key = 7  # a -> h

    assert Caesar.cipher(plain_text, key, alphabet=english()) == expected_hidden_text


def test_caesar_decipher_mode():
    expected_plain_text = "todas las unidades recibiran apoyo aereo."
    hidden_text = "avkhz shz bupkhklz yljpipyhu hwvfv hlylv.".upper()
    key = 7  # a -> 7

    assert Caesar.decipher(hidden_text, key, alphabet=english()) == expected_plain_text
