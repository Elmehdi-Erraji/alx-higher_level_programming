#!/usr/bin/python3
"""
test_square module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test class for Suqare class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1(self):
        """test 1"""
        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s0.__str__(), "[Square] (1) 0/0 - 1")
        self.assertEqual(s0.area(), 1)
        output = {'id': 1, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s0.to_dictionary(), output)
        s0.update()
        self.assertEqual(s0.__str__(), "[Square] (1) 0/0 - 1")
        s0.update(89)
        self.assertEqual(s0.__str__(), "[Square] (89) 0/0 - 1")
        s0.update(89, 1)
        self.assertEqual(s0.__str__(), "[Square] (89) 0/0 - 1")
        s0.update(89, 1, 2)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/0 - 1")
        s0.update(89, 1, 2, 3)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0_dictionary = s0.to_dictionary()
        s1 = Rectangle.create(**s0_dictionary)
        self.assertIsNot(s0, s1)

    def test_2(self):
        """test 2"""
        s0 = Square(1, 2)
        self.assertEqual(s0.id, 1)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s0.__str__(), "[Square] (1) 2/0 - 1")
        self.assertEqual(s0.area(), 1)
        output = {'id': 1, 'x': 2, 'size': 1, 'y': 0}
        self.assertEqual(s0.to_dictionary(), output)
        s0.update()
        self.assertEqual(s0.__str__(), "[Square] (1) 2/0 - 1")
        s0.update(89)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/0 - 1")
        s0.update(89, 1)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/0 - 1")
        s0.update(89, 1, 2)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/0 - 1")
        s0.update(89, 1, 2, 3)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

    def test_3(self):
        """test 3"""
        s0 = Square(1, 2, 3)
        self.assertEqual(s0.id, 1)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.__str__(), "[Square] (1) 2/3 - 1")
        self.assertEqual(s0.area(), 1)
        output = {'id': 1, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(s0.to_dictionary(), output)
        s0.update()
        self.assertEqual(s0.__str__(), "[Square] (1) 2/3 - 1")
        s0.update(89)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1, 2)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1, 2, 3)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

    def test_4(self):
        """test 4"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
        	Square("1")

    def test_5(self):
        """test 5"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
        	Square(1, "2")

    def test_6(self):
        """test 6"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
        	Square(1, 2, "3")

    def test_7(self):
        """test 7"""
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.id, 4)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(s0.area(), 1)
        output = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(s0.to_dictionary(), output)
        s0.update()
        self.assertEqual(s0.__str__(), "[Square] (4) 2/3 - 1")
        s0.update(89)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1, 2)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(89, 1, 2, 3)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")
        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

    def test_8(self):
        """test 8"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
        	Square(-1)

    def test_9(self):
        """test 9"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
        	Square(1, -2)

    def test_10(self):
        """test 10"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
       		Square(1, 2, -3)

    def test_11(self):
        """test 11"""
       	with self.assertRaisesRegex(ValueError, "width must be > 0"):
        	Square(0)



if __name__ == '__main__':
    unittest.main()
