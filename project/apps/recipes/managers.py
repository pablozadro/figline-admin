from django.db.models import Manager

class RecipeManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('category').defer('detail','steps')

    def list(self):
        return self.get_queryset().all().order_by('category')

    def detail(self, id):
        return self.get(id=id)