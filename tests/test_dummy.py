import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2017, 5, 12)
        self.assertEqual(weekday, "Friday")

        weekday = calculate(2010, 6, 30)
        self.assertEqual(weekday, "Wednesday")

        weekday = calculate(2012, 2, 29)
        self.assertEqual(weekday, "Wednesday")

        weekday = calculate(2014, 2, 29)
        self.assertEqual(weekday, None)

        weekday = calculate(2100, 2, 29)
        self.assertEqual(weekday, None)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        retcode = main(("--year", "a2001", "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode, 0)

        retcode = main(("--year", "-2001", "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode, 0)


if __name__ == '__main__':
    unittest.main()
