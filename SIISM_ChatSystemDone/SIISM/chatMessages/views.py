
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Q

from userena.utils import get_user_model, user_model_label

from .models import Message
from .forms import NewMessageForm

@login_required
def userList(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'chatMessages/chat_list.html', context)

@login_required
def chat(request, username):

    contactCollection = User.objects.filter(username = username)
    loggedInUserCollection = User.objects.filter(id = request.user.id)

    messages = Message.objects.filter(
    	( Q(sender = loggedInUserCollection) & Q(recipient = contactCollection) ) |
    	( Q(recipient = loggedInUserCollection) & Q(sender = contactCollection) )
    ).order_by('-timestamp')[:5]

    #messages = reversed(reversed_messages) #to display most recent messages at the bottom

    form = NewMessageForm(request.POST or None)

    args = {'messages':messages,
            'form': form,
    }

    contact = contactCollection[0]

    if request.POST:
    	if form.is_valid():
            instances = form.save(commit = False)
            instances.sender = request.user
            instances.recipient = contact
            instances.save()

            return render_to_response('chatMessages/chat_messages.html', args, context_instance = RequestContext(request))

    return render_to_response('chatMessages/chat_messages.html', args, context_instance = RequestContext(request))