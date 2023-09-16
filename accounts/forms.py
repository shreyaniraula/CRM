from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        # Which model we build the form for
        model = Order
        # What fields to allow
        fields = '__all__'