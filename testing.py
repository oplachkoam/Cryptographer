import crypt_engine
import unittest

class TestCryptEngine(unittest.TestCase):
    def test_most_popular_item(self):
        self.assertEqual(crypt_engine.most_popular_item([0, 1, 1, 1, 3, 3, 10]), 1)
        self.assertEqual(crypt_engine.most_popular_item([0, 1, 1, 3, 3, 3, 10]), 3)
        self.assertEqual(crypt_engine.most_popular_item([0, 1, 1, 1, 3, 3, 3, 10]), 1)
        self.assertEqual(crypt_engine.most_popular_item([10, -5, 12, 1, 1, 14, 10, 10]), 10)

    def test_language_definition(self):
        self.assertEqual(crypt_engine.language_definition("hello, world"), crypt_engine.english_alphabet)
        self.assertEqual(crypt_engine.language_definition("привет, мир"), crypt_engine.russian_alphabet)
        self.assertEqual(crypt_engine.language_definition("hello, world привет, мир"), None)
        self.assertEqual(crypt_engine.language_definition("!!!{}{}.,\\//\t"), None)

    def test_line_formatting(self):
        self.assertEqual(crypt_engine.line_formatting("hello, world"), "hello world")
        self.assertEqual(crypt_engine.line_formatting("ПРИВЕТ МИР"), "привет мир")
        self.assertEqual(crypt_engine.line_formatting("HeLlO\nWoRlD"), "hello\nworld")
        self.assertEqual(crypt_engine.line_formatting("П-р-И-в-Е-т"), "п р и в е т")

    def test_cesar_encrypting(self):
        self.assertEqual(crypt_engine.cesar_encrypting("abcde", 1), "bcdef")
        self.assertEqual(crypt_engine.cesar_encrypting("abcde", 26), "abcde")
        self.assertEqual(crypt_engine.cesar_encrypting("эюя", 3), "абв")
        self.assertEqual(crypt_engine.cesar_encrypting("привет", 33), "привет")

    def test_dynamic_cesar_encrypting(self):
        self.assertEqual(crypt_engine.dynamic_cesar_encrypting("abcd", 0), "aceg")
        self.assertEqual(crypt_engine.dynamic_cesar_encrypting("эюя", 3), "авд")
        self.assertEqual(crypt_engine.dynamic_cesar_encrypting("привет", 33), "пскеич")

    def test_visener_encrypting(self):
        self.assertEqual(crypt_engine.visener_encrypting("ATTACKATDAWN", "lemon"), "LXFOPVEFRNHR".lower())
        self.assertEqual(crypt_engine.visener_encrypting("пришёл увидел победил", "забег"), "чрйэиу угнжмл рудмдйр")
        self.assertEqual(crypt_engine.visener_encrypting("lemon", "lemon"), "wiyca")

    def test_verman_encrypting(self):
        self.assertEqual(crypt_engine.visener_encrypting("ATTACKATDAWN", "lemon"), "LXFOPVEFRNHR".lower())
        self.assertEqual(crypt_engine.visener_encrypting("пришёл увидел победил", "забег"), "чрйэиу угнжмл рудмдйр")
        self.assertEqual(crypt_engine.visener_encrypting("lemon", "lemon"), "wiyca")

    def test_cesar_decrypt(self):
        self.assertEqual(crypt_engine.cesar_decrypt("bcdef", 1), "abcde")
        self.assertEqual(crypt_engine.cesar_decrypt("abcde", 26), "abcde")
        self.assertEqual(crypt_engine.cesar_decrypt("абв", 3), "эюя")
        self.assertEqual(crypt_engine.cesar_decrypt("привет", 33), "привет")

    def test_dynamic_cesar_decrypt(self):
        self.assertEqual(crypt_engine.dynamic_cesar_decrypt("aceg", 0), "abcd")
        self.assertEqual(crypt_engine.dynamic_cesar_decrypt("авд", 3), "эюя")
        self.assertEqual(crypt_engine.dynamic_cesar_decrypt("пскеич", 33), "привет")

    def test_verman_decrypt(self):
        self.assertEqual(crypt_engine.verman_decrypt("LXFOPVEFRNHR", "lemon"), "ATTACKATDAWN".lower())
        self.assertEqual(crypt_engine.verman_decrypt("чрйэиу угнжмл рудмдйр", "забег"), "пришёл увидел победил")
        self.assertEqual(crypt_engine.verman_decrypt("wiyca", "lemon"), "lemon")

    def test_visener_decrypt(self):
        self.assertEqual(crypt_engine.visener_decrypt("LXFOPVEFRNHR", "lemon"), "ATTACKATDAWN".lower())
        self.assertEqual(crypt_engine.visener_decrypt("чрйэиу угнжмл рудмдйр", "забег"), "пришёл увидел победил")
        self.assertEqual(crypt_engine.visener_decrypt("wiyca", "lemon"), "lemon")

    def test_auto_hack_cesar(self):
        ru_string = "Строка, которая будет использована для тестирования функции взлома методом частотного анализа"
        en_string = "String, that will be used to test hack function by frequency analysis method"
        for i in range(34):
            encrypted = crypt_engine.cesar_encrypting(ru_string, i)
            hacked = crypt_engine.auto_hack_cesar(encrypted)
            self.assertEqual(hacked, crypt_engine.line_formatting(ru_string))
        for i in range(27):
            encrypted = crypt_engine.cesar_encrypting(en_string, i)
            hacked = crypt_engine.auto_hack_cesar(encrypted)
            self.assertEqual(hacked, crypt_engine.line_formatting(en_string))

if __name__ == '__main__':
    unittest.main()