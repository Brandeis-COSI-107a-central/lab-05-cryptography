

# Lab 5: Cryptography

Due Wednesday, March 5, 2025, by 9 PM

In this lab, we will explore some ideas in cryptography using Python, particularly the widely-used Python `cryptography` library, which is an add-on module.

The programming parts have tests for your code, which you can run with `make test` as usual.

As before, the `program` assignments are for code on GHC, and the `question` parts are to be answered on Gradescope.

If you get stuck on one part, you might find it helpful to skip to the next one and come back to it later.


# Exploring the Caesar cipher


## Implement ROT13

As discussed in class, ROT13 is sometimes used as the name for an algorithm that rotates letters 13 places in the alphabet. For example, A -> N, B-> O, etc.

> Program 1. Write a Python function `rot13` that takes a string as an argument and returns the ROT13 version of it. Upper case letters should be mapped to upper case, lower case to lower case, and any other characters to themselves.
> 
> Use your `rot13` function in a program called `rot13.py` that reads lines from standard input and prints the ROT13 versions. A simple version of the code that calls it this way might be:
> 
>     for arg in sys.stdin:
>         print(rot13(arg))
> 

If your program is in `rot13.py`, running `make test` should let you check if it&rsquo;s working correctly.

Python tip: You can get the numeric value for a character in Python with the `ord` function, and convert a number to a character with using `chr`.

If you save your function in a file called `rot13.py`, you can import it into the Python interpreter to try it out interactively. Here&rsquo;s an example:

    # The first command imports your code into the top-level namespace.
    >>> from rot13 import *
    >>> rot13('hi there')
    'uv gurer'
    >>> rot13('WHO GOES THERE')
    'JUB TBRF GURER'
    >>> rot13("Who knows the key?")
    'Jub xabjf gur xrl?'


## Generalize the Caesar cipher with a simple key

> Program 2. Julius Caesar didn&rsquo;t use ROT13. Instead, he shifted letters by 3 places. Make a new version of your function called `rotN` that takes an optional argument `count` that is the number of places to rotate. The default value of `count` should be 13, and the result of a call like `rotN('abc', 13)` should be exactly the same as the result of `rot13('abc')`.
> 
> You might need to look up how optional arguments work for Python functions.
> 
> Your program in the file `rotN.py` should take an optional command line argument used for `count`.  Like `rot13.py`, it should read lines from standard input and print the result of calling `rotN` on them.
> 
> Examples:
> 
>     >>> rotN("Attack at dawn", 11)
>     'Leelnv le olhy'
>     >>> rotN("where is the pizza?", 2)
>     'yjgtg ku vjg rkbbc?'
>     >>> rotN("lwpi'h udg qgtpzuphi?", 11)
>     "what's for breakfast?"
> 
> Use `make test` to test your program.
> 


## Breaking ROT13

One way to break a code is by &ldquo;brute force,&rdquo; by guessing many possibilities for the code. Computers are good at repetitive work, but even then it can take them a long time.

> Question 1. Think about how you might use brute force to decode an unknown Caesar cipher and describe your approach.
> 


## Multiple rounds

In the 1970s, a block cipher called the Data Encryption Standard (DES) was standardized by the US government for many uses, including banking. It used 56-bit keys. When those became possibly vulnerable to brute-force attacks, some people used &ldquo;Triple DES,&rdquo; which used three rounds of DES with three separate DES keys.

> Question 2. Would it improve security to do &ldquo;Triple ROT13,&rdquo; in which ROT13 was done three times? Why or why not?
> 


> Question 3. Would it improve security to do &ldquo;Triple Caesar,&rdquo; with three different rotations applied? Why or why not?
> 


# Secret-key encryption with AES

In this part, we&rsquo;ll experiments with secret-key encryption using AES as our algorithm.

First, make sure that your Kali system has the Python `cryptography` library installed. The following should work without any errors.

    % python3
    >>> import cryptography

If `cryptography` is not installed, you can install it with `sudo apt install python3-cryptography`.

The `cryptography` documentation with the AES example we looked at in class is at [Symmetric encryption — Cryptography latest documentation](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/). Feel free to refer to it in working on this lab.

We&rsquo;ll also need to use binary data in Python, as described in the lab manual.

> Program 3. Write a program called `aes-try.py` that takes three arguments command-line arguments: an `inputfile`, `keyfile_name`, and an `outputfile`.
> 
> It should then:
> 
> 1.  Generate a random AES key (as shown in class)
> 2.  Generate a random initialization vector
> 3.  Write the key and initialization vector sequentially into the binary file named by the `keyfile_name` argument.
> 4.  Encrypt the contents of the file named by `inputfile`, using cipher-block chaining mode. Since we are using CBC mode, the data may need to be padded to a multiple of the block size (see below).
> 5.  Write the encrypted data in binary form to the file named by `outputfile`.
> 

The test code works by verifying that it can decrypt your output file using the key file you saved. This means that you may get some errors from different parts of the test program in your debugging.

Padding is necessary to make the data a multiple of the block size. We are using PKCS7 padding for this assignment. The Python cryptography library documentation discusses how to use padding with AES at [Symmetric Padding — Cryptography 2.7 documentation](https://cryptography.io/en/2.7/hazmat/primitives/padding/).

> Question 4. What is the purpose of the initialization vector?
> 


> Question 5. Why do we use cipher-block chaining mode for this kind of encryption? Explain why it matters.
> 


# Public-key operations with RSA

For this part, we&rsquo;ll be exploring how to use some basic operations with RSA as our public-key algorithm. The main documentation for the functions we will use can be found at [RSA — Cryptography 43.0.0.dev1 documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/). We will not be using passwords for the RSA keys, so where appropriate, use `password=None`.


## Generating a key

> Program 4. Using the techniques described in the `cryptography` documentation, write a program `rsa-genkey.py` that generates an RSA keypair. It should save the public key in the file `rsa-key.pub` and the private key in the file `rsa-key.priv`.
> 

> Question 6. The library method for saving the private key can take a password argument; the one for saving a public key does not. Why do you think this choice was made?
> 


> Question 7. If you were writing a real application using RSA keys, would you use a password to save private keys?
> 


## Encrypting and decrypting messages with RSA

> Program 5. Next, write a program called `rsa-encrypt.py` that takes one command-line argument, the name of a file to encrypt. Your program should encrypt the contents of the file using the public key, and the encrypted output should be saved in a file named `encrypted.bin`.
> 

> Program 6. Similarly, using the same keypair files, write a program called `rsa-decrypt.py` to decrypt the file given on the command line.
> 

Note: when encrypting using an RSA key, for strong cryptographic protection, the size of the message plus the padding must be less than the length of the key. This normally restricts the use of RSA encryption to small messages, which is one of the reasons that&rsquo;s it&rsquo;s often just used to encrypt a symmetric cipher key. If you try to encrypt a larger message (try it!) you&rsquo;ll get a rather mysterious error message.


## Signing a message and checking a signature

Finally, we have two more short programs for digital signatures.

> Program 7. First, write a program `rsa-sign.py` that uses your keypair files to digitally sign the contents of file named on the command line. Your program should write the signature in binary form to the file `myfile.sig`.
> 

> Program 8. Second, write a program `rsa-verify.py` that can verify a signature on a file. It should take three command-line arguments:
> 
> -   **`keyfile`:** The base name of the key file to use. Assume that the public key will be found in that file with a `.pub` extension, and the private key in that file with a `.priv` extension.
> -   **`datafile`:** The name of a text file that contains the original message data that was signed.
> -   **`signature_file`:** The name of a binary file containing a possible signature for the file.
> 

Your program should use the key pair in the `keyfile` files to verify the signature. It should print the line &ldquo;Verified!&rdquo; or &ldquo;Not verified!&rdquo; on stdout (with no quotes), depending on whether the signature verifies or not. Note that there are tests for both cases.

