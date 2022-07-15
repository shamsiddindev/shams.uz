from django.shortcuts import render


def layouts_base(request):
    return render(request, 'layouts/base.html')
