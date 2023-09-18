import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        """ test valid input """
        r = Rectangle(5, 10, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

        """ testing for invalid width, height, x and y """
        def test_invalid_width(self):
            with self.assertRaises(ValueError):
                r = Rectangle(-5, 10, 2, 3)

        def test_invalid_height(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, -10, 2, 3)

        def test_invalid_x(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, 10, -2, 3)

        def test_invalid_y(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, 10, 2, -3)

        def test_invalid_width_height(self):
            with self.assertRaises(ValueError):
                r = Rectangle(-5, -10, 2, 3)

        def test_invalid_height_x(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, -10, -2, 3)

        def test_invalid_x_y(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, 10, -2, -3)

        def test_invalid_width_x(self):
            with self.assertRaises(ValueError):
                r = Rectangle(-5, 10, -2, 3)

        def test_invalid_height_y(self):
            with self.assertRaises(ValueError):
                r = Rectangle(5, -10, 2, -3)

        def test_invalid_all(self):
            with self.assertRaises(ValueError):
                r = Rectangle(-5, -10, -2, -3
        
        """ testing for width and height are invalid types"""
        def test_invalid_type_width(self):
            with self.assertRaises(TypeError):
                r = Rectangle("5", 10, 2, 3)

        def test_invalid_type_height(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5, "10", 2, 3)

        def test_invalid_tpe_x(self):
            with self.assertRaises(TypeError):
                r = Rectangle("5", 10, "2", 3)

        def test_invalid_type_y(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5, 10, 2, "3")

        def test_invalid_type_float_width(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5.5, 10, 2, 3)

        def test_invalid_typ_float_hei(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5, 10.1, 2, 3)

        def test_invalid_typ_float_x(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5, 10, 2.2, 3)

        def test_invalid_typ_float_y(self):
            with self.assertRaises(TypeError):
                r = Rectangle(5, 10, 2, 3.3)

        def test_to_dictionary(self):
            r = Rectangle(5, 10, 2, 3, 1)
            expected_dict = {
                'id': 1,
                'width': 5,
                'height': 10,
                'x': 2,
                'y': 3
                }
            self.assertEqual(r.to_dictionary(), expected_dict)

        def test_update(self):
            r = Rectangle(5, 10, 2, 3, 1)
            r.update(2, 7, 8, 4, 5)
            self.assertEqual(r.id, 2)
            self.assertEqual(r.width, 7)
            self.assertEqual(r.height, 8)
            self.assertEqual(r.x, 4)
            self.assertEqual(r.y, 5)

            r.update(width=9, y=6)
            self.assertEqual(r.width, 9)
            self.assertEqual(r.y, 6)
