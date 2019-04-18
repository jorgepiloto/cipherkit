from cipherkit.ciphers import reverse


# This test was taken from: Hacking Secret ciphers with Python
def test_reverse_cipher_mode():
    expected_hidden_text = ".daed era meht fo owt fi ,terces a peek nac eerhT"
    text = "Three can keep a secret, if two of them are dead."

    assert reverse(text) == expected_hidden_text
