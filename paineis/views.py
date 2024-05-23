from django.views.generic import TemplateView



class Home(TemplateView):
    template_name = 'paineis/index.html'
    
    
class Index(TemplateView):
    template_name = 'paineis/index2.html'
 
 
