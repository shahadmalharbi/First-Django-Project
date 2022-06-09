from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
def redirected_method(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request,number):
    context = {"number": int(number)}
    return  render(request, "index.html", context)
def edit(request,number):
    context = {"number": int(number)}
    return  render(request, "edit.html", context)
def destroy(request,number):
    context = {"number": number}
    return  redirect("/blogs")
def json_file(request):
    return JsonResponse({
        "title": "My first blog",
        "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
    })