// Julie Hendry - Transformation Consultancy
// Simple, performant JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Scroll reveal for sections
    const sections = document.querySelectorAll('section');
    
    const revealSection = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.animation = 'fadeIn 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    };
    
    const sectionObserver = new IntersectionObserver(revealSection, {
        root: null,
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    sections.forEach(section => {
        section.style.opacity = '0';
        sectionObserver.observe(section);
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Nav background on scroll
    const nav = document.querySelector('.nav');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            nav.style.boxShadow = '0 2px 20px rgba(0,0,0,0.08)';
        } else {
            nav.style.boxShadow = 'none';
        }
        
        lastScroll = currentScroll;
    });
    
    // Form handling (placeholder - connect to your email service)
    const checklistForm = document.querySelector('.checklist-form');
    if (checklistForm) {
        checklistForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            // Replace this with your actual form handling
            // Options: Mailchimp, ConvertKit, Buttondown, or simple Formspree
            
            // For now, show a thank you message
            const formParent = this.parentElement;
            this.innerHTML = `
                <p style="color: var(--paper); padding: 1rem; text-align: center;">
                    Thanks! Check your inbox for the checklist.
                </p>
            `;
            
            // Log for testing (remove in production)
            console.log('Email submitted:', email);
            
            // Example: Formspree integration
            // fetch('https://formspree.io/f/YOUR_FORM_ID', {
            //     method: 'POST',
            //     body: JSON.stringify({ email: email }),
            //     headers: { 'Content-Type': 'application/json' }
            // });
        });
    }
    
    // Timeline animation on scroll
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    const revealTimeline = (entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    };
    
    const timelineObserver = new IntersectionObserver(revealTimeline, {
        threshold: 0.2
    });
    
    timelineItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        timelineObserver.observe(item);
    });
    
    // Barrier cards stagger animation
    const barriers = document.querySelectorAll('.barrier');
    
    const revealBarriers = (entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                const allBarriers = document.querySelectorAll('.barrier');
                allBarriers.forEach((barrier, i) => {
                    setTimeout(() => {
                        barrier.style.opacity = '1';
                        barrier.style.transform = 'translateY(0)';
                    }, i * 80);
                });
                observer.unobserve(entry.target);
            }
        });
    };
    
    const barrierObserver = new IntersectionObserver(revealBarriers, {
        threshold: 0.1
    });
    
    barriers.forEach(barrier => {
        barrier.style.opacity = '0';
        barrier.style.transform = 'translateY(20px)';
        barrier.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    });
    
    if (barriers.length > 0) {
        barrierObserver.observe(barriers[0]);
    }
});

// Stripe integration placeholder
// To enable payments, add your Stripe publishable key and create a checkout session
// 
// const stripe = Stripe('pk_live_YOUR_KEY');
// 
// document.querySelector('.btn-primary[href*="stripe"]')?.addEventListener('click', async (e) => {
//     e.preventDefault();
//     const response = await fetch('/create-checkout-session', { method: 'POST' });
//     const session = await response.json();
//     stripe.redirectToCheckout({ sessionId: session.id });
// });
