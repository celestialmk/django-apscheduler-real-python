from django.test import TestCase
from django.utils import timezone
from .models import Episode
from django.urls.base import reverse

class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title='My Dope Podcast Episode',
            description='the very first episode',
            pub_date=timezone.now(),
            link='https://myawesomehow.com',
            image='https://image.myawesomehow.com',
            podcast_name='My Learning Podcast',
            guid='de194720-7b4c-49e2-a05f-432436d3fetr'
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, 'the very first episode')
        self.assertEqual(self.episode.link, 'https://myawesomehow.com')
        self.assertEqual(
            str(self.episode.guid), 'de194720-7b4c-49e2-a05f-432436d3fetr'
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), 'My Learning Podcast: My Dope Podcast Episode'
        )

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_home_page_list_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'My Dope Podcast Episode')

    
