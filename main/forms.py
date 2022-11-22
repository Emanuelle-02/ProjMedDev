from django.forms import ModelForm
from .models import Entregador, Entregas, Farmacia

class EntregadorForm(ModelForm):
    class Meta:
        model = Entregador
        fields = '__all__'

class FarmaciaForm(ModelForm):
    class Meta:
        model = Farmacia
        fields = '__all__'

class EntregaForm(ModelForm):
    class Meta:
        model = Entregas
        fields = '__all__'