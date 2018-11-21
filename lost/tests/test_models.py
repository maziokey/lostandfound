from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date

from ..models import Post

# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        username = 'john'
        password = '123'
        user = User.objects.create_user(username=username, email='john@doe.com', password=password)
        Post.objects.create(name='Police badge', type_of_object='badge', description='A police badge belonging to sergent rogers', location_found='inside a bus', pickup_details='Holy rosary church, agbakpa.', posted_at = date.today(), created_by=user, status='AVAILABLE', image='/home/okey/Pictures/badge.jpg')

    def test_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_type_of_object_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('type_of_object').verbose_name
        self.assertEquals(field_label, 'type of object')

    def test_description_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_location_found_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('location_found').verbose_name
        self.assertEquals(field_label, 'location found')

    def test_pickup_details_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('pickup_details').verbose_name
        self.assertEquals(field_label, 'pickup details')

    def test_posted_at_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('posted_at').verbose_name
        self.assertEquals(field_label, 'posted at')

    def test_created_by_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created_by').verbose_name
        self.assertEquals(field_label, 'created by')

    def test_status_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_image_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')

    def test_name_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_type_of_object_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('type_of_object').max_length
        self.assertEquals(max_length, 200)

    def test_description_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_location_found_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('location_found').max_length
        self.assertEquals(max_length, 300)

    def test_pickup_details_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('pickup_details').max_length
        self.assertEquals(max_length, 300)

    def test_status_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('status').max_length
        self.assertEquals(max_length, 12)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/lost/post/1/')
