from django.test import TestCase
from ..models import *

class MasterTest(TestCase):
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
    #Проверка на тип парикмахера - муж/жен
    def test_men_or_women(self):
        master_m = Master.objects.get(name='Паша')
        self.assertEqual(master_m.is_male, True)
        masters = Master.men.all()
        self.assertEqual(masters.count(), 1)

    def test_men_or_women_filtering(self):
        masters= Master.men.all()
        self.assertEqual(masters.count(), 1)
