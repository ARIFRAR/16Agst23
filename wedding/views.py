from django.shortcuts import render, get_object_or_404
from .models import Wedding
from django.core.paginator import Paginator

def weddingg(request):
    weddings = Wedding.objects.order_by('-created_date')
    paginator = Paginator(weddings, 4)
    page = request.GET.get('page')
    paged_weddings = paginator.get_page(page)

    data = {
        'weddings': paged_weddings,
    }
    return render(request, 'wedding/wedding.html', data)

def wedding_detail(request, id):
    weddingss = get_object_or_404(Wedding, id=id)
    # Lakukan operasi lainnya dan kembalikan responsenya
    data = {
        'weddingss': weddingss,
    }
    return render(request, 'wedding/wedding_detail.html', data)

def search(request):
    weddings = Wedding.objects.order_by('-created_date')
    music_sound_search = Wedding.objects.values_list('music_sound', flat=True).distinct()
    wedding_organizer_search = Wedding.objects.values_list('wedding_organizer', flat=True).distinct()
    durasi_acara_search = Wedding.objects.values_list('durasi_acara', flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            weddings = weddings.filter(description__icontains=keyword)

    # if 'music_sound' in request.GET:
    #     music_sound = request.GET['music_sound']
    # if music_sound:
    #     weddings = weddings.filter(music_sound__iexact=music_sound)


    if 'wedding_organizer' in request.GET:
        wedding_organizer = request.GET['wedding_organizer']
        if wedding_organizer:
            weddings = weddings.filter(wedding_organizer__iexact=wedding_organizer)

    if 'durasi_acara' in request.GET:
        durasi_acara = request.GET['durasi_acara']
        if durasi_acara:
            weddings = weddings.filter(durasi_acara__iexact=durasi_acara)


    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            weddings = weddings.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'weddings': weddings,
        'music_sound_search': music_sound_search,
        'wedding_organizer_search': wedding_organizer_search,
        'durasi_acara_search': durasi_acara_search,
       }
    return render(request, 'wedding/search.html', data)
# views.py
from django.shortcuts import render


def booking_view(request):
    # Logika untuk proses booking

    booking_done = True  # Ganti dengan logika yang sesuai untuk menentukan apakah booking telah selesai

    context = {
        'booking_done': booking_done
    }

    return render(request, 'wedding_detail.html', context)

