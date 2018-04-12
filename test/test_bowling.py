import unittest

from source.main import function_somme_tupe


class Test(unittest.TestCase):

    def test_tuple(self):
        self.assertEqual(function_somme_tupe([(1, 2), (3, 4)]), 10)

    def test_limite_zero(self):
        self.assertEqual(function_somme_tupe([(1, 0)]), 1)

    def test_spare(self):
        self.assertEqual(function_somme_tupe([(5, 5), (5, 2)]), 22)

    def test_strike(self):
        self.assertEqual(function_somme_tupe([(10, 0), (5, 2)]), 24)

    def test_chain_strike(self):
        self.assertEqual(function_somme_tupe([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (5, 2)]), 139)

    def test_chain_strike_2(self):
        self.assertEqual(function_somme_tupe([(10, 0), (10, 0), (10, 0), (2, 0)]), 66)

    def test_full_strike(self):
        self.assertEqual(function_somme_tupe(
            [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
             (10, 0)]), 300)

    def test_spare_coup(self):
        self.assertEqual(function_somme_tupe(
            [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (5, 5)]), 285)

    def test_limite_dix(self):
        self.assertEqual(function_somme_tupe([(10, 0)]), 10)

    def test_tuple_negatif(self):
        with self.assertRaises(TypeError):
            function_somme_tupe([(1, -2), (3, 4)])

    def test_nb_tuple_sup_douze(self):
        with self.assertRaises(TypeError):
            function_somme_tupe(
                [(1, 2), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
                 (1, 2), (1, 2), (1, 2)])

    def test_tuple_sup_dix(self):
        with self.assertRaises(TypeError):
            function_somme_tupe([(1, 20), (3, 4)])

    def test_nb_tuple_sup_dix(self):
        with self.assertRaises(TypeError):
            function_somme_tupe(
                [(1, 3), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4)])
