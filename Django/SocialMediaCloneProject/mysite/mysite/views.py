from django.views.generic import TemplateView

# Create yours views here!
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class Homepage(TemplateView):
    template_name = 'index.html'