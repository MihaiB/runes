import runes
import unittest


class Test(unittest.TestCase):

    def test_describe(self):
        for ch, desc in {
            " ": "' ' U+0020  SPACE  [20]",
            "\n": "'\\n' U+000A  " + runes.NO_NAME + "  [0a]",
            "\t": "'\\t' U+0009  " + runes.NO_NAME + "  [09]",
            "a": "'a' U+0061  LATIN SMALL LETTER A  [61]",
            "\x00": "'\\x00' U+0000  (none)  [00]",
            "€": "'€' U+20AC  EURO SIGN  [e2 82 ac]",
            "∞": "'∞' U+221E  INFINITY  [e2 88 9e]",
            "\u200b": "'\\u200b' U+200B  ZERO WIDTH SPACE  [e2 80 8b]",
            "🤠": "'🤠' U+1F920  FACE WITH COWBOY HAT  [f0 9f a4 a0]",
                }.items():
            self.assertEqual(runes.describe(ch), desc)
