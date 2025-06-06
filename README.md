# [Hotel Booking Web Application](https://santhus-hotel-d0ffe8e23f1e.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel)



![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://santhus-hotel-d0ffe8e23f1e.herokuapp.com)

---

## Project Overview

This is a full-stack hotel booking web application developed with Django. It enables customers to explore available rooms based on categories, make bookings, and complete payments seamlessly. Each customer has access to a personal dashboard to view upcoming reservations, booking history, and manage their profile. The admin interface provides tools for managing room categories, handling bookings, and updating customer reservations. The system is designed to offer a smooth and efficient booking experience for both customers and administrators.

## UX

The design of the hotel booking system focuses on creating a luxurious and user-friendly experience. The interface is clean, modern, and intuitive, making it easy for users to browse rooms, make bookings, and manage their reservations.

### Colour Scheme

The color scheme was carefully chosen to reflect a premium hotel experience while maintaining excellent readability and user experience:

- `#f8f9fa` used for background colors, creating a clean and spacious feel
- `#ffc107` used for primary highlights and hover effects
- `#0d6efd` used for interactive elements and icons
- `#444` used for secondary text
- `#ffffff` used for cards and content blocks

The color palette was designed to:
- Create a sense of luxury and comfort
- Ensure high contrast for readability
- Maintain consistency across all pages
- Provide clear visual feedback for interactive elements

### Typography

The website uses a combination of modern, clean fonts to enhance readability and create a premium feel:

- [Montserrat](https://fonts.google.com/specimen/Montserrat) is used for headings and important text elements, providing a strong and elegant presence
- [Lato](https://fonts.google.com/specimen/Lato) is used for body text, ensuring excellent readability across all devices
- [Font Awesome](https://fontawesome.com) icons are used throughout the site for visual elements like:
  - Navigation items
  - Room amenities
  - Contact information
  - Booking status indicators
  - Payment methods

The typography system is designed to:
- Create clear visual hierarchy
- Ensure readability across all screen sizes
- Maintain consistency throughout the user journey
- Support the premium feel of the hotel brand






## User Stories

### New Site Users

- As a new site user, I would like to browse available room categories, so that I can view different room options and their amenities.
- As a new site user, I would like to create an account, so that I can make bookings and manage my reservations.
- As a new site user, I would like to view room availability for specific dates, so that I can plan my stay.
- As a new site user, I would like to see room prices and total cost for my stay, so that I can budget accordingly.

### Returning Site Users

- As a returning site user, I would like to receive booking confirmation emails, so that I have proof of my reservation.
- As a returning site user, I would like to log in to my account, so that I can access my booking history.
- As a returning site user, I would like to view my upcoming bookings, so that I can plan my stay.
- As a returning site user, I would like to update my profile information, so that my details are current.

### Site Admin

- As a site administrator, I should be able to manage room categories and availability, so that I can control the hotel's inventory.
- As a site administrator, I should be able to view and manage all bookings, so that I can track occupancy and revenue.

## Wireframes

To follow best practice, wireframes were developed for mobile and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Desktop Wireframes

| Page | Screenshot |
| --- | --- |
| Home | ![screenshot](documentation/wireframes-desktop-home.png) |
| About | ![screenshot](documentation/wireframes-desktop-about.png) |
| Contact | ![screenshot](documentation/wireframes-desktop-contact.png) |
| Room Categories | ![screenshot](documentation/wireframes-desktop-room-categories.png) |
| Register | ![screenshot](documentation/wireframes-desktop-register.png) |
| Login | ![screenshot](documentation/wireframes-desktop-login.png) |

### Mobile Wireframes

| Page | Screenshot |
| --- | --- |
| Home | ![screenshot](documentation/wireframes-mobile-home.png) |
| About | ![screenshot](documentation/wireframes-mobile-about.png) |
| Contact | ![screenshot](documentation/wireframes-mobile-contact.png) |
| Room Categories | ![screenshot](documentation/wireframes-mobile-room-categories.png) |
| Register | ![screenshot](documentation/wireframes-mobile-register.png) |
| Login | ![screenshot](documentation/wireframes-mobile-login.png) |

## Features

## Existing Features

### Home Page

A welcoming homepage featuring beautiful images of the hotel, engaging text to attract visitors, and a newsletter subscription form for updates and promotions.

![Home Page 1](documentation/feature-home-page-1.png)
![Home Page 2](documentation/feature-home-page-2.png)
![Home Page 3](documentation/feature-home-page-3.png)

---

### About Page

Provides more information about the hotel. Includes elegant images to help guests connect with the hotel's environment.

![About Page](documentation/feature-about-page.png)

---

### Contact Page

A straightforward contact page displaying the hotel’s address, phone number, and email. Useful for inquiries or support.

![Contact Page](documentation/feature-contact-page.png)

---

## Customer Room Booking System

### Browse Room Categories

Customers can explore various room categories with images, descriptions, and pricing.

![Room Categories](documentation/feature-room-categories.png)

---

### Check Room Availability

After selecting a room category, logged-in users can view detailed information and check availability by entering check-in and check-out dates.

![Check Availability](documentation/feature-check-availability.png)

---

### Booking Summary

If the selected room is available, customers are shown a booking summary that includes:

* Room price per night
* Total number of nights
* Total cost
* A button to proceed to payment

![Booking Summary](documentation/feature-booking-summary.png)

---

### Payment

Customers make secure payments using Stripe. After successful payment, they are redirected to a confirmation page.

![Payment Form](documentation/feature-payment-form.png)
![Payment Success](documentation/feature-payment-success.png)

---

## Customer Dashboard

Logged-in customers can view:

* Upcoming bookings
* Booking history

![Customer Bookings](documentation/feature-customer-bookings.png)
![Booking Detail](documentation/feature-booking-detail.png)

---

## Customer Profile

Customers can view and update their profile information.

![View Profile](documentation/feature-view-profile.png)
![Edit Profile](documentation/feature-edit-profile.png)

---

## Admin Dashboard

The admin interface allows management of room categories, individual rooms, and customer bookings.

### Manage Room Categories

Admins can:

* View room categories
* Add new room categories
* Edit existing ones

![View Room Category](documentation/feature-admin-view-category.png)
![Add Room Category](documentation/feature-admin-add-category.png)
![Edit Room Category](documentation/feature-admin-edit-category.png)

---

### Manage Rooms

Admins can:

* Add rooms to categories
* Edit room details
* Delete rooms

![Add Room](documentation/feature-admin-add-room.png)
![Edit Room](documentation/feature-admin-edit-room.png)
![Delete Room](documentation/feature-admin-delete-room.png)

---

### Booking Management

Admins can:

* View all customer bookings
* Update booking status and details

![Admin View Booking](documentation/feature-admin-view-booking.png)
![Admin Update Booking](documentation/feature-admin-update-booking.png)

---

### Future Features

- **Enhanced Website Pages**
    - Virtual tour of hotel facilities
    - Restaurant and dining section with online reservations
    - Spa and wellness booking system
    - Event and conference room booking
    - Local attractions and activities guide
    - Customer testimonials and reviews section
    - Blog section for hotel news and updates

- **AI-Powered Analytics & Reporting**
    - Predictive occupancy forecasting
    - Revenue optimization suggestions
    - Customer behavior analysis
    - Automated pricing recommendations
    - Seasonal trend predictions
    - Staffing level optimization
    - Maintenance schedule predictions


## Tools & Technologies Used

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control.
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as the local IDE for development.

### Frontend Technologies
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for enhanced user interaction and AJAX functionality.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.

### Backend Technologies
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python web framework.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management system.
- [![Django Allauth](https://img.shields.io/badge/Django_Allauth-grey?logo=django&logoColor=092E20)](https://django-allauth.readthedocs.io) used for user authentication and account management.

### Deployment & Services
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed application.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of hotel bookings.

### Development Tools
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

Entity Relationship Diagrams (ERD) help visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

### Models Overview

The project consists of the following key models:

#### RoomCategory Model
- Purpose: Manages different categories of hotel rooms (e.g., Standard, Deluxe, Suite)
- Fields:
  - `name`: CharField - Name of the room category
  - `description`: TextField - Detailed description of the room category
  - `price`: DecimalField - Price per night
  - `image`: CloudinaryField - Main image for the room category

#### RoomCategoryImage Model
- Purpose: Handles multiple images for each room category
- Fields:
  - `room_category`: ForeignKey to RoomCategory
  - `image`: CloudinaryField - Additional images for the room category
  - `caption`: CharField - Optional caption for the image

#### Room Model
- Purpose: Represents individual rooms in the hotel
- Fields:
  - `category`: ForeignKey to RoomCategory
  - `name`: CharField - Unique identifier for the room
  - `is_available`: BooleanField - Current availability status

#### Booking Model
- Purpose: Manages guest reservations
- Fields:
  - `user`: ForeignKey to User - Guest making the booking
  - `room`: ForeignKey to Room - Specific room assigned (optional)
  - `room_category`: ForeignKey to RoomCategory - Category of room booked
  - `check_in`: DateField - Planned check-in date
  - `check_out`: DateField - Planned check-out date
  - `actual_check_in`: DateTimeField - Actual check-in time (optional)
  - `actual_check_out`: DateTimeField - Actual check-out time (optional)
  - `created_at`: DateTimeField - Booking creation timestamp
  - `is_paid`: BooleanField - Payment status
  - `is_cancelled`: BooleanField - Cancellation status
  - `booking_number`: CharField - Unique 6-digit booking reference
  - `total_price`: DecimalField - Total cost of the stay

#### Payment Model
- Purpose: Tracks payment transactions for bookings
- Fields:
  - `booking`: OneToOneField to Booking
  - `stripe_payment_intent`: CharField - Stripe payment reference
  - `amount`: DecimalField - Payment amount
  - `timestamp`: DateTimeField - Payment timestamp
  - `status`: CharField - Current payment status

#### UserProfile Model
- Purpose: Extends the default Django User model with additional information
- Fields:
  - `user`: OneToOneField to User
  - `address`: CharField - Guest's address
  - `city`: CharField - Guest's city
  - `post_code`: CharField - Guest's postal code
  - `country`: CharField - Guest's country
  - `phone_number`: CharField - Guest's contact number (optional)

#### Subscriber Model
- Purpose: Manages newsletter subscriptions
- Fields:
  - `email`: EmailField - Subscriber's email address
  - `date_subscribed`: DateTimeField - Subscription date
  - `is_active`: BooleanField - Subscription status

### Auto-generating ERD with pygraphviz

I used `pygraphviz` and `django-extensions` to auto-generate an ERD. Here are the steps I followed:

1. Install required dependencies:
   ```bash
   sudo apt update
   sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
   pip3 install django-extensions pygraphviz
   ```

2. Add 'django_extensions' to INSTALLED_APPS in settings.py:
   ```python
   INSTALLED_APPS = [
       ...
       'django_extensions',
       ...
   ]
   ```

3. Generate the ERD:
   ```bash
   python3 manage.py graph_models -a -o erd.png
   ```

4. Move the generated `erd.png` to your documentation folder

5. Clean up:
   ```bash
   pip3 uninstall django-extensions pygraphviz -y
   ```

The generated ERD can be found in the documentation folder:

![erd](documentation/erd.png)

*Source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)*

## Agile Development Process

### Project Management Tools

#### GitHub Projects
[GitHub Projects](https://github.com/chrysanthusobinna/django-hotel/projects) served as our primary Agile tool for project management. Through careful organization of tags and project creation, we effectively utilized the Kanban board to track user stories, issues, and milestone tasks on a weekly basis.

![GitHub Projects Board](documentation/gh-projects.png)

#### GitHub Issues
[GitHub Issues](https://github.com/chrysanthusobinna/django-hotel/issues) complemented our Agile workflow with a custom **User Story Template** for managing user stories and tracking milestone iterations.

- **Open Issues** [![GitHub issues](https://img.shields.io/github/issues/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/issues)  
  ![Open Issues](documentation/gh-issues-open.png)

- **Closed Issues** [![GitHub closed issues](https://img.shields.io/github/issues-closed/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/issues?q=is%3Aissue+is%3Aclosed)  
  ![Closed Issues](documentation/gh-issues-closed.png)


### Prioritization Methodology

I implemented the MoSCoW prioritization technique to effectively manage our backlog:

- **Must Have**: Critical features guaranteed for delivery (max 60% of stories)
- **Should Have**: Important features that add significant value (approximately 20% of stories)
- **Could Have**: Desirable features with smaller impact (approximately 20% of stories)
- **Won't Have**: Features deferred to future iterations

This approach allowed me to decompose Epics into manageable stories, apply appropriate prioritization labels, and maintain focus on delivering the most valuable features first.

## Ecommerce Business Model

This hotel booking system follows a `Business to Customer` (B2C) model, focusing on providing a seamless booking experience for individual guests. The platform is designed to:

- Enable direct room bookings by individual customers
- Provide transparent pricing and room availability
- Offer secure payment processing
- Allow customers to manage their bookings and profiles
- Support customer communication through social media

The system includes features for:
- Room browsing and filtering
- Real-time availability checking
- Secure payment processing
- Booking management
- Customer profile management

Social media integration helps build a community of guests and promotes the hotel's brand, while the newsletter system enables direct communication about:
- Special offers and seasonal promotions
- New room types or amenities
- Event announcements
- Seasonal packages
- Important updates about hotel services

## Search Engine Optimization (SEO) & Social Media Marketing

### SEO Implementation

The project implements comprehensive SEO best practices:

1. **Meta Tags & Open Graph**
   - Custom meta descriptions and keywords for each page
   - Open Graph tags for better social media sharing
   - Responsive viewport settings
   - Proper title tags with dynamic content

2. **Technical SEO**
   - XML Sitemap implementation (sitemap.xml)
   - Robots.txt configuration with proper directives
   - Clean URL structure
   - Mobile-responsive design

3. **Keywords Strategy**
   The site targets relevant hotel and booking-related keywords:
   - Primary: hotel, booking, rooms, accommodation
   - Secondary: luxury stay, comfortable rooms, hotel reservation
   - Location-based keywords for better local SEO

### Sitemap Implementation

The project uses a comprehensive XML sitemap that includes:
- Homepage (priority: 1.00)
- About page (priority: 0.80)
- Contact page (priority: 0.80)
- Room listing pages
- Other important site sections

The sitemap is properly referenced in the robots.txt file and follows XML sitemap protocol standards.

### Robots.txt Configuration

The robots.txt file is configured with:
```
User-agent: *
Disallow: /accounts/
Sitemap: https://santhus-hotel-d0ffe8e23f1e.herokuapp.com/sitemap.xml
```

This configuration:
- Allows search engines to crawl all public pages
- Restricts access to account-related pages for security
- Properly references the sitemap location

### Social Media Integration

The site implements Open Graph meta tags for optimal social media sharing:
- Dynamic title and description for each page



## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://santhus-hotel-d0ffe8e23f1e.herokuapp.com).

### Environment Variables

The following environment variables are required to run the application:

| Variable | Description | Example Value |
| --- | --- | --- |
| `SECRET_KEY` | Django secret key for security | "your-secret-key-here" |
| `DATABASE_URL` | PostgreSQL database URL | "postgresql://username:password@host:port/database_name" |
| `STRIPE_SECRET_KEY` | Stripe API secret key | "sk_test_your_stripe_secret_key" |
| `STRIPE_PUBLIC_KEY` | Stripe API public key | "pk_test_your_stripe_public_key" |
| `CLOUDINARY_URL` | Cloudinary URL for media storage | "cloudinary://api_key:api_secret@cloud_name" |
| `SITE_NAME` | Name of the hotel | "Your Hotel Name" |
| `SITE_EMAIL` | Hotel's contact email | "info@yourhotel.com" |
| `SITE_PHONE` | Hotel's contact phone number | "+44 1234 567890" |
| `SITE_ADDRESS` | Hotel's physical address | "Your Hotel Address" |
| `FACEBOOK_PAGE_LINK` | Full URL to hotel's Facebook page | "https://www.facebook.com/your-hotel-page" |
| `INSTAGRAM_PAGE_LINK` | Full URL to hotel's Instagram page | "https://www.instagram.com/your-hotel-page" |
| `CURRENCY_SYMBOL` | Currency symbol for prices | "£" |
| `CURRENCY_CODE` | Currency code for payments | "GBP" |
| `EMAIL_BACKEND` | Django email backend | "django.core.mail.backends.smtp.EmailBackend" |
| `EMAIL_HOST` | SMTP server hostname | "your-smtp-server.com" |
| `EMAIL_PORT` | SMTP server port | "465" |
| `EMAIL_USE_TLS` | Use TLS for email (True/False) | "False" |
| `EMAIL_USE_SSL` | Use SSL for email (True/False) | "True" |
| `EMAIL_HOST_USER` | SMTP username/email | "your-email@example.com" |
| `EMAIL_HOST_PASSWORD` | SMTP password | "your-email-password" |
| `DEFAULT_FROM_EMAIL` | Default sender email address | "your-email@example.com" |

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- Navigated to the Databases section
- Requested a new PostgreSQL database
- Received an email with my database credentials and connection URL
- The database URL was in the format: `postgresql://username:password@host:port/database_name`

> [!CAUTION]  
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Cloudinary

This project uses [Cloudinary](https://cloudinary.com) to store media files online, due to the fact that Heroku doesn't persist this type of data.

To set up Cloudinary:

1. Create a free account on [Cloudinary](https://cloudinary.com)
2. Once logged in, you'll find your Cloudinary URL in the dashboard
3. The URL will be in the format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

To set up Stripe:

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Go to the Developers section
3. Get your test API keys:
   - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
   - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

### Email Configuration

This project uses SMTP for sending emails. The configuration uses a custom email server:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'SMPTP HOST'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@domain.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@domain.com'
```

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com) for deployment. Follow these steps:

1. Create a new Heroku app:
   - Log in to Heroku
   - Click "New" → "Create new app"
   - Choose a unique name and region

2. Set up Config Vars in Heroku using all the Environment Variables listed in the table above. Each variable from the table should be added as a Config Var with its corresponding value.

3. Required files for Heroku deployment:
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`

4. Connect your GitHub repository to Heroku:
   - In Heroku dashboard, go to "Deploy" tab
   - Choose "GitHub" as deployment method
   - Connect to your repository
   - Enable automatic deploys
### Local Deployment

To run this project locally:

1. Clone the repository:
```bash
git clone https://github.com/chrysanthusobinna/django-hotel.git
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Create an `env.py` file with your environment variables (use `env.example.py` as template)

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The site should now be running at `http://127.0.0.1:8000/`

### Forking

To fork this repository:

1. Log in to GitHub
2. Go to [the repository](https://github.com/chrysanthusobinna/django-hotel)
3. Click the "Fork" button in the top-right corner
4. You'll now have a copy of the repository in your GitHub account

### Cloning

To clone this repository:

1. Go to [the repository](https://github.com/chrysanthusobinna/django-hotel)
2. Click the "Code" button
3. Copy the URL (HTTPS or SSH)
4. In your terminal:
```bash
git clone https://github.com/chrysanthusobinna/django-hotel.git
```

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Django Documentation](https://docs.djangoproject.com) | Entire Project | Used for Django framework implementation and best practices |
| [Bootstrap Documentation](https://getbootstrap.com/docs) | Frontend | Used for responsive design and UI components |
| [Stripe Documentation](https://stripe.com/docs) | Payment System | Used for payment processing implementation |
| [Django Allauth Documentation](https://django-allauth.readthedocs.io) | Authentication | Used for user authentication and account management |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com/photo/orange-lounges-near-swimming-pool-261169/) | Home Page | Image | Swimming pool area with orange lounges showcasing hotel amenities |
| [Pexels](https://www.pexels.com/photo/brown-wooden-house-in-daytime-453201/) | Home Page | Image | Exterior view of hotel building used in banner section |
| [Pexels](https://www.pexels.com/photo/white-bathtub-in-bathroom-1571461/) | Home Page | Image | Luxury bathroom interior highlighting hotel facilities |
| [Pexels](https://www.pexels.com/photo/person-holding-pastry-dishes-on-white-ceramic-plates-262978/) | Home Page | Image | Restaurant service presentation showcasing dining experience |
| [Pexels](https://www.pexels.com/photo/white-sunloungers-beside-pool-261102/) | Home Page | Image | Poolside loungers displaying outdoor relaxation area |
| [Pexels](https://www.pexels.com/photo/palm-trees-at-night-258154/) | About Page | Image | Night view of hotel exterior with palm trees |
| [Pexels](https://www.pexels.com/photo/woman-in-white-long-sleeve-shirt-holding-pink-and-green-floral-textile-7755659/) | Contact Page | Image | Welcoming hotel reception staff member |
| [Pexels](https://www.pexels.com/photo/photo-of-living-room-1457842/) | Room Categories | Image | Family Suite showcase featuring spacious living area |
| [Pexels](https://www.pexels.com/photo/upholstered-bed-near-cabinet-262048/) | Room Categories | Image | Standard Room display with comfortable furnishings |
| [Pexels](https://www.pexels.com/photo/room-with-bed-and-wooden-floor-1743229/) | Room Categories | Image | Luxury Room presentation with premium interior design |
| [Font Awesome](https://fontawesome.com) | Throughout Site | Icons | Various UI icons for enhanced user experience |
| [Am I Responsive](https://ui.dev/amiresponsive) | Documentation | Image | Website mockup showing responsive design across devices |
| [ChatGPT](https://chat.openai.com) | Meta Tags | Content | Generated Open Graph protocol meta descriptions for social media sharing |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank my family and friends for their support and encouragement throughout the development of this project.

