import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Master
from ..serializers import UserSerializer
from landing.views import *
client = Client()


class GetAllMastersTest(TestCase):
    def setUp(self):
        Master.objects.create(name='Паша',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=True)
        Master.objects.create(name='Артём',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=False)
        Master.objects.create(name='Миша',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=False)

    def test_get_all_masters(self):
        response = client.get(reverse('master-list'))
        masters = Master.objects.all()
        serializer = UserSerializer(masters, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewMasterTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Святослав',
            'position' : 'frgesthr',
            'descriptions': 'Старший мастер. Опыт 5 лет.',
            'date': '2020-01-17T15:02:00'
        }
        self.invalid_payload = {
            'name': 'Егор',
            'position' : 'frgesthr',
            'descriptions': 'Старший мастер. Опыт 5 лет.',
            'date': 'опыт'
        }

    def test_create_valid_single_master(self):
        response = client.post(reverse('master-list'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_master(self):
        response = client.post(reverse('master-list'),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateMasterTest(TestCase):
    """ Test module for updating an existing post record """
    def setUp(self):
        self.master = Master.objects.create(name='Вадим', position='Старший', date = '2020-01-17T15:02:00', descriptions= "bdtfjngh", is_male=False)

        self.valid_payload = {
            'name': 'Артём',
            'position': 'Старший мастер. Опыт 5 лет.',
            'date': '2020-01-17T15:02:00',
            'descriptions' : 'frsde',
            'is_male' : True
        }
        self.invalid_payload = {
            'name': '',
            'position': None,
            'date': '2020-01-17T15:02:00',
            'descriptions' : None,
            'is_male' : None
        }

    def test_valid_update_Master(self):
        response = client.put(reverse('master-detail',
                                      kwargs={'pk': self.master.pk}),
                              data=json.dumps(self.valid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_Master(self):
        response = client.put(reverse('master-detail',
                                      kwargs={'pk': self.master.pk}),
                              data=json.dumps(self.invalid_payload),
                              content_type='application/json')
        # self.assertEqual(len(response.data), 1)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleMasterTest(TestCase):
    def setUp(self):
        self.master = Master.objects.create(name='Вадим', position='Старший', date = '2020-01-17T15:02:00', descriptions= "bdtfjngh", is_male=False)

    def test_valid_delete_master(self):
        response = client.delete(
            reverse('master-detail', kwargs={'pk': self.master.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_master(self):
        response = client.delete(reverse('master-detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
