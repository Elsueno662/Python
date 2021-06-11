from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib import messages
from .models import Book
from .forms import BookForm


def add(request):
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Book Added Successfully!')

    context['form'] = form
    return render(request, 'add.html', context)


def display(request):
    context = {}

    context["dataset"] = Book.objects.all()
    return render(request, "display.html", context)


def update(request, id):
    context = {}
    obj = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Book Updated Successfully!')
        return HttpResponseRedirect('/')

    context["book"] = obj
    return render(request, "update.html", context)


def delete(request, id):
    context = {}
    obj = get_object_or_404(Book, id=id)
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.SUCCESS, 'Book Deleted Successfully!')
        return HttpResponseRedirect("/")
    context["dataset"] = obj
    return render(request, "delete.html", context)
