from django import template

register = template.Library()


@register.filter
def horas_y_minutos(value):
    try:
        horas = int(value)
        minutos = int((value - horas) * 100)
        if minutos>=60:
            horas+=1
            minutos-=60
        
        if minutos!=0:
            return f"{horas}h {minutos}m"
        else:
            return f"{horas}h"
    except (ValueError, TypeError):
        return value
