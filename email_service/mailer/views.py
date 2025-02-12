from django.shortcuts import render
from django.http import JsonResponse
from .forms import MailingForm

def create_mailing(request):
    if request.method == 'POST' and request.is_ajax():
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save()
            return JsonResponse({'success': True, 'mailing_id': mailing.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})