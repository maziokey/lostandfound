from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, resolve
from django.test import TestCase
from django.views.generic import RedirectView
from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile

from ..views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from ..models import Post
from ..forms import PostForm


class PostDetailTests(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.post = Post.objects.create(name='Police badge', type_of_object='badge', description='A police badge belonging to sergent rogers', location_found='inside a bus', pickup_details='Holy rosary church, agbakpa.', posted_at = date.today(), created_by=self.user, status='AVAILABLE', image='/home/okey/Pictures/badge.jpg')

    def test_post_detail_view_success_status_code(self):
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_post_detail_view_not_found_status_code(self):
        url = reverse('post_detail', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_post_detail_url_resolves_post_detail_view(self):
        view = resolve('/lost/post/1/')
        self.assertEquals(view.func.view_class, PostDetailView)

    def test_post_detail_view_contains_link_back_to_homepage(self):
        post_detail_url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(post_detail_url)
        homepage_url = reverse('posts')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
