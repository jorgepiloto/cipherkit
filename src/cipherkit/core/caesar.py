""" This script holds caesar cipher and it main routines. """


def caesar(plain_text, key, alphabet, mode="cipher"):
    """ Cipher by making use of caesar algorithm.

    Parameters
    ----------
    plain_text: str
        Text to be ciphered.
    key: int
        Key for cipher.
    alphabet:
        Alphabet that contains the characters of the language.

    Returns
    -------
    hidde_text: str
        Ciphered text.
    """

    if not isinstance(key, int):
        raise ValueError("Key should be an integer value.")

    hidden_text = ""

    for character in plain_text.upper():

        if character in alphabet:
            # This means we can cipher that letter
            pos = alphabet.index(character)

            if mode == "cipher":
                pos = (pos + key) % len(alphabet)
            else:
                pos = (pos - key) % len(alphabet)
            hidden_text += alphabet[pos]

        else:
            hidden_text += character

    return hidden_text
