#!/usr/bin/python3
"""
Collection of tests for Square class.
"""
import contextlib
from io import StringIO
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):
    """Test Square methods."""

    def setUp(self):
        """Set up Base class tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tidy up after test methods."""
        pass

    def test_type(self):
        """Test type."""
        s1 = Square(5)
        self.assertTrue(type(s1) == Square)

    def test_valid_id(self):
        """Test valid id."""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_valid_size(self):
        """Test for valid size."""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)

    def test_valid_x_y(self):
        """Test for valid x and y."""
        s1 = Square(10)
        s2 = Square(10, 7, 8, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 8)

    def test_string(self):
        """Test string input."""
        with self.assertRaises(TypeError) as cm:
            Square("10")
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, "1", 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, "1")
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_float(self):
        """Test float input."""
        with self.assertRaises(TypeError) as cm:
            Square(2.5)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 2.5, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, 2.5)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_bool(self):
        """Test boolean input."""
        with self.assertRaises(TypeError) as cm:
            Square(True)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, False, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, True)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_inf(self):
        """Test infinity input."""
        with self.assertRaises(TypeError) as cm:
            Square(float('inf'))
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, float('inf'), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, float('inf'))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_nan(self):
        """Test nan input."""
        with self.assertRaises(TypeError) as cm:
            Square(float('nan'))
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, float('nan'), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, float('nan'))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_list(self):
        """Test list input."""
        with self.assertRaises(TypeError) as cm:
            Square([1, 2, 3])
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, [1, 2, 3], 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, [1, 2, 3])
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_tuple(self):
        """Test tuple input."""
        with self.assertRaises(TypeError) as cm:
            Square((1, 2, 3))
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, (1, 2, 3), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, (1, 2, 3))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_set(self):
        """Test set input."""
        with self.assertRaises(TypeError) as cm:
            Square({1, 2, 3})
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, {1, 2, 3}, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, {1, 2, 3})
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_negative(self):
        """Test negative input."""
        with self.assertRaises(ValueError) as cm:
            s = Square(-10)
        self.assertEqual('width must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            s = Square(10, -1, 1)
        self.assertEqual('x must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            s = Square(10, 1, -1)
        self.assertEqual('y must be >= 0', str(cm.exception))

    def test_zero(self):
        """Test zero input."""
        with self.assertRaises(ValueError) as cm:
            s = Square(0)
        self.assertEqual('width must be > 0', str(cm.exception))
        s = Square(10, 0, 1)
        self.assertEqual(s.x, 0)
        s = Square(10, 1, 0)
        self.assertEqual(s.y, 0)

    def test_empty(self):
        """Test missing argument."""
        with self.assertRaises(TypeError) as cm:
            Square()
        self.assertEqual("__init__() missing 1 required positional argument:" +
                         " 'size'", str(cm.exception))

    def test_extra_parameter(self):
        """Test with extra parameter."""
        with self.assertRaises(TypeError) as cm:
            Square(1, 2, 3, 4, 5)
        self.assertEqual('__init__() takes from 2 to 5 positional arguments ' +
                         'but 6 were given', str(cm.exception))

    def test_none(self):
        """Test none arguments."""
        with self.assertRaises(TypeError) as cm:
            Square(None)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, None, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1, None)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_area(self):
        """Test valid areas."""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        """Test display."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(5)
            s1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '#####\n#####\n#####\n#####\n#####\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(2)
            s1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '##\n##\n')

    def test_str(self):
        """Test __str__."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(5)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 0/0 - 5\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s2 = Square(4, 2, 1, 12)
            print(s2)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (12) 2/1 - 4\n')

    def test_display_x_y(self):
        """Test display, handling x and y."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(2, 2)
            s1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '  ##\n  ##\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(3, 1, 3)
            s1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '\n\n\n ###\n ###\n ###\n')

    def test_update(self):
        """Test update."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 10/10 - 10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(89)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 10/10 - 10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(89, 2)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 10/10 - 2\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(89, 2, 3)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/10 - 2\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(89, 2, 3, 4)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/4 - 2\n')

    def test_update_extra_parameter(self):
        """Test update with extra parameters."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(89, 2, 3, 4, 5, 6, 7)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/4 - 2\n')

    def test_update_blank(self):
        """Test update with no parameters."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update()
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 10/10 - 10\n')

    def test_update_kwargs(self):
        """Test update with kwargs."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 10/10 - 10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1.update(size=1)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 10/10 - 1\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1.update(size=1, x=2)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 2/10 - 1\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1.update(y=1, width=2, x=3, id=89)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/1 - 2\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1.update(x=1, size=2, y=3)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 1/3 - 2\n')

    def test_update_kwargs_extra(self):
        """Test update with extra kwargs."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 10, 10)
            s1.update(x=1, size=2, y=3, brent=5)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 1/3 - 2\n')

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(10, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'size': 10})

        s2 = Square(1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'size': 10})

        self.assertEqual(s1 == s2, False)

    def test_to_json(self):
        """Test to_json_string method."""
        s1 = Square(10, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")

    def test_to_json_empty(self):
        """Test to_json_string method with empty and None."""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_save_to_file(self):
        """Test save_to_file method."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(10, 2, 8)
            s2 = Square(2)
            Rectangle.save_to_file([s1, s2])
            if path.isfile("Square.json"):
                with open("Square.json", "r") as file:
                    print(file.read())
        output = temp_stdout.getvalue()

if __name__ == '__main__':
    unittest.main()
