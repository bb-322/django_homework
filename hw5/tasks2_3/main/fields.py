from django.forms import CharField, ValidationError

class AnyCharField(CharField):
    def clean(self, value:str):
        return value.strip()