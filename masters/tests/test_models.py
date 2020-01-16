from django.test import TestCase
from ..models import Master


class MasterTest(TestCase):
     def setUp(self):
        Master.objects.create(name='Миша',
                            description='Старший мастер. Опыт 5 лет.', position='Старший',
                            category='Муж', haircut='Ёжик')
        Master.objects.create(name='Артём',
                            description='Старший мастер. Опыт 5 лет.', position='Старший',
                            category='Муж', haircut='Ёжик')
        Master.objects.create(name='Миша',
                            description='Старший мастер. Опыт 5 лет.', position='Старший',
                            category='Жен', haircut='Ёжик')

    def test_men_or_women(self):
        master = Master.objects.get(master='Вадим Немков')
        self.assertEqual(Master.is_male, True)
        masters = Master.masters_men.all()
        self.assertEqual(Masters.count(), 1)
