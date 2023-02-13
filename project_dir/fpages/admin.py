# Импорт модуля администратора из пакета django.contrib
from django.contrib import admin

# Импорт класса FlatPageAdmin из приложения flatpages
from django.contrib.flatpages.admin import FlatPageAdmin

# Импорт модели FlatPage из приложения flatpages
from django.contrib.flatpages.models import FlatPage

# Ярлык для перевода строк в админке
from django.utils.translation import gettext_lazy as _


# Это подкласс класса FlatPageAdmin, который поставляется с Django.
class Permission(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Удаление FlatPageAdmin по умолчанию с сайта администратора.
admin.site.unregister(FlatPage)

# Регистрация модели FlatPage на сайте администратора.
admin.site.register(FlatPage, Permission)
