from django.db import models

# Create your models here.

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))
# dangerは、list.htmlの表示色（bootstrap）
# 右側の値は、選択肢の値

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        )

    duedate = models.DateField()

    def __str__(self):
        return self.title