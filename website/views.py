from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#erp_page,contact_page,register_page,events_page,projects_page,results_page

def home_page(request):
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)

'''
def erp_page(request):
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)

def family_page(request):
    t = get_template('navbar.html')
    html = t.render(Context())
    return HttpResponse(html)

def admissions_page(request):
    t = get_template('main.html')
    html = t.render(Context())
    return HttpResponse(html)

def events_page(request):
    t = get_template('carousel.html')
    html = t.render(Context())
    return HttpResponse(html)

'''
