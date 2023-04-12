from django.db import models


class Level(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level


class Theme(models.Model):
    theme = models.CharField(max_length=50)

    def __str__(self):
        return self.theme


class Question(models.Model):
    level = models.ForeignKey(Level, null=True, on_delete=models.DO_NOTHING)
    text = models.TextField(unique=True)
    theme = models.ForeignKey(Theme, null=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
