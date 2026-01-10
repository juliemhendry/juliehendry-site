# Julie Hendry - Transformation Consultancy

A clean, fast landing page for Julie's transformation consulting practice.

## Quick Deploy to GitHub Pages

### 1. Create a new repository
- Go to github.com and create a new repo called `juliehendry.com` (or whatever you prefer)
- Make it public (required for free GitHub Pages)

### 2. Upload these files
Either:
- Drag and drop all files into the repo via GitHub's web interface
- Or use git:
```bash
git init
git add .
git commit -m "Initial site"
git remote add origin https://github.com/YOUR_USERNAME/juliehendry.com.git
git push -u origin main
```

### 3. Enable GitHub Pages
- Go to repo Settings → Pages
- Under "Source", select "Deploy from a branch"
- Choose "main" branch and "/ (root)" folder
- Click Save

Your site will be live at `https://YOUR_USERNAME.github.io/juliehendry.com/` within a few minutes.

### 4. Connect your custom domain (juliehendry.com)

**In GitHub:**
- Settings → Pages → Custom domain
- Enter: `juliehendry.com`
- Check "Enforce HTTPS"

**At your domain registrar:**
Add these DNS records:

For apex domain (juliehendry.com):
```
A     @     185.199.108.153
A     @     185.199.109.153
A     @     185.199.110.153
A     @     185.199.111.153
```

For www subdomain:
```
CNAME   www   YOUR_USERNAME.github.io.
```

DNS can take up to 24 hours to propagate.

---

## Files Included

```
├── index.html          # Main landing page
├── styles.css          # All styling
├── script.js           # Smooth scrolling, animations, form handling
├── checklist.html      # Lead magnet assessment tool
└── README.md           # This file
```

## Customization

### Change pricing
Edit `index.html` and find:
```html
<p class="offer-price">£1,497</p>
```

### Connect email form
In `script.js`, find the form handler and replace with your email service:

**Option 1: Formspree (easiest)**
1. Go to formspree.io, create account
2. Create a new form
3. Replace the form action in `index.html`:
```html
<form class="checklist-form" action="https://formspree.io/f/YOUR_ID" method="POST">
```

**Option 2: ConvertKit**
Replace the form with ConvertKit's embed code.

**Option 3: Mailchimp**
Replace the form with Mailchimp's embed code.

### Add Stripe payments
For direct payments (instead of Calendly), you'll need:
1. Stripe account
2. A simple backend (or use Stripe Payment Links)

Easiest approach: Create a Stripe Payment Link and replace the "Book Audit" button href.

### Update Calendly link
Find all instances of `https://calendly.com/juliehendry` and update if your Calendly URL is different.

---

## Future Enhancements

When you're ready to add:
- Blog → Create a `/blog` folder, add markdown files, use a static site generator
- More services → Duplicate the offer section structure
- Testimonials → Add more to the proof section
- Case studies → Create individual HTML pages

---

## Need Help?

The site is pure HTML/CSS/JS—no build step, no dependencies. Edit any file directly and changes go live automatically with GitHub Pages.

For structural changes or new features, come back to Claude!
