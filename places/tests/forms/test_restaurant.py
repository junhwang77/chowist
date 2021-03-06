from django.test import TestCase

from places.forms import RestaurantForm


class TestRestaurantForm(TestCase):
    """RestaurantForm test suite"""

    def test_restaurant_form_valid_as_empty(self):
        form_data = {"category": "", "name": ""}
        form = RestaurantForm(form_data)
        self.assertTrue(form.is_valid())

    def test_restaurant_form_valid_as_partial(self):
        form_data = {"category": "Burgers", "name": ""}
        form = RestaurantForm(form_data)
        self.assertTrue(form.is_valid())

    def test_restaurant_form_valid_as_full(self):
        form_data = {
            "category": "Burgers",
            "name": "Five Guys",
            "min_party": 1,
            "max_party": 10,
        }
        form = RestaurantForm(form_data)
        self.assertTrue(form.is_valid())
