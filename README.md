# Cipherkit: a cryptography toolbox made with Python

<img align="left" src="docs/img/logo_cipherkit.png">

A Python package holding classical ciphers and different cryptanalysis tools.
For the moment, this package is under heavy development. Some of the features
it will include are the following:

- Classical ciphers: atbash, caesar, vigenere, affine...
- Crytanalysis tools: brute force and frequancy analysis
- Language identifier based on dictionaries

Once the package is complete and first versions start releasing, some future
implementation would be:

- Work with .txt files
- Steganography algorithms
- Modern non-symmetric ciphers


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/cipherkit/badge/?version=latest)](https://cipherkit.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/jorgepiloto/cipherkit.svg?branch=master)](https://travis-ci.org/jorgepiloto/cipherkit)


## Why cryptography?

Cryptography is one of the most used sciencies today due to its strong relation
with cryptocurrencies, money transactions, online business and others. Most of
moder ciphers try to solve the key-exchange problem by using a public/private
keys.

Elliptic curves, hash functions, RSA, AES and others may be familiar when we
talk about modern cryptography. Their implementation is really smart and at
the same time really counter-intuitive. It is not only the process of designing
the cipher but also to make as 'hard' as possible for cryptanalysists.

Although classical ciphers are just obsolete in termns of security, this package
objective is just to have fun with their implementation in a beautiful
programming language.

## Books and sources about cryptography

There exist really good books on cryptography history, algorithms and
cryptanalysis techniques. Some of them, which were used consulted during
the coding phase of this package ares listed down:

- Hacking secret ciphers with Python, AI Sweigart
- The Code Book, Simon Singh
- Boletín Enigma, Arturo Quirantes Sierra
- Cripgrafía sin secretos con Python, David Arboledas


## Installation

```bash
pip install cipherkit
```



## Documentation

https://cipherkit.readthedocs.io/


## Development

Bug solving, new features and improves are always welcome. This is an opensource
project: we want to have fun, learn and improve. For that reason if you have
doubts, issues with the package or just want to add a new cipher please follow
the following steps:

- Fork cipherkit
- Download and install with *pip install -e cipherkit*. This wll install the
  package in editable mode, which will enable you to make code changes and
  continue while using cipherkit.
- Create a new branch in your local repo, improve the code and start a pull
  request.
- Celebrate your first contribution.

