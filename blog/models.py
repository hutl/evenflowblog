from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    pub_date = models.DateTimeField('Data da publicação',default=now)
    imagem = models.ImageField(upload_to='uploads/',default="")

class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    com_date = models.DateTimeField('Data do comentário',default=now)
    nome = models.CharField(max_length=100, default="")