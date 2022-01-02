from unittest import TestCase


class TestEmptyString(TestCase):

    def test_emptystring_shouldreturnboolfalse(self):
        string = ""
        self.assertFalse(string)

    def test_emptystring_whenhascondition_shouldreturnboolfalse(self):
        string = ""
        if not string:
            self.assertFalse(string)

    def test_emptystring_shouldreturnbooltrue(self):
        string = "Teste"
        self.assertTrue(string)