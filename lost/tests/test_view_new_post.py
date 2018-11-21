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

#image simulation after importing SimpleUploadedFile
small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


class NewPostTests(TestCase):
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_new_post_view_success_status_code(self):
        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_post_url_resolves_new_post_view(self):
        view = resolve('/lost/post/create/')
        self.assertEquals(view.func.view_class, PostCreateView)

    def test_new_post_view_contains_link_back_to_posts(self):
        new_post_url = reverse('post_create')
        posts_url = reverse('posts')
        response = self.client.get(new_post_url)
        self.assertContains(response, 'href="{0}"'.format(posts_url))

    def test_csrf(self):
        url = reverse('post_create')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_post_valid_post_data(self):
        url = reverse('post_create')
        data = {
            'name': 'Mopol Badge',
            'type_of_object': 'badge',
            'description': 'A mopol badge belonging to sergent rogers',
            'location_found': 'inside a bus',
            'pickup_details': 'Holy rosary church, agbakpa.',
            'posted_at': date.today(),
            'status': 'AVAILABLE',
            'image': SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        }
        response = self.client.post(url, data)
        self.assertTrue(Post.objects.exists())

    def test_new_post_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('post_create')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_post_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('post_create')
        data = {
            'name': '',
            'type_of_object': '',
            'description': '',
            'location_found': '',
            'pickup_details': '',
            'posted_at': '',
            'status': '',
            'image': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Post.objects.exists())

    def test_contains_form(self):
        url = reverse('post_create')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, PostForm)

class LoginRequiredNewPostTests(TestCase):
    def setUp(self):
        self.url = reverse('post_create')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
