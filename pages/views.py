from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about-us.html")


def gallery(request):
    return render(request, "gallery.html")


def page_404(request):
    return render(request, "404.html")


def booking_info(request):
    return render(request, "booking-information.html")


def personal_info(request):
    return render(request, "personal-information.html")


def payment_info(request):
    return render(request, "payment-information.html")


def booking_done(request):
    return render(request, "booking-done.html")


def room_booking(request):
    return render(request, "room-booking.html")


def news(request):
    return render(request, "news.html")


def staff(request):
    return render(request, "staff.html")


def our_room(request):
    return render(request, "our-room.html")


def contact(request):
    return render(request, "contact-us.html")
