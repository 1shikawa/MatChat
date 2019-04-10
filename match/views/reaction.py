from django.shortcuts import loader
from django.http import HttpResponse

from match.forms.reaction import ReactionForm

def matching(request):
    form = ReactionForm(request.GET)
    form.load(request.user.id)
    context = {
        'form': form
    }
    template = loader.get_template('matching.html')
    return HttpResponse(template.render(context, request))