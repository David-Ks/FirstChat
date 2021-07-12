from django.contrib import admin
from .models import *

class ChatAdmin(admin.ModelAdmin):
	list_display = ('id', 'text', 'data', 'is_published')
	list_display_links = ('id',)
	list_editable = ('is_published',)
	search_fields = ('id', 'text', 'data')
	#list_filter = ('pr_type',)

admin.site.register(ChatModel, ChatAdmin)
