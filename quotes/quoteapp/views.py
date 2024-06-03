from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author, Quote
from .connect import db


from django.shortcuts import render, redirect, get_object_or_404

# db = client.test

def main(request, page=1):
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quote_per_page = paginator.page(page)
    return render(request, 'quoteapp/index.html', context={'quotes': quote_per_page})

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:root')
        else:
            return render(request, 'quoteapp/new_tag.html', {'form': form})

    return render(request, 'quoteapp/new_tag.html', {'form': TagForm()})

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:root')
        else:
            return render(request, 'quoteapp/new_author.html', {'form': form})

    return render(request, 'quoteapp/new_author.html', {'form': AuthorForm()})

def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            
            a = Author.objects.filter(fullname__in=request.POST.getlist('author'))
            new_quote.author = a[0]
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            return redirect(to='quoteapp:root')
        else:
            return render(request, 'quoteapp/new_quote.html', {"tags": tags, "authors": authors,'form': form})

    return render(request, 'quoteapp/new_quote.html', {"tags": tags, "authors": authors,'form': QuoteForm()})


def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/detail.html', {"author": author})

def tags(request, tag_id):
    quotes = Quote.objects.filter(tags__pk=tag_id)
    print(quotes)
    return render(request, 'quoteapp/quotes.html', {"quotes": quotes})
