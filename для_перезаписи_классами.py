# Нужно для дальнейшей работы с классами и VIEW моделями
class Bloglist(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    model = Post
    template_name = 'about.html'


class SearchResultView(ListView):
    model = Post
    template_name = "search_result.html"

    def get_queryset(self):
        # object_list = self.model.objects.all()
        # print(object_list)
        name = self.request.POST.get("search", "")
        if name:
            object_list = Post.objects.filter(Q(title__icontains=name) | Q(body__icontains=name))
            return object_list
return Post.objects.filter(Q(title__icontains="с") | Q(body__icontains="с"))

class SearchResultView(ListView):
    model = Post
    template_name = "search_result.html"

    def get_queryset(self):
        object_list = self.model.objects.all()
        name = self.kwargs.get("search", "")
        if name:
            object_list = Post.objects.filter(Q(title__icontains=name) | Q(body__icontains=name))
        return object_list
        # return Post.objects.filter(Q(title__icontains="с") | Q(body__icontains="с"))