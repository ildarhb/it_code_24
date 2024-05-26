from django.test import TestCase, Client
from core.models import Post, Category



# class Tests(TestCase):
#     def SetUp(self):
#         self.client = Client()
#         self.category = Category.objects.create(
#             title = "Тестовая категория"
#         )
#         self.post = Post.objects.create(
#             title = 'Тестовое Статья',
#             body = 'Тестовое содержание',
#             likes = 42,
#             category = self.category,
#         )
    
#     def test_index(self):
#         response = self.client.get('')
#         self.assertAlmostEquals(response.status_code, 200)

#     def test_list_post(self):
#         response = self.client.get(f'/posts')
#         self.assertAlmostEquals(response.status_code, 200)

#     def test_detail_post(self):
#         response = self.client.get(f'/post/{self.post.pk}/')
#         self.assertAlmostEquals(response.status_code, 200)

class TestsViewSets(TestCase):
    def setUp(self):
        self.data = {
            "title": "добавленный",
            "body": "текст первой статьи",
            "status": "DF",
            "likes": 15,
            "date": "2024-05-07",
            "category": 2
        }
    def test_list(self):
        response = self.client.get(f'/posts_set/')
        self.assertAlmostEquals(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/posts_set/2/')
        self.assertAlmostEquals(response.status_code, 200)
    
    def test_create(self):
        response = self.client.post(f'/posts_set/', data=self.data, format='json')
        self.assertAlmostEquals(response.status_code, 201)
    
    def test_update(self):
        response = self.client.get(f'/posts_set/2/')
        self.assertAlmostEquals(response.status_code, 201)

    def test_partial_update(self):
        response = self.client.put(f'/posts_set/2/')
        self.assertAlmostEquals(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete(f'/posts_set/3/')
        self.assertAlmostEquals(response.status_code, 204)