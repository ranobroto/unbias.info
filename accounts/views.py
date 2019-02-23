from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#def SignUp(request):
 #   if request.method == 'POST':
  #      f = UserCreationForm(request.POST)
   #     if f.is_valid():
    #        f.save()
     #       messages.success(request, 'Account created successfully')
      #      return redirect('register')

#    else:
 #       f = UserCreationForm()

  #  return render(request, 'accounts/signup.html', {'form': f})