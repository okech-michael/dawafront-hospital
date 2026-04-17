from django.contrib import admin
from .models import PatientTestimonial, Appointment, ServiceRequest, BlogPost, Facility, Branch, ContactMessage


@admin.register(PatientTestimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'created_at']
    list_filter = ['rating']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'preferred_date', 'preferred_time', 'phone', 'created_at']
    list_filter = ['service', 'preferred_date']
    search_fields = ['name', 'phone', 'email']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'request_type', 'preferred_date', 'phone', 'created_at']
    list_filter = ['request_type']
    search_fields = ['name', 'phone', 'email']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'date', 'is_published']
    list_filter = ['category', 'is_published']
    search_fields = ['title', 'content']


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']
    search_fields = ['name']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone', 'is_main']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
