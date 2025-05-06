import unittest

class TestCase(unittest.TestCase):
    # def test_syntax_error_if_not_multiline(self):

    #     try:
    #         d"csv\nx"
    #     except SyntaxError:
    #         pass
    #     else:
    #         self.fail("Syntax Error not raised")

    def test_simplestr(self):
        self.assertEqual(
            d"""
            x
            """,
            "x\n"
        )

    def test_str_with_hint(self):
        self.assertEqual(
            d"""csv
            x
            """,
            "x\n"
        )


if __name__ == '__main__':
    unittest.main()
