from django.views import generic
from blog.models import Blog


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail_article.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
