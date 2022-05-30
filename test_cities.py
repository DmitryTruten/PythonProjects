import unittest
from city_functions import cities


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        """Will it work with names like 'Kyiv, Ukraine'?"""
        formatted_city_country = cities('kyiv,', 'ukraine')
        self.assertEqual(formatted_city_country, 'Kyiv, Ukraine')  # add assertion here

    def test_city_country_population(self):
        formatted_city_country_population = cities('kyiv,', 'ukraine -', 46_000_000)
        self.assertEqual(formatted_city_country_population, 'Kyiv, Ukraine - 46000000')


if __name__ == '__main__':
    unittest.main()
