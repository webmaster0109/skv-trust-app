from django.shortcuts import render, get_object_or_404
from .models import SKVEventDetail, SKVNewsDetail, SKVHistory

# Create your views here.

def home(request):

    skv_event_detail = SKVEventDetail.objects.all().filter(is_active=True).order_by('-created_at')[:5]
    skv_news_detail = SKVNewsDetail.objects.all().filter(is_active=True).order_by('-created_at')[:6]
    skv_news_detail_count = skv_news_detail.count()

    context = {
        'skv_event_detail': skv_event_detail,
        'skv_news_detail': skv_news_detail,
        'skv_news_detail_count': skv_news_detail_count,
    }
    return render(request, template_name='pages/index.html', context=context)

def about(request):
    return render(request, template_name='pages/about.html')

def skv_history(request):
    skv_history = SKVHistory.objects.all().filter(is_active=True).order_by('order')
    context = {
        'skv_history': skv_history,
    }
    return render(request, template_name='pages/skv_history.html', context=context)

def skv_event_detail(request, slug):
    skv_event_detail = get_object_or_404(SKVEventDetail, slug=slug, is_active=True)
    context = {
        'skv_event_detail': skv_event_detail,
    }
    return render(request, template_name='pages/skv_event_detail.html', context=context)

def skv_news_detail(request, slug):
    skv_news_detail = get_object_or_404(SKVNewsDetail, slug=slug, is_active=True)
    context = {
        'skv_news_detail': skv_news_detail,
    }
    return render(request, template_name='news/news_detail.html', context=context)
