from skvapp.models import BannerSlider

def get_banner_slider(request):
    banners = BannerSlider.objects.all().filter(is_active=True).order_by('order')
    banner_context = {
        'banners': banners,
    }
    return banner_context