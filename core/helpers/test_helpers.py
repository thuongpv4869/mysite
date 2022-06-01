import unittest
from . import helpers


class TestHelpers(unittest.TestCase):

    def test_get_batch_index(self):
        # data test: (num,step,expect)
        data = [
            (8, 3, [[1, 2, 3], [4, 5, 6], [7, 8]]),
            (9, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ]

        except_data = [
            (0, 1),
            (0, 0),
            (1, 0)
        ]

        for d in except_data:
            with self.assertRaises(Exception):
                helpers.get_batch_index(*d)

        for d in data:
            rs = helpers.get_batch_index(d[0], d[1])
            self.assertCountEqual(rs, d[2])
