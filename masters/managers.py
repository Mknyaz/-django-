from django.db.models import Manager, QuerySet


class MasterQuerySet(QuerySet):
    def Master_set(self):
        return self.all()


class MasterManager(Manager):
    def get_queryset(self):
        return MasterQuerySet(self.model, using=self._db)


class MasterMenManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_male=True)

class MasterWomenManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_male=False)
