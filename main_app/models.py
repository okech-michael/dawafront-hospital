from django.db import models


class PatientTestimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('outpatient', 'Outpatient Consultation'),
        ('inpatient', 'Inpatient Admission'),
        ('emergency', 'Emergency Services'),
        ('surgery', 'Surgery'),
        ('maternity', 'Maternity'),
        ('pediatrics', 'Pediatrics'),
        ('radiology', 'Radiology'),
        ('laboratory', 'Laboratory'),
        ('pharmacy', 'Pharmacy'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} on {self.preferred_date}"


class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('doctor', 'Request a Doctor'),
        ('nurse', 'Request a Nurse'),
        ('drug_delivery', 'Drug Delivery'),
    ]
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=300)
    details = models.TextField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.request_type} - {self.name}"


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('health_tips', 'General Health Tips'),
        ('disease_prevention', 'Disease Prevention'),
        ('nutrition', 'Nutrition'),
        ('maternal_health', 'Maternal Health'),
        ('child_health', 'Child Health'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='health_tips')
    author = models.CharField(max_length=100, default='Dawafront Medical Team')
    date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    capacity = models.IntegerField(default=10)
    icon = models.CharField(max_length=50, default='fa-hospital')

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    map_link = models.URLField(blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
