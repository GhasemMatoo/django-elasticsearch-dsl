from django.shortcuts import render
from django.views import View
from elastics.forms import BookSearchForm
from elastics.documents import BookDocument
from elastics.models import Book

# Create your views here.


class BookSearchView(View):
    form_class = BookSearchForm
    template_name = "elastics/home.html"

    def get(self, request, *args, **kwargs):
        results = {}
        if request.GET.get("search"):
            results = BookDocument.search().query('match', name=request.GET['search'])
        return render(
            request, template_name=self.template_name, context={"form": self.form_class, 'results': results})


class BookDitail(View):
    template_name = "elastics/index.html"

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get('book_id'))
        return render(request, template_name=self.template_name, context={"book": book})
