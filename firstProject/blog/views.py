from django.shortcuts import render




def home(request):
    context = {'posts': posts}
    return render(request, 'blog/initial.html', context)