from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory, Tag

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        queryset = Article.objects.filter(is_published=True).select_related('category').prefetch_related('tags')
        category_slug = self.request.GET.get('category')
        tag_slug = self.request.GET.get('tag')

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        context['tags'] = Tag.objects.all()
        context['active_category'] = self.request.GET.get('category', '')
        context['active_tag'] = self.request.GET.get('tag', '')
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category').prefetch_related('tags', 'related_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(
            is_published=True
        ).exclude(id=self.object.id).order_by('-is_featured', '?')[:3]
        return context
