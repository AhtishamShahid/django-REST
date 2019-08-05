from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Post, Category, Comments
from django.utils.datetime_safe import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


def create_category(title):
    return Category.objects.create(title=title).id


class PostTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('posts')
        cats = [create_category('dasdas1'), create_category('dasdas2'), create_category('dasdas3')]

        data = {
            'title': 'DabApps',
            'description': 'this is a post',
            # 'post_image': SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4"),
            'category': cats,
            'pub_date': datetime.now()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'DabApps')
