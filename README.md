# Cryptographer
A cryptographer who encrypts and decrypts text using such methods as: Caesar cipher, Vernam cipher, Vigener cipher and others

To start program you should download main.py, gui.py, crypt_engine.py in one directory and run main.py in the python interpreter.

The program has grphic interface. There are 4 possible modes. Encrypt and Decrypt text. Encrypt and Decrypt file.

Ecnrypt mode: You should push the button - "Зашифровать". In opened window you should write text that will be encypted. 
Then you have to choose encryption mode and to write a key (number for Caesar cipher and Dynamic Caesar, word or phrase for Vernam cipher and Vigener cipher)
Then, you should push the button "Зашифровать". In the special form you will see your encrypted text.

Decrypt mode: The same as Encrypt mode, but decrypt yout text. Has the same interface. To start you should push "Расшифровать". The special type of decryption is "Взлом Цезаря". 
It will decrypt you Caesar Cipher without a key, using frequency analysis method. The lenght of string should be enough. 

Encrypt file: You should push the button - "Зашифровать файл". The will be 2 forms to write into. In first one you should write a path to the file that will be encrypted.
In the second one you should write a path to the file where encrypted text will be written (you may leave this form empty if you want to rewrite file). Other interface the same as in Encrypt mode.

Decrypt file: The same as Decrypt file mode, but decrypt text in your file. Has the same interface. Also contains "Взлом Цезаря".

# Ciphers' descriptions
Description of Caesar Cipher: https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F

Description of Verman Cipher: https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B5%D1%80%D0%BD%D0%B0%D0%BC%D0%B0

Decription of Vigener Cipher: https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0

Description of Dynamic Caesar: the same as Caesar Cipher, but offset is not constant, it depends off the lenght of the string from the beginning to this character. 
For example, Dynamic Caesar(abcd, 1 - starting offset): a -> b, b -> d, c -> f, d -> h.
