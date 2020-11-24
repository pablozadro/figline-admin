from django.db.models import Manager

class IngredientManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('category').defer('detail')

    def list(self):
        return self.get_queryset().all().order_by('title')

    def detail(self, id):
        return self.get(id=id)