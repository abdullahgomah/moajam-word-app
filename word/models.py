from django.db import models

# Create your models here.
class Word(models.Model):

    word = models.CharField(verbose_name="الكلمة", max_length=255)
    meaning = models.CharField(verbose_name="المعنى", max_length=255)

    class Meta:
        verbose_name = 'كلمة'
        verbose_name_plural = "الكلمات"

    def __str__(self):
        return str(self.word) 
