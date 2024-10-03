import unittest

from main import num2hex


class Tests(unittest.TestCase):
    def test_num2hex(self):
        self.assertEqual(num2hex(-100), 0x9c)
        self.assertEqual(num2hex(100), 0x64)

        buttons = 0
        x = -100
        y = -100
        byte_string = f"\\x{num2hex(buttons):02x}\\x{num2hex(x):02x}\\x{num2hex(y):02x}"
        print('byte_string:', byte_string)
        self.assertEqual(byte_string, '\\x00\\x9c\\x9c')


if __name__ == '__main__':
    unittest.main()
