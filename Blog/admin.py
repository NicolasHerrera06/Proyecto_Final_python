from django.contrib import admin
from .models import Posteo, Contacto

class PoseoAdmin(admin.ModelAdmin):
    #muestra el titulo, el autor y la fecha
    list_display = ["titulo", "autor","fecha"]
    #crea un busqueda por autor
    search_fields = ["autor"]
    #crea un filtro por autor y por fecha
    list_filter = ["autor","fecha"]
    #lista post por pagina
    list_per_page = 5 


admin.site.register(Posteo,PoseoAdmin)
admin.site.register(Contacto)


