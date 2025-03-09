from django.contrib import admin


class AdminUpdatedFields(admin.ModelAdmin):
    """Работать с update_fields из админ панели"""

    save_on_top = True
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            try:
                update_fields = form.changed_data
                obj.save(update_fields=update_fields)
            except ValueError:
                pass
