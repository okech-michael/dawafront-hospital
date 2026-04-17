// ===== NAVBAR SCROLL =====
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ===== HAMBURGER MENU =====
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const spans = hamburger.querySelectorAll('span');
    spans[0].style.transform = navLinks.classList.contains('open') ? 'rotate(45deg) translate(5px, 5px)' : '';
    spans[1].style.opacity = navLinks.classList.contains('open') ? '0' : '1';
    spans[2].style.transform = navLinks.classList.contains('open') ? 'rotate(-45deg) translate(5px, -5px)' : '';
  });
}

// ===== HERO CAROUSEL =====
const carouselSlides = document.querySelector('.carousel-slides');
const dots = document.querySelectorAll('.carousel-dot');
const prevBtn = document.querySelector('.carousel-prev');
const nextBtn = document.querySelector('.carousel-next');
let currentSlide = 0;
let autoplayInterval;

function goToSlide(index) {
  currentSlide = (index + 3) % 3;
  if (carouselSlides) {
    carouselSlides.style.transform = `translateX(-${currentSlide * 100}%)`;
  }
  dots.forEach((d, i) => d.classList.toggle('active', i === currentSlide));
}

function startAutoplay() {
  autoplayInterval = setInterval(() => goToSlide(currentSlide + 1), 5000);
}

function stopAutoplay() {
  clearInterval(autoplayInterval);
}

if (carouselSlides) {
  goToSlide(0);
  startAutoplay();

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => { stopAutoplay(); goToSlide(i); startAutoplay(); });
  });

  if (prevBtn) prevBtn.addEventListener('click', () => { stopAutoplay(); goToSlide(currentSlide - 1); startAutoplay(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { stopAutoplay(); goToSlide(currentSlide + 1); startAutoplay(); });

  // Touch/swipe support
  let touchStartX = 0;
  carouselSlides.addEventListener('touchstart', e => touchStartX = e.touches[0].clientX, { passive: true });
  carouselSlides.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      stopAutoplay();
      goToSlide(diff > 0 ? currentSlide + 1 : currentSlide - 1);
      startAutoplay();
    }
  }, { passive: true });
}

// ===== BOOKING TABS =====
const bookingTabs = document.querySelectorAll('.booking-tab');
const bookingSections = document.querySelectorAll('.booking-form-section');

bookingTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    bookingTabs.forEach(t => t.classList.remove('active'));
    bookingSections.forEach(s => s.classList.remove('active'));
    tab.classList.add('active');
    const target = tab.dataset.tab;
    const section = document.getElementById(target);
    if (section) section.classList.add('active');
  });
});

// ===== CHAT BOT =====
const chatToggle = document.querySelector('.chat-toggle');
const chatWindow = document.querySelector('.chat-window');
const chatClose = document.querySelector('.chat-close');
const chatInput = document.querySelector('.chat-input');
const chatSend = document.querySelector('.chat-send');
const chatMessages = document.querySelector('.chat-messages');

function addMessage(text, sender) {
  const msg = document.createElement('div');
  msg.className = `chat-message ${sender}`;
  msg.textContent = text;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTyping() {
  const typing = document.createElement('div');
  typing.className = 'chat-message bot typing-indicator';
  typing.innerHTML = '<span></span><span></span><span></span>';
  typing.id = 'typing';
  chatMessages.appendChild(typing);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById('typing');
  if (typing) typing.remove();
}

async function sendMessage() {
  if (!chatInput) return;
  const text = chatInput.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  chatInput.value = '';

  showTyping();

  try {
    const response = await fetch('/api/chat/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text }),
    });
    const data = await response.json();
    removeTyping();
    addMessage(data.response, 'bot');
  } catch (err) {
    removeTyping();
    addMessage('Sorry, I am unable to connect right now. Please call us at +254 700 123 456.', 'bot');
  }
}

if (chatToggle) {
  chatToggle.addEventListener('click', () => {
    chatWindow.classList.toggle('open');
    const notification = chatToggle.querySelector('.chat-notification');
    if (notification) notification.remove();
  });
}

if (chatClose) {
  chatClose.addEventListener('click', () => chatWindow.classList.remove('open'));
}

if (chatSend) {
  chatSend.addEventListener('click', sendMessage);
}

if (chatInput) {
  chatInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
}

// ===== AUTO-DISMISS MESSAGES =====
const djangoMessages = document.querySelectorAll('.message');
djangoMessages.forEach(msg => {
  setTimeout(() => {
    msg.style.opacity = '0';
    msg.style.transition = 'opacity 0.5s ease';
    setTimeout(() => msg.remove(), 500);
  }, 5000);
});

// ===== SCROLL ANIMATIONS =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.service-card, .facility-card, .testimonial-card, .blog-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});

// ===== COUNTER ANIMATION =====
function animateCounter(element, target, suffix = '') {
  let current = 0;
  const increment = target / 60;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current).toLocaleString() + suffix;
  }, 25);
}

const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const numberEl = entry.target.querySelector('.number');
      if (numberEl && !numberEl.dataset.animated) {
        numberEl.dataset.animated = 'true';
        const raw = numberEl.dataset.target;
        const target = parseInt(raw);
        const suffix = numberEl.dataset.suffix || '';
        animateCounter(numberEl, target, suffix);
      }
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.stat-item').forEach(el => statsObserver.observe(el));

// ===== TYPING INDICATOR STYLE =====
const style = document.createElement('style');
style.textContent = `
.typing-indicator {
  display: flex;
  gap: 4px;
  align-items: center;
  padding: 12px 16px !important;
}
.typing-indicator span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--mid-grey);
  animation: typingBounce 1.2s infinite;
}
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingBounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-6px); }
}
`;
document.head.appendChild(style);
