import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Master
from ..serializers import UserSerializer

client = Client()


class GetAllMastersTest(TestCase):
    def setUp(self):
        Master.objects.create(name='Паша',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=True, haircut='Ёжик')
        Master.objects.create(name='Артём',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=False, haircut='Модная')
        Master.objects.create(name='Миша',
                            descriptions='Старший мастер. Опыт 5 лет.', position='Старший',
                            is_male=False, haircut='Стильная')

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
            'descriptions': 'Старший мастер. Опыт 5 лет.',
            'date': '2020-01-17T15:02:00'
        }
        self.invalid_payload = {
            'name': 'Егор',
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
        self.master = Master.objects.create(name='Вадим', position='Старший', date = '2020-01-17T15:02:00')

        self.valid_payload = {
            'name': 'Артём',
            'position': 'Старший мастер. Опыт 5 лет.',
            'date': '2020-01-17T15:02:00'
        }
        self.invalid_payload = {
            'name': '',
            'position': 'Старший мастер. Опыт 5 лет.',
            'date': ''
        }

    def test_valid_update_Master(self):
        response = client.put(reverse('master',
                                      kwargs={'pk': self.master.pk}),
                              data=json.dumps(self.valid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_Master(self):
        response = client.put(reverse('master',
                                      kwargs={'pk': self.master.pk}),
                              data=json.dumps(self.invalid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
