from cipherkit.alphabets import ascii_basic

from cipherkit.core.reverse import reverse
from cipherkit.core.caesar import caesar


class Reverse(object):
    """ This is the class for reverse cipher. """

    def __init__(self, plain_text, hidden_text):
        """ Constructo for the cipher.

        Parameters
        ----------
        plain_text: str
            Text to be ciphered.
        hidden_text: str
            Text ciphered.
        """

        self.plain_text = plain_text.lower()
        self.hidden_text = hidden_text.upper()

    @classmethod
    def cipher(cls, plain_text):
        """ Cipher mode.

        Parameters
        ----------
        text: str
            Text to be ciphered. """

        hidden_text =  reverse(plain_text)
        return cls(plain_text, hidden_text).hidden_text

    @classmethod
    def decipher(cls, hidden_text):
        """ Decipher mode.

        Parameters
        ----------
        hidden_text: str
            Text to be deciphered.
        """

        plain_text = reverse(hidden_text)
        return cls(plain_text, hidden_text).plain_text

class Caesar(object):
    """ This is the class for Caesar cipher. """

    def __init__(self, plain_text, hidden_text, key, alphabet):
        """ Constructo for the cipher.

        Parameters
        ----------
        plain_text: str
            Text to be ciphered.
        hidden_text: str
            Text ciphered.
        """

        self.plain_text = plain_text.lower()
        self.hidden_text = hidden_text.upper()
        self.key = key
        self.alphabet = alphabet

    @classmethod
    def cipher(cls, plain_text, key, alphabet=ascii_basic()):
        """ Cipher mode.

        Parameters
        ----------
        plain_text: str
            Text to be ciphered.
        key: int
            Key to cipher with.
        alphabet: str
            String that contains all the characters of the language.
        """

        hidden_text = caesar(plain_text, key, alphabet, mode='cipher')

        return cls(plain_text, hidden_text, key, alphabet).hidden_text

    @classmethod
    def decipher(cls, hidden_text, key, alphabet=ascii_basic()):
        """ Decipher mode.

        Parameters
        ----------
        hidden_text: str
            Text to be deciphered.
        key: int
            Key to decipher with.
        alphabet: str
            String that contains all the characters of the language.
        """
        plain_text = caesar(hidden_text, key, alphabet, mode='decipher')

        return cls(plain_text, hidden_text, key, alphabet).plain_text
