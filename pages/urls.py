from django.urls import path

from pages.views import index, about, gallery, page_404, booking_info, personal_info, payment_info, booking_done, \
    room_booking, news, staff, our_room, contact

app_name = "pages"

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("page_404/", page_404, name="page_404"),
    path("booking-info/", booking_info, name="booking-info"),
    path("personal-info/", personal_info, name="personal-info"),
    path("payment-info/", payment_info, name="payment-info"),
    path("booking-done/", booking_done, name="booking-done"),
    path("news/", news, name="news"),
    path("staff/", staff, name="staff"),
    path("our-room/", our_room, name="our-room"),
    path("contact/", contact, name="contact"),
    path("room-booking/", room_booking, name="room-booking"),
]
