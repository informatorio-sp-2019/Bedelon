from django.contrib import admin
from reservas import models

# Register your models here.
class DocenteAdmin(admin.ModelAdmin):
	pass

class BedelAdmin(admin.ModelAdmin):
	pass

class AulaAdmin(admin.ModelAdmin):
	pass

class ReservaAdmin(admin.ModelAdmin):
	pass

class FeriadoAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Docente, DocenteAdmin)
admin.site.register(models.Bedel, BedelAdmin)
admin.site.register(models.Aula, AulaAdmin)
admin.site.register(models.Reserva, ReservaAdmin)
admin.site.register(models.Feriado, FeriadoAdmin)