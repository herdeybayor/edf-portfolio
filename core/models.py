from django.db import models

class Script(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    url = models.CharField(
        max_length=255, default=True)

    image = models.ImageField(
        upload_to='images/')

    def __str__(self):
        return self.name

    # Rest of the model code


class Website(models.Model):
    FM_TYPES = (
        ('DJANGO', 'DANGO FM'),
        ('FLASK', 'FLASK FM'),
        ('NODE.JS', 'NODE FM'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    fm_type = models.CharField(max_length=7, choices=FM_TYPES)
    url = models.CharField(
        max_length=255, default=True)


class API(models.Model):
    API_TYPES = (
        ('DRF', 'DJANGO REST API'),
        ('FAST', 'FAST API'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    api_type = models.CharField(max_length=4, choices=API_TYPES)
    url = models.CharField(
        max_length=255, default=True)

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    source = models.CharField(max_length=100)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
