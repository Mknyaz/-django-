import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Master
from ..serializers import UserSerializer

client = Client()


class GetAllRoomsTest(TestCase):
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
