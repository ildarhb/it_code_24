from django.test import TestCase, Client
from core.models import Post, Category



class Tests(TestCase):
    def SetUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            title = "Тестовая категория"
        )
        self.post = Post.objects.create(
            title = 'Тестовое Статья',
            body = 'Тестовое содержание',
            likes = 42,
            category = self.category,
        )
    
    def test_index(self):
        response = self.client.get('')
        self.assertAlmostEquals(response.status_code, 200)

    def test_list_post(self):
        response = self.client.get(f'/posts')
        self.assertAlmostEquals(response.status_code, 200)

    def test_detail_post(self):
        response = self.client.get(f'/post/{self.post.pk}/')
        self.assertAlmostEquals(response.status_code, 200)