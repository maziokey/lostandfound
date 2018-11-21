from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from datetime import date

from ..models import Post
from ..views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from ..forms import PostForm


class PostUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.post = Post.objects.create(name='Police badge', type_of_object='badge', description='A police badge belonging to sergent rogers', location_found='inside a bus', pickup_details='Holy rosary church, agbakpa.', posted_at = date.today(), created_by=user, status='AVAILABLE', image='/home/okey/Pictures/badge.jpg')
        self.url = reverse('post_update', kwargs={'pk': self.post.pk})

class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        '''
        Test if only logged in users can edit the posts
        '''
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        '''
        Create a new user different from the one who posted
        '''
        super().setUp()
        username = 'jane'
        password = '321'
        user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        '''
        A post should be edited only by the owner.
        Unauthorized users should get a 404 response (Page Not Found)
        '''
        self.assertEquals(self.response.status_code, 404)

class PostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/lost/post/1/update/')
        self.assertEquals(view.func.view_class, PostUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PostForm)

    def test_form_inputs(self):
        '''
        The view must contain six inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, '<textarea', 3)

'''
class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'description': 'edited description'})

    def test_redirection(self):

        A valid form submission should redirect the user

        post_detail_url = reverse('post_detail', kwargs={'pk': self.post.pk})
        self.assertRedirects(self.response, post_detail_url)

    def test_post_changed(self):
        self.post.refresh_from_db()
        self.assertEquals(self.post.description, 'edited description')
'''
