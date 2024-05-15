from django.views import generic
from portfolio.models import Post

class PostView(generic.View):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
