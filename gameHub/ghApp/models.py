from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class userInfo(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    accountUsername = models.ForeignKey(Account,
        on_delete = models.CASCADE,
        default = None
    )
