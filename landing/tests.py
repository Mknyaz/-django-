from django.test import TestCase
from .views import *
from masters.models import Master


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
        self.assertEqual(Master.masters_men, True)
        masters = Master.masters_men.all()
        self.assertEqual(Masters.count(), 1)

# class SubscriberTest(TestCase):
#      def setUp(self):
#         Subscriber.objects.create(name='Миша', email='afwcrev@mail.ru',
#                             master='Вадим Немков',
#                             date='01.03.2021 18:00:35')
#         Subscriber.objects.create(name='Мишаy', email='afwtegrev@mail.ru',
#                             master='Святослав Романов',
#                             date='01.05.2021 18:00:00')
#         Subscriber.objects.create(name='Мишrа', email='afweacrev@mail.ru',
#                             master='Владимир Егоров',
#                             date='01.07.2021 18:00:00')
#
#     def test_men_or_women(self):
#         maste = Master.objects.get(master='Вадим Немков')
#         self.assertEqual(Master.masters_men, True)
#         masters = Master.masters_men.all()
#         self.assertEqual(Masters.count(), 1)
