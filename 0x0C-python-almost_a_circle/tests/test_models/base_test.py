#!/usr/bin/python3
"""
Collection of tests for Base class.
"""
import contextlib
from io import StringIO
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Test Base methods."""

    def setUp(self):
        """Set up Base class tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tidy up after test methods."""
        pass

    def test_type(self):
        """Test type."""
        b1 = Base()
        self.assertTrue(type(b1) == Base)

    def test_id(self):
        """Test id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -1)

    def test_unknown(self):
        """Test name error."""
        with self.assertRaises(NameError):
            Base(a)

    def test_to_json(self):
        """Test to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")

    def test_to_json_rectangle(self):
        """Test to_json_string length for rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary),
                         len(str([{"x": 2, "width": 10, "id": 1, "height": 7,
                                   "y": 8}])))
        self.assertTrue(type(json_dictionary), dict)
        self.assertTrue(type(json_dictionary) is str)

    def test_to_json_square(self):
        """Test to_json_string length for square."""
        s1 = Square(10, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary),
                         len(str([{"x": 2, "size": 10, "id": 1, "y": 8}])))
        self.assertTrue(type(json_dictionary), dict)

    def test_to_json_empty(self):
        """Test to_json_string method with empty and None."""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_empty(self):
        """Test to_json_string method with empty string."""
        json_dictionary = Base.to_json_string('')
        self.assertEqual(json_dictionary, '[]')

    def test_save_to_file_rectangle_len(self):
        """Test length of json string rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as file:
            self.assertEqual(len(file.read()), len(str(
                [{"x": 2, "id": 6, "width": 10, "y": 8, "height": 7},
                 {"x": 0, "id": 7, "width": 2, "y": 0, "height": 4}])))

    def test_save_to_file_square_len(self):
        """Test length of json string square."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json") as file:
            self.assertEqual(len(file.read()), len(str(
                    [{"x": 7, "id": 8, "size": 10, "y": 2},
                     {"x": 4, "id": 7, "size": 2, "y": 0}])))

    def test_save_to_file_rectangle(self):
        """Test save_to_file rectangle empty."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_square(self):
        """Test save_to_file square empty."""
        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_rectangle_none(self):
        """Test save_to_file square empty."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_square_none(self):
        """Test save_to_file with None."""
        Square.save_to_file(None)
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string_three(self):
        """Test from_json_string three inputs."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4},
                                       {'id': 7, 'width': 1, 'height': 7}])
        self.assertTrue(type(list_output), list)

    def test_from_json_string_two(self):
        """Test from_json_string two inputs."""
        list_input = [{'id': 89, 'size': 10}, {'id': 7, 'size': 1}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'size': 10},
                                       {'id': 7, 'size': 1}])
        self.assertTrue(type(list_output), list)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string('')
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output), list)

    def test_create(self):
        """Test create."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(3, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 1/0 - 3/5\n')
        self.assertTrue(type(r1) == Rectangle)

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(3)
            s1_dictionary = s1.to_dictionary()
            s2 = Square.create(**s1_dictionary)
            print(s1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (3) 0/0 - 3\n')
        self.assertTrue(type(s1) == Square)

    def test_create2(self):
        """Test create, check for new instance."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(3, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)
            print(r2)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 1/0 - 3/5\n')
        self.assertTrue(type(r2) == Rectangle)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_none(self):
        """Test create with None."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)

    def test_create_int(self):
        """Test create with int."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(1, 2, 3)

    def test_create_string(self):
        """Test create with string."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create('string')

    def test_create_name_error(self):
        """Test create with name error."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(NameError):
            r2 = Rectangle.create(**betty)

    def test_load_from_file_rectangle(self):
        """Test load from file rectangle."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1 = Rectangle(10, 7, 2, 8)
            r2 = Rectangle(2, 4)
            list_rectangles_input = [r1, r2]
            Rectangle.save_to_file(list_rectangles_input)
            list_rectangles_output = Rectangle.load_from_file()
            print(list_rectangles_output[0])
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 2/8 - 10/7\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(list_rectangles_output[1])
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (2) 0/0 - 2/4\n')
        self.assertTrue(type(list_rectangles_output), list)

    def test_load_from_file_square(self):
        """Test load from file square."""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(5)
            s2 = Square(7, 9, 1)
            list_squares_input = [s1, s2]
            Square.save_to_file(list_squares_input)
            list_squares_output = Square.load_from_file()
            print(list_squares_output[0])
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 0/0 - 5\n')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(list_squares_output[1])
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (2) 9/1 - 7\n')
        self.assertTrue(type(list_squares_output), list)

if __name__ == '__main__':
    unittest.main()
