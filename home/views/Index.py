from django.shortcuts import render, redirect, get_object_or_404, render_to_response


# Index
def index(request):
    return render(request, 'home/index.html', {})
