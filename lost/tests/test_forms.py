from datetime import date
from django.test import TestCase

from ..forms import PostForm


class PostFormTest(TestCase):
    def test_post_form_name_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Name')

    def test_post_form_name_field_help_text(self):
        form = PostForm()
        self.assertEqual(form.fields['name'].help_text, 'Enter the name or title of lost object')

    def test_post_form_type_of_object_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['type_of_object'].label == None or form.fields['type_of_object'].label == 'Type of object')

    def test_post_form_type_of_object_field_help_text(self):
        form = PostForm()
        self.assertEqual(form.fields['type_of_object'].help_text, 'What type of object are you posting')

    def test_post_form_description_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['description'].label == None or form.fields['description'].label == 'Description')

    def test_post_form_location_found_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['location_found'].label == None or form.fields['location_found'].label == 'Location found')

    def test_post_form_location_found_field_help_text(self):
        form = PostForm()
        self.assertEqual(form.fields['location_found'].help_text, 'Where did you find the object?')

    def test_post_form_pickup_details_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['pickup_details'].label == None or form.fields['pickup_details'].label == 'Pickup details')

    def test_post_form_pickup_details_field_help_text(self):
        form = PostForm()
        self.assertEqual(form.fields['pickup_details'].help_text, 'Details of pickup location')

    def test_post_form_posted_at_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['posted_at'].label == None or form.fields['posted_at'].label == 'Posted at')

    def test_post_form_status_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['status'].label == None or form.fields['status'].label == 'Status')

    def test_post_form_image_field_label(self):
        form = PostForm()
        self.assertTrue(form.fields['image'].label == None or form.fields['image'].label == 'Image')
