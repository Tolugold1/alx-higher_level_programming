#!/usr/bin/python3
"""
Collection of tests for Rectangle class.
"""
import contextlib
from io import StringIO
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class RectangleTest(unittest.TestCase):
    """Test Rectangle methods."""

    def setUp(self):
        """Set up Base class tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tidy up after test methods."""
        pass

    def test_type(self):
        """Test type."""
        r1 = Rectangle(10, 2)
        self.assertTrue(type(r1) == Rectangle)

    def test_valid_id(self):
        """Test valid id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_valid_width_height(self):
        """Test for valid width and height."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

    def test_valid_x_y(self):
        """Test for valid x and y."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 7, 8, 12)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)

    def test_string(self):
        """Test string input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, "1", 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, "1")
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_float(self):
        """Test float input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2.5)
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10.5, 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1.5, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, 1.5)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_bool(self):
        """Test boolean input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, True)
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(False, 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, True, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, False)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_inf(self):
        """Test infinity input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, float('inf'))
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(float('inf'), 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, float('inf'), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, float('inf'))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_nan(self):
        """Test nan input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, float('nan'))
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(float('nan'), 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, float('nan'), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, float('nan'))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_list(self):
        """Test list input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, [1, 2, 3])
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle([1, 2, 3], 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, [1, 2, 3], 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, [1, 2, 3])
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_tuple(self):
        """Test tuple input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, (1, 2, 3))
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle((1, 2, 3), 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, (1, 2, 3), 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, (1, 2, 3))
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_set(self):
        """Test set input."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, {1, 2, 3})
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle({1, 2, 3}, 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, {1, 2, 3}, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, {1, 2, 3})
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_negative(self):
        """Test negative input."""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual('width must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.height = -10
        self.assertEqual('height must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2, 1, 1)
            r.x = -10
        self.assertEqual('x must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2, 1, 1)
            r.y = -10
        self.assertEqual('y must be >= 0', str(cm.exception))

    def test_zero(self):
        """Test zero input."""
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(0, 2, 1, 1)
        self.assertEqual('width must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 0, 1, 1)
        self.assertEqual('height must be > 0', str(cm.exception))
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_empty(self):
        """Test missing arguments."""
        with self.assertRaises(TypeError) as cm:
            Rectangle()
        self.assertEqual("__init__() missing 2 required positional " +
                         "arguments: 'width' and 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10)
        self.assertEqual("__init__() missing 1 required positional argument:" +
                         " 'height'", str(cm.exception))

    def test_extra_parameter(self):
        """Test with extra parameter."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual('__init__() takes from 3 to 6 positional arguments ' +
                         'but 7 were given', str(cm.exception))

    def test_unknown_parameter(self):
        """Test with unknown parameter."""
        with self.assertRaises(NameError):
            r1 = Rectangle(a)

    def test_none(self):
        """Test none arguments."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, None)
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(None, 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, None, 1)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 1, None)
        self.assertEqual('y must be an integer', str(cm.exception))

    def test_area(self):
        """Test valid areas."""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(4, 6)
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '####\n####\n####\n####\n####\n####\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(2, 2)
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '##\n##\n')

    def test_str(self):
        """Test __str__."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (12) 2/1 - 4/6\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r2 = Rectangle(5, 5, 1)
            print(r2)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 1/0 - 5/5\n')

    def test_display_x_y(self):
        """Test display, handling x and y."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '\n\n  ##\n  ##\n  ##\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(3, 2, 1, 0)
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, ' ###\n ###\n')

    def test_update(self):
        """Test update."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 10/10 - 10/10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 10/10 - 10/10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 10/10 - 2/10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2, 3)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 10/10 - 2/3\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2, 3, 4)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 4/10 - 2/3\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2, 3, 4, 5)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 4/5 - 2/3\n')

    def test_update_extra_parameter(self):
        """Test update with extra parameters."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2, 3, 4, 5, 6, 7)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 4/5 - 2/3\n')

    def test_update_blank(self):
        """Test update with no parameters."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update()
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 10/10 - 10/10\n')

    def test_update_kwargs(self):
        """Test update with kwargs."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 10/10 - 10/10\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.update(height=1)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 10/10 - 10/1\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.update(width=1, x=2)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 2/10 - 1/1\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.update(y=1, width=2, x=3, id=89)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 3/1 - 2/1\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.update(x=1, height=2, y=3, width=4)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 1/3 - 4/2\n')

    def test_update_kwargs_extra(self):
        """Test update with extra kwargs."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(x=1, height=2, y=3, width=4, brent=5)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 1/3 - 4/2\n')

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

        self.assertEqual(r1 == r2, False)

    def test_to_json(self):
        """Test to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
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
            r1 = Rectangle(10, 7, 2, 8)
            r2 = Rectangle(2, 4)
            Rectangle.save_to_file([r1, r2])
            with open("Rectangle.json", "r") as file:
                print(file.read())
        output = temp_stdout.getvalue()

if __name__ == '__main__':
    unittest.main()
