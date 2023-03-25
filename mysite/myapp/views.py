from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm

def message_list(request):
    messages = Message.objects.order_by('-timestamp')
    form = MessageForm()
    return render(request, 'myapp/message_list.html', {'messages': messages, 'form': form})

def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('message_list')

def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('message_list')
