from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    # Return the last five published questions(not including those set to be published in the future).
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
   

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(LoginRequiredMixin,generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# class VoteView(generic.View):

#     def get_queryset(self, choice_id):
#         return Choice.objects.get(pk=choice_id)

#     def post(self, request, pk):
#         question_id = pk
#         choice_id = request.POST.get('choice', None)
#         try:
#             queryset = self.get_queryset(choice_id)
#         except (KeyError, Choice.DoesNotExist):
#             return redirect('polls:detail', pk=question_id)
#         else:
#             queryset.votes += 1
#             queryset.save()
#             return redirect('polls:vote_result', pk=question_id)

# class ResultsView(TemplateResponseMixin, generic.View):
#     template_name = 'polls/results.html'

#     def get_queryset(self, question_id):
#         return Question.objects.get(pk=question_id)

#     def get(self, request, pk):
#         queryset = self.get_queryset(pk)
#         context = {'question': queryset}
#         return self.render_to_response(context)


# class SwitchboardView(generic.View):
#     def get(self, request, pk):
#         view = ResultsView.as_view()
#         return view(request, pk)

#     def post(self, request, pk):
#         view = VoteView.as_view()
#         return view(request, pk)

