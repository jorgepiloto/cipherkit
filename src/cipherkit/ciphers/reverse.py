""" The reverse cipher works changing last character from the text to the first
place and so on."""


def reverse(text):
    """ Ciphers or deciphers by reverse algorithm.

    Parameters
    ----------
    text: string
        Text to cipher or decipher.

    Returns
    -------
    hidden_text: string
        Ciphered or deciphered text.


    Notes
    -----
    Since this cipher has only one key, no cipher or decipher mode is provided.
    """

    n = len(text)
    hidden_text = ""
    while n > 0:
        hidden_text += text[n - 1]
        n -= 1

    return hidden_text
