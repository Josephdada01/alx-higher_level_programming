import unittest
from models.square import Square

class TestSquareMethod(unittest.TestCase):
    def test_init_valid_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_init_valid_size_with_position(self):
        square = Square(5, 2, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_init_invalid_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_init_negative_size(self):
        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_init_invalid_types(self):
        with self.assertRaises(TypeError):
            square = Square("5")

    def test_update_with_args(self):
        square = Square(4)
        square.update(1, 2, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_with_kwargs(self):
        square = Square(4)
        square.update(id=1, size=2, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_mixed_args_kwargs(self):
        square = Square(4)
        square.update(1, 2, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    def test_to_dictionary_empt_square(self):
        with self.assertRaises(ValueError):
            square = Square(0)
            square_dict = square.to_dictionary()

    def test_str_representation(self):
        square = Square(4, 1, 2, 3)
        str_repr = str(square)
        self.assertEqual(str_repr, "[Square] (3) 1/2 - 4")

    def test_str_representation_no_id(self):
        square = Square(6)
        str_repr = str(square)
        self.assertEqual(str_repr, "[Square] (6) 0/0 - 6")

if __name__ == '__main__':
    unittest.main()
