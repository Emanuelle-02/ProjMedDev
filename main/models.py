from django.db import models

# Create your models here.
CLASSES_CHOICES = [
        ('EM ANDAMENTO', 'EM ANDAMENTO'),
        ('ENTREGUE', 'ENTREGUE'),
        ('CANCELADA', 'CANCELADA'),
    ]

class Cidade(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Farmacia(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    cnpj = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Entregador(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
            return self.nome

class Entregas(models.Model):
    medicamento = models.CharField(max_length=150)
    Farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE)
    destinatario = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    status = models.CharField(max_length=150,choices=CLASSES_CHOICES)