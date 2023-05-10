from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    TYPE_CHOICES = (
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='type1')

    def __str__(self):
        return self.username
    
    
class ToDoList(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, verbose_name="Yapılacaklar")
    creatingDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    deleteDate = models.DateField(null=True, blank=True, auto_now_add=False)
    completedPercent = models.PositiveIntegerField(blank=True, null=True, verbose_name="Tamamlanma Yüzdesi")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "To Do Listesi"


class ToDoStep(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='steps', verbose_name="To Do Listesi")
    creationDate = models.DateField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updateDate = models.DateField(auto_now=True, verbose_name="Güncelleme Tarihi")
    deleteDate = models.DateField(auto_now_add=True, verbose_name="Silme Tarihi")
    content = models.TextField(verbose_name="İçerik")
    isCompleted = models.BooleanField(default=False, verbose_name="Bitirilme Durumu")
     

    class Meta:
        verbose_name_plural = "To Do Adımı"
    
