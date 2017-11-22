from django.db import models

# Create your models here.
class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('Data de Publicação')
class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta)
    respota_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)