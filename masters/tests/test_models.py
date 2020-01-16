from django.test import TestCase
from ..models import *

class MasterTest(TestCase):
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
    #Проверка на тип парикмахера - муж/жен
    def test_men_or_women(self):
        master_m = Master.objects.get(name='Паша')
        self.assertEqual(master_m.is_male, True)
        masters = Master.men.all()
        self.assertEqual(masters.count(), 1)

    # def test__update(self):
    #     master = Master.objects.get(price=1000)
    #     room.price=5000
    #     self.assertEqual(room.is_premium, True)