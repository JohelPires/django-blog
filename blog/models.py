from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    slug = models.SlugField()
    intro = models.TextField()

    class Meta:
        ordering = ['-publicado_em']

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['publicado_em']