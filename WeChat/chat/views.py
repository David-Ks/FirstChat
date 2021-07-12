from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.db.models import Max
from .models import *
from .forms import *


class MyChat(CreateView):
	template_name = 'chat.html'
	form_class = ChatForm
	success_url = reverse_lazy('chat')

	def get_context_data(self, **kwargs):
		last = ChatModel.objects.all().aggregate(Max('pk'))
		last=last['pk__max']
		kwargs['items'] = ChatModel.objects.filter(pk__gt=last-6)
		return super(MyChat, self).get_context_data(**kwargs)


class MailSender(FormView):
	form_class = MailForm
	template_name = 'msender.html'
	success_url = reverse_lazy('msender')