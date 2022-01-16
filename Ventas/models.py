from django.db import models

# Create your models here.
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cita_id = models.IntegerField()
    total_pagar = models.FloatField()
    fecha_cita = models.DateTimeField()
    descricpion = models.TextField(blank=True, null=True)
    estado = models.IntegerField()   # This field type is a guess.

    class Meta:
        db_table = 'pedidos'
        verbose_name ='pedido'
        verbose_name_plural='pedidos'
