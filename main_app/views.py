from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import (
    PatientTestimonial, Appointment, ServiceRequest,
    BlogPost, Facility, Branch, ContactMessage
)


def home(request):
    try:
        testimonials = PatientTestimonial.objects.all()[:6]
    except Exception:
        testimonials = []
    context = {
        'testimonials': testimonials,
        'page': 'home',
    }
    return render(request, 'main_app/home.html', context)


def services(request):
    context = {'page': 'services'}
    return render(request, 'main_app/services.html', context)


def facilities(request):
    try:
        facilities_list = Facility.objects.all()
    except Exception:
        facilities_list = []
    context = {
        'facilities': facilities_list,
        'page': 'facilities',
    }
    return render(request, 'main_app/facilities.html', context)


def patient_care(request):
    insurers = [
        'NHIF',
        'AAR Healthcare',
        'Jubilee Insurance',
        'UAP Old Mutual',
        'Britam',
        'Madison Insurance',
        'Resolution Health',
        'CIC Insurance',
        'APA Insurance',
        'Minet Kenya'
    ]
    context = {
        'page': 'patient_care',
        'insurers': insurers,
    }
    return render(request, 'main_app/patient_care.html', context)


def booking(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'appointment':
            try:
                Appointment.objects.create(
                    name=request.POST.get('name'),
                    phone=request.POST.get('phone'),
                    email=request.POST.get('email'),
                    location=request.POST.get('location'),
                    service=request.POST.get('service'),
                    preferred_date=request.POST.get('preferred_date'),
                    preferred_time=request.POST.get('preferred_time'),
                    notes=request.POST.get('notes', ''),
                )
                messages.success(request, 'Appointment booked successfully! We will contact you shortly.')
            except Exception as e:
                messages.error(request, f'Error booking appointment: {str(e)}')

        elif form_type == 'service_request':
            try:
                ServiceRequest.objects.create(
                    request_type=request.POST.get('request_type'),
                    name=request.POST.get('name'),
                    phone=request.POST.get('phone'),
                    email=request.POST.get('email'),
                    location=request.POST.get('location'),
                    details=request.POST.get('details'),
                    preferred_date=request.POST.get('preferred_date'),
                    preferred_time=request.POST.get('preferred_time'),
                )
                messages.success(request, 'Service request submitted successfully! Our team will be in touch.')
            except Exception as e:
                messages.error(request, f'Error submitting request: {str(e)}')

        return redirect('booking')

    context = {'page': 'booking'}
    return render(request, 'main_app/booking.html', context)


def blog(request):
    try:
        posts = BlogPost.objects.filter(is_published=True).order_by('-date')
    except Exception:
        posts = []
    context = {
        'posts': posts,
        'page': 'blog',
    }
    return render(request, 'main_app/blog.html', context)


def blog_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk, is_published=True)
        recent_posts = BlogPost.objects.filter(is_published=True).exclude(pk=pk).order_by('-date')[:3]
    except (BlogPost.DoesNotExist, Exception):
        return redirect('blog')
    context = {
        'post': post,
        'recent_posts': recent_posts,
        'page': 'blog',
    }
    return render(request, 'main_app/blog_detail.html', context)


def contact(request):
    branches = Branch.objects.all()
    if request.method == 'POST':
        try:
            ContactMessage.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone', ''),
                subject=request.POST.get('subject'),
                message=request.POST.get('message'),
            )
            messages.success(request, 'Message sent successfully! We will respond within 24 hours.')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')
        return redirect('contact')

    context = {
        'branches': branches,
        'page': 'contact',
    }
    return render(request, 'main_app/contact.html', context)


@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').lower()
            response = get_chat_response(user_message)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'response': 'I apologize, I encountered an error. Please try again or call us directly.'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


def get_chat_response(message):
    """Simple rule-based chat responses."""
    responses = {
        'malaria': "Malaria symptoms include fever, chills, headache, and muscle aches. Please visit our clinic for proper diagnosis and treatment. Early treatment is essential! Call us: +254 700 123 456.",
        'appointment': "To book an appointment, click the 'Book Appointment' button on our website or call +254 700 123 456. We're open 24 hours.",
        'hours': "Dawafront Healthcare is open 24 hours a day, 7 days a week including public holidays.",
        'location': "Our main clinic is in Kisumu, Kondele Ward, Kisumu Central. We also have a branch in Homa Bay. Call +254 700 123 456 for exact directions.",
        'emergency': "For emergencies, call +254 700 123 456 immediately or come directly to our emergency department. We are available 24/7.",
        'maternity': "Our maternity ward offers antenatal care, safe delivery services, and postnatal care. Book a consultation today at +254 700 123 456.",
        'insurance': "We accept various insurance schemes including NHIF, AAR, Jubilee, and others. Contact us to confirm your specific plan.",
        'covid': "For COVID-19 concerns, we offer testing and treatment. Please call ahead so we can prepare appropriate isolation measures.",
        'flu': "Common cold/flu symptoms include runny nose, sore throat, fever, and fatigue. Stay hydrated, rest well. If symptoms worsen, visit our clinic.",
        'diabetes': "Diabetes management requires regular blood sugar monitoring, proper diet, exercise, and medication. Our doctors can help create your personalized care plan.",
        'blood pressure': "High blood pressure is often asymptomatic. Regular check-ups are important. Reduce salt intake, exercise regularly, and take prescribed medication.",
        'pharmacy': "Our pharmacy is stocked with a wide range of medications. We also offer drug delivery services. Call +254 700 123 456 to order.",
        'pediatric': "Our pediatric department handles all children's health needs from newborns to teenagers. Book an appointment for your child today.",
        'surgery': "We have a modern surgical theater for various procedures. All surgeries are performed by qualified surgeons. Call us for a consultation.",
        'laboratory': "Our laboratory offers comprehensive tests including blood work, urine analysis, and more. Results are usually ready within 24 hours.",
    }

    for keyword, response in responses.items():
        if keyword in message:
            return response

    if any(word in message for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return "Hello! Welcome to Dawafront Healthcare. I'm your virtual health assistant. How can I help you today? You can ask me about symptoms, services, appointments, or our facilities."

    if any(word in message for word in ['thank', 'thanks', 'bye', 'goodbye']):
        return "Thank you for reaching out to Dawafront Healthcare. Stay healthy! For urgent matters, please call +254 700 123 456."

    return "I understand you have a health concern. For accurate medical advice, please consult one of our qualified doctors. You can book an appointment online or call +254 700 123 456. Remember: this chat is for general information only and does not replace professional medical advice. 🏥"
