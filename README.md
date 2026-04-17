# Dawafront Healthcare Clinic — Website

A full-service hospital website built with Django + SQLite for Dawafront Healthcare Clinic, Kisumu, Kenya.

---

## 🏥 About

Dawafront Healthcare Clinic is a Level 3 Medical Facility located at Lolwe Shopping Centre, Kisumu Central, Kenya.  
This website provides a full patient-facing portal with appointments, service requests, blog, and an AI health assistant.

**Website built by TerraSept Solutions PLC, Kisii Kwanza Place, Third Floor.**

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Django 4.2
- **Database:** SQLite (included)
- **Frontend:** HTML5, CSS3 (custom), Vanilla JavaScript
- **Icons:** Font Awesome 6
- **Fonts:** Playfair Display, Source Sans 3 (Google Fonts)

---

## 📁 Project Structure

```
project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── hospital_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main_app/
    ├── models.py          # All database models
    ├── views.py           # All page views + chat API
    ├── urls.py            # URL routing
    ├── admin.py           # Admin panel configuration
    ├── migrations/        # Database migrations
    ├── templates/
    │   └── main_app/
    │       ├── base.html          # Base layout (navbar, footer, chat)
    │       ├── home.html          # Landing page with carousel
    │       ├── services.html      # Full services listing
    │       ├── facilities.html    # Facilities with capacity info
    │       ├── patient_care.html  # Patient journey steps
    │       ├── booking.html       # Appointment + request forms
    │       ├── blog.html          # Blog listing
    │       ├── blog_detail.html   # Single blog post
    │       └── contact.html       # Contact form + map + branches
    └── static/
        ├── css/
        │   └── style.css          # Complete custom CSS
        └── js/
            └── main.js            # Carousel, chat, tabs, animations
```

---

## ⚙️ Setup Instructions

### 1. Clone / Extract the Project

```bash
cd project
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files (for production)

```bash
python manage.py collectstatic
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**  
Admin Panel: **http://127.0.0.1:8000/admin/**

---

## 📄 Pages

| URL | Page |
|---|---|
| `/` | Home (Carousel, Services, Testimonials) |
| `/services/` | All Medical Services |
| `/facilities/` | Hospital Facilities |
| `/patient-care/` | Patient Journey & Rights |
| `/booking/` | Book Appointment / Request / Drug Order |
| `/blog/` | Health Articles |
| `/blog/<id>/` | Single Blog Post |
| `/contact/` | Contact Form + Map + Branches |
| `/admin/` | Django Admin Panel |
| `/api/chat/` | Chat Bot API (POST) |

---

## 🤖 AI Chat Assistant

The floating chat button activates a rule-based health assistant that answers questions about:
- Malaria, diabetes, hypertension, flu, COVID-19
- Appointments and clinic hours
- Maternity, pediatrics, pharmacy services
- Location and emergency contacts

To connect to an actual AI API (e.g., OpenAI or Claude), replace the `get_chat_response()` function in `views.py`.

---

## 🗄️ Database Models

| Model | Description |
|---|---|
| `PatientTestimonial` | Patient reviews shown on homepage |
| `Appointment` | Booked appointments |
| `ServiceRequest` | Doctor/nurse/drug delivery requests |
| `BlogPost` | Health articles |
| `Facility` | Hospital facilities with capacity |
| `Branch` | Clinic branches (Main + Homa Bay) |
| `ContactMessage` | Contact form submissions |

---

## 🎨 Design

- **Color Scheme:** Deep Navy Blue (#0a4a8c) + Soft Teal (#00a896) + White
- **Typography:** Playfair Display (headings) + Source Sans 3 (body)
- **Fully Responsive:** Mobile, tablet, and desktop
- **Smooth animations:** Scroll-triggered fade-ins, hover effects, carousel transitions

---

## 📞 Clinic Contact

- **Phone:** +254 700 123 456
- **Email:** info@dawafront.co.ke
- **Address:** Lolwe Shopping Centre, 50m from Lolwe Main Gate, next to Joymat Supermarket, Kisumu
- **Registration:** No. 020978 | License: 620589
- **Regulated by:** Pharmacy & Poisons Board

---

*Website built by TerraSept Solutions PLC, Kisii Kwanza Place, Third Floor.*
