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


class HomeTests(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.post = Post.objects.create(name='Police badge', type_of_object='badge', description='A police badge belonging to sergent rogers', location_found='inside a bus', pickup_details='Holy rosary church, agbakpa.', posted_at = date.today(), created_by=self.user, status='AVAILABLE', image='/home/okey/Pictures/badge.jpg')
        url = reverse('posts')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'lost/post_list.html')

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, RedirectView)

    def test_home_view_contains_navigation_links(self):
        post_detail_url = reverse('post_detail', kwargs={'pk': self.post.pk})
        post_create_url = reverse('post_create')

        self.assertContains(self.response, 'href="{0}"'.format(post_detail_url))
        self.assertContains(self.response, 'href="{0}"'.format(post_create_url))
