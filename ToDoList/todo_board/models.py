from django.db import models
from django.db.models import Max


# Create your models here.


class ProjectCode(models.Model):
    pcode = models.CharField(primary_key=True, max_length=4)
    pname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_code'


class TodoList(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    is_complete = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def todo_save(self):
        self.is_complete = 0
        if TodoList.objects.all().aggregate(Max('priority'))['priority__max'] is None : self.priority = 1
        else : self.priority = int(TodoList.objects.latest('priority').priority) + 1
        self.pcode = 1
        self.user_id = 'guest'
        self.save()

    def todo_update_is_complete(self, complete):
        self.is_complete = complete
        self.save()

    class Meta:
        managed = False
        db_table = 'todo_list'
