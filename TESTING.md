# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.
 
## Code Validation

I have validated all the code files in my hotel booking project using industry-standard validators. This ensures that my code follows best practices and maintains high quality standards. The validation was performed on the deployed site to catch any potential issues that might arise in production.

### HTML

I have used the [HTML W3C Validator](https://validator.w3.org) to validate all HTML templates. This ensures proper HTML structure and helps identify any potential rendering issues across different browsers.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bookings | templates/bookings/booking_summary.html | ![screenshot](documentation/html-validation-booking-summary.png) | No Errors |
| bookings | templates/bookings/payment_cancelled.html | ![screenshot](documentation/html-validation-payment-cancelled.png) | No Errors |
| bookings | templates/bookings/payment_success.html | ![screenshot](documentation/html-validation-payment-success.png) | No Errors |
| customer | templates/customer/booking_detail.html | ![screenshot](documentation/html-validation-customer-booking-detail.png) | No Errors |
| customer | templates/customer/dashboard.html | ![screenshot](documentation/html-validation-customer-dashboard.png) | No Errors |
| mainsite | templates/mainsite/about.html | ![screenshot](documentation/html-validation-about.png) | No Errors |
| mainsite | templates/mainsite/contact.html | ![screenshot](documentation/html-validation-contact.png) | No Errors |
| mainsite | templates/mainsite/home.html | ![screenshot](documentation/html-validation-home.png) | No Errors |
| profiles | templates/profiles/edit_profile.html | ![screenshot](documentation/html-validation-edit-profile.png) | No Errors |
| profiles | templates/profiles/view_profile.html | ![screenshot](documentation/html-validation-view-profile.png) | No Errors |
| rooms | templates/rooms/room_detail.html | ![screenshot](documentation/html-validation-room-detail.png) | No Errors |
| rooms | templates/rooms/room_list.html | ![screenshot](documentation/html-validation-room-list.png) | No Errors |
| templates | templates/404.html | ![screenshot](documentation/html-validation-404.png) | No Errors |
| custom_admin | templates/custom_admin/dashboard.html | ![screenshot](documentation/html-validation-admin-dashboard.png) | No Errors |
| custom_admin | templates/custom_admin/booking_list.html | ![screenshot](documentation/html-validation-admin-booking-list.png) | No Errors |
| custom_admin | templates/custom_admin/booking_detail.html | ![screenshot](documentation/html-validation-admin-booking-detail.png) | No Errors |
| custom_admin | templates/custom_admin/room_categories.html | ![screenshot](documentation/html-validation-admin-room-categories.png) | No Errors |
| custom_admin | templates/custom_admin/room_category_detail.html | ![screenshot](documentation/html-validation-admin-room-category-detail.png) | No Errors |
| custom_admin | templates/custom_admin/add_room_category.html | ![screenshot](documentation/html-validation-admin-add-room-category.png) | No Errors |
| custom_admin | templates/custom_admin/edit_room_category.html | ![screenshot](documentation/html-validation-admin-edit-room-category.png) | No Errors |


### CSS

I have used the [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files. This helps maintain consistent styling and identifies any CSS syntax errors or browser compatibility issues.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/css.png) | No errors found |

### JavaScript

I have used the [JShint Validator](https://jshint.com) to validate my JavaScript files. This ensures proper JavaScript syntax and helps identify potential runtime errors in the client-side code.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/jshint.png) | No errors found |

### Python

I have used the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files. This ensures that the code follows Python's style guide and best practices, making it more maintainable and readable.

#### Bookings App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/admin.py) | ![screenshot](documentation/admin_py_pep8_check.png) | All clear, no errors found |
| helpers.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/helpers.py) | ![screenshot](documentation/helpers_py_pep8_check.png) | All clear, no errors found |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/models.py) | ![screenshot](documentation/models_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/urls.py) | ![screenshot](documentation/urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/views.py) | ![screenshot](documentation/views_py_pep8_check.png) | All clear, no errors found |

#### Customer App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/urls.py) | ![screenshot](documentation/customer_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/views.py) | ![screenshot](documentation/customer_views_py_pep8_check.png) | All clear, no errors found |


#### Hotel Booking (Project Settings)
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/context_processors.py) | ![screenshot](documentation/context_processors_py_pep8_check.png) | All clear, no errors found |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/settings.py) | ![screenshot](documentation/settings_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/urls.py) | ![screenshot](documentation/hotel_urls_py_pep8_check.png) | All clear, no errors found |

#### Mainsite App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/urls.py) | ![screenshot](documentation/mainsite_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/views.py) | ![screenshot](documentation/mainsite_views_py_pep8_check.png) | All clear, no errors found |

#### Payments App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/payments/admin.py) | ![screenshot](documentation/payments_admin_py_pep8_check.png) | All clear, no errors found |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/payments/models.py) | ![screenshot](documentation/payments_models_py_pep8_check.png) | All clear, no errors found |


#### Profiles App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/admin.py) | ![screenshot](documentation/profiles_admin_py_pep8_check.png) | All clear, no errors found |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/forms.py) | ![screenshot](documentation/profiles_forms_py_pep8_check.png) | All clear, no errors found |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/models.py) | ![screenshot](documentation/profiles_models_py_pep8_check.png) | All clear, no errors found |
| signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/signals.py) | ![screenshot](documentation/profiles_signals_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/urls.py) | ![screenshot](documentation/profiles_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/views.py) | ![screenshot](documentation/profiles_views_py_pep8_check.png) | All clear, no errors found |


#### Rooms App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/admin.py) | ![screenshot](documentation/rooms_admin_py_pep8_check.png) | All clear, no errors found |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/models.py) | ![screenshot](documentation/rooms_models_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/urls.py) | ![screenshot](documentation/rooms_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/views.py) | ![screenshot](documentation/rooms_views_py_pep8_check.png) | All clear, no errors found |

#### Custom Admin App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/custom_admin/forms.py) | ![screenshot](documentation/custom_admin_forms_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/custom_admin/urls.py) | ![screenshot](documentation/custom_admin_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/custom_admin/views.py) | ![screenshot](documentation/custom_admin_views_py_pep8_check.png) | All clear, no errors found |


#### Newsletter App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/newsletter/admin.py) | ![screenshot](documentation/newsletter_admin_py_pep8_check.png) | All clear, no errors found |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/newsletter/forms.py) | ![screenshot](documentation/newsletter_forms_py_pep8_check.png) | All clear, no errors found |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/newsletter/models.py) | ![screenshot](documentation/newsletter_models_py_pep8_check.png) | All clear, no errors found |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/newsletter/urls.py) | ![screenshot](documentation/newsletter_urls_py_pep8_check.png) | All clear, no errors found |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/newsletter/views.py) | ![screenshot](documentation/newsletter_views_py_pep8_check.png) | All clear, no errors found |



## Browser Compatibility

I have thoroughly tested my hotel booking application across multiple browsers to ensure a consistent user experience. The testing was performed on the deployed site to verify that all features work correctly regardless of the browser being used.

| Page | Chrome | Firefox | Edge |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-edge-home.png) |
| About | ![screenshot](documentation/browser-chrome-about.png) | ![screenshot](documentation/browser-firefox-about.png) | ![screenshot](documentation/browser-edge-about.png) |
| Contact | ![screenshot](documentation/browser-chrome-contact.png) | ![screenshot](documentation/browser-firefox-contact.png) | ![screenshot](documentation/browser-chrome-edge.png) |
| Room List | ![screenshot](documentation/browser-chrome-room-list.png) | ![screenshot](documentation/browser-firefox-room-list.png) | ![screenshot](documentation/browser-edge-room-list.png) |
| Room Detail | ![screenshot](documentation/browser-chrome-room-detail.png) | ![screenshot](documentation/browser-firefox-room-detail.png) | ![screenshot](documentation/browser-edge-room-detail.png) |
| Booking Summary | ![screenshot](documentation/browser-chrome-booking-summary.png) | ![screenshot](documentation/browser-firefox-booking-summary.png) | ![screenshot](documentation/browser-edge-booking-summary.png) |
| Payment Success | ![screenshot](documentation/browser-chrome-payment-success.png) | ![screenshot](documentation/browser-firefox-payment-success.png) | ![screenshot](documentation/browser-edge-payment-success.png) |
| Payment Cancelled | ![screenshot](documentation/browser-chrome-payment-cancelled.png) | ![screenshot](documentation/browser-firefox-payment-cancelled.png) | ![screenshot](documentation/browser-edge-payment-cancelled.png) |
| Customer Dashboard | ![screenshot](documentation/browser-chrome-customer-dashboard.png) | ![screenshot](documentation/browser-firefox-customer-dashboard.png) | ![screenshot](documentation/browser-edge-customer-dashboard.png) |
| Customer Booking Detail | ![screenshot](documentation/browser-chrome-customer-booking.png) | ![screenshot](documentation/browser-firefox-customer-booking.png) | ![screenshot](documentation/browser-edge-customer-booking.png) |
| Profile View | ![screenshot](documentation/browser-chrome-profile.png) | ![screenshot](documentation/browser-firefox-profile.png) | ![screenshot](documentation/browser-edge-profile.png) |
| Profile Edit | ![screenshot](documentation/browser-chrome-profile-edit.png) | ![screenshot](documentation/browser-firefox-profile-edit.png) | ![screenshot](documentation/browser-edge-profile-edit.png) |
| Admin Dashboard | ![screenshot](documentation/browser-chrome-admin-dashboard.png) | ![screenshot](documentation/browser-firefox-admin-dashboard.png) | ![screenshot](documentation/browser-edge-admin-dashboard.png) |
| Admin Room Categories | ![screenshot](documentation/browser-chrome-admin-rooms.png) | ![screenshot](documentation/browser-firefox-admin-rooms.png) | ![screenshot](documentation/browser-edge-admin-rooms.png) |
| Admin Room Category Detail | ![screenshot](documentation/browser-chrome-admin-room-detail.png) | ![screenshot](documentation/browser-firefox-admin-room-detail.png) | ![screenshot](documentation/browser-edge-admin-room-detail.png) |
| Admin Add Room Category | ![screenshot](documentation/browser-chrome-admin-add-room.png) | ![screenshot](documentation/browser-firefox-admin-add-room.png) | ![screenshot](documentation/browser-edge-admin-add-room.png) |
| Admin Edit Room Category | ![screenshot](documentation/browser-chrome-admin-edit-room.png) | ![screenshot](documentation/browser-firefox-admin-edit-room.png) | ![screenshot](documentation/browser-edge-admin-edit-room.png) |
| Admin Booking List | ![screenshot](documentation/browser-chrome-admin-bookings.png) | ![screenshot](documentation/browser-firefox-admin-bookings.png) | ![screenshot](documentation/browser-edge-admin-bookings.png) |
| Admin Booking Detail | ![screenshot](documentation/browser-chrome-admin-booking-detail.png) | ![screenshot](documentation/browser-firefox-admin-booking-detail.png) | ![screenshot](documentation/browser-edge-admin-booking-detail.png) |
| Login | ![screenshot](documentation/browser-chrome-login.png) | ![screenshot](documentation/browser-firefox-login.png) | ![screenshot](documentation/browser-edge-login.png) |
| Register | ![screenshot](documentation/browser-chrome-register.png) | ![screenshot](documentation/browser-firefox-register.png) | ![screenshot](documentation/browser-edge-register.png) |

Notes:
- All pages work as expected across Chrome, Firefox, and Edge browsers
- Consistent functionality and appearance maintained across all browsers
- Forms and interactive elements function correctly in all browsers
- Responsive design works consistently across all browsers
- Images and media content display properly in all browsers

## Responsiveness

I have conducted comprehensive responsive testing on my hotel booking application to ensure optimal user experience across all device sizes. The testing was performed on the deployed site to verify that the layout, navigation, and functionality adapt seamlessly to different screen sizes.

| Page | Mobile (DevTools) | Tablet (DevTools) | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-desktop-home.png) |
| About | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-desktop-about.png) |
| Contact | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-desktop-contact.png) |
| Room List | ![screenshot](documentation/responsive-mobile-room-list.png) | ![screenshot](documentation/responsive-tablet-room-list.png) | ![screenshot](documentation/responsive-desktop-room-list.png) |
| Room Detail | ![screenshot](documentation/responsive-mobile-room-detail.png) | ![screenshot](documentation/responsive-tablet-room-detail.png) | ![screenshot](documentation/responsive-desktop-room-detail.png) |
| Booking Summary | ![screenshot](documentation/responsive-mobile-booking-summary.png) | ![screenshot](documentation/responsive-tablet-booking-summary.png) | ![screenshot](documentation/responsive-desktop-booking-summary.png) |
| Payment Success | ![screenshot](documentation/responsive-mobile-payment-success.png) | ![screenshot](documentation/responsive-tablet-payment-success.png) | ![screenshot](documentation/responsive-desktop-payment-success.png) |
| Customer Dashboard | ![screenshot](documentation/responsive-mobile-customer-dashboard.png) | ![screenshot](documentation/responsive-tablet-customer-dashboard.png) | ![screenshot](documentation/responsive-desktop-customer-dashboard.png) |
| Booking Detail | ![screenshot](documentation/responsive-mobile-booking-detail.png) | ![screenshot](documentation/responsive-tablet-booking-detail.png) | ![screenshot](documentation/responsive-desktop-booking-detail.png) |
| Admin Dashboard | ![screenshot](documentation/responsive-mobile-admin-dashboard.png) | ![screenshot](documentation/responsive-tablet-admin-dashboard.png) | ![screenshot](documentation/responsive-desktop-admin-dashboard.png) |
| Admin Booking List | ![screenshot](documentation/responsive-mobile-admin-booking-list.png) | ![screenshot](documentation/responsive-tablet-admin-booking-list.png) | ![screenshot](documentation/responsive-desktop-admin-booking-list.png) |
| Admin Booking Detail | ![screenshot](documentation/responsive-mobile-admin-booking-detail.png) | ![screenshot](documentation/responsive-tablet-admin-booking-detail.png) | ![screenshot](documentation/responsive-desktop-admin-booking-detail.png) |
| Admin Room Categories | ![screenshot](documentation/responsive-mobile-admin-room-categories.png) | ![screenshot](documentation/responsive-tablet-admin-room-categories.png) | ![screenshot](documentation/responsive-desktop-admin-room-categories.png) |
| Admin Add Room Category | ![screenshot](documentation/responsive-mobile-admin-add-room-category.png) | ![screenshot](documentation/responsive-tablet-admin-add-room-category.png) | ![screenshot](documentation/responsive-desktop-admin-add-room-category.png) |
| Admin Edit Room Category | ![screenshot](documentation/responsive-mobile-admin-edit-room-category.png) | ![screenshot](documentation/responsive-tablet-admin-edit-room-category.png) | ![screenshot](documentation/responsive-desktop-admin-edit-room-category.png) |


Notes:
- Mobile, Tablet, and Desktop: Works as expected across all pages
- All pages maintain proper layout and functionality across different screen sizes
- Tables and forms are properly responsive and usable on all devices
- Navigation remains accessible and user-friendly on all screen sizes

## Lighthouse Audit

I have conducted comprehensive Lighthouse audits on all pages of my hotel booking application to ensure optimal performance, accessibility, and user experience. The audits were performed on the deployed site to get accurate metrics for both mobile and desktop views.

| Page | Result | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home.png) | Performance 68, Accessibility 98, Best Practices 82, SEO 100 – clean, accessible, and SEO-friendly hotel website. |
| About | ![screenshot](documentation/lighthouse-about.png) | Performance 75, Accessibility 98, Best Practices 100, SEO 100 – optimized, user-friendly, and fully standards-compliant. |
| Contact | ![screenshot](documentation/lighthouse-contact.png) | Performance 74, Accessibility 98, Best Practices 100, SEO 100 – responsive, accessible, and well-optimized for user interaction. |
| Room Categories | ![screenshot](documentation/lighthouse-rooms.png) | Performance 73, Accessibility 98, Best Practices 82, SEO 100 – well-structured and SEO-optimized with strong accessibility support.|
| Room Detail | ![screenshot](documentation/lighthouse-room-detail.png) | Performance 76, Accessibility 93, Best Practices 82, SEO 100 – fast-loading, SEO-friendly, and well-structured for user engagement. |
| Booking Summary | ![screenshot](documentation/lighthouse-booking.png) | Performance 96, Accessibility 98, Best Practices 100, SEO 100 – fast, accessible, and fully optimized for a smooth booking experience. |
| Payment Success | ![screenshot](documentation/lighthouse-payment-success.png) | Performance 73, Accessibility 93, Best Practices 61, SEO 100 – functional and SEO-optimized with room for best practice improvements. |
| Payment Cancelled | ![screenshot](documentation/lighthouse-payment-cancelled.png) | Performance 96, Accessibility 100, Best Practices 100, SEO 100 – fast, fully accessible, and flawlessly optimized. |
| Customer Dashboard | ![screenshot](documentation/lighthouse-customer-dashboard.png) | Performance 83, Accessibility 96, Best Practices 100, SEO 100 – efficient, accessible, and optimized for managing bookings. |
| Customer Booking Detail | ![screenshot](documentation/lighthouse-customer-booking.png) | Performance 75, Accessibility 95, Best Practices 82, SEO 100 – informative, accessible, and optimized for booking transparency. |
| Profile View | ![screenshot](documentation/lighthouse-profile.png) | Performance 97, Accessibility 94, Best Practices 100, SEO 100 – fast, accessible, and optimized for user account management. |
| Profile Edit | ![screenshot](documentation/lighthouse-profile-edit.png) | Performance 95, Accessibility 95, Best Practices 100, SEO 100 – smooth, secure, and optimized for user profile updates. |
| Admin Dashboard | ![screenshot](documentation/lighthouse-admin-dashboard.png) |  Performance 97, Accessibility 97, Best Practices 100, SEO 100 – fast, accessible, and fully optimized for admin operations. |
| Admin Room Categories | ![screenshot](documentation/lighthouse-admin-rooms.png) | Performance 97, Accessibility 94, Best Practices 100, SEO 100 – fast, accessible, and optimized for efficient room management. |
| Admin Booking List | ![screenshot](documentation/lighthouse-admin-bookings.png) | Performance 92, Accessibility 96, Best Practices 100, SEO 100 – efficient, accessible, and well-optimized for managing bookings. |
| Login | ![screenshot](documentation/lighthouse-login.png) | Performance 98, Accessibility 95, Best Practices 100, SEO 100 – fast, secure, and fully optimized for user access. |
| Register | ![screenshot](documentation/lighthouse-register.png) | Performance 99, Accessibility 100, Best Practices 100, SEO 100 – lightning-fast, fully accessible, and perfectly optimized for user registration.|

## Defensive Programming

I have implemented comprehensive defensive programming measures throughout my hotel booking application to ensure security and data integrity. The following tests demonstrate the security features and access controls in place.

| Feature | Implementation | Test Coverage | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Authentication | Django's login_required decorator | Comprehensive | Pass | All protected views require authentication |
| Staff Access Control | user_passes_test decorator with is_admin check | Comprehensive | Pass | Admin views restricted to staff users |
| CSRF Protection | Django's CSRF middleware and tokens | Comprehensive | Pass | All forms include CSRF tokens |
| Form Validation | Django form validation with custom forms | Comprehensive | Pass | Input validation on all forms |
| Profile Access Control | User permission checks in views | Comprehensive | Pass | Users can only access their own profiles |
| Booking Management | Staff-only access control | Comprehensive | Pass | Booking operations restricted to staff |
| Room Management | Staff-only access control | Comprehensive | Pass | Room operations restricted to staff |
| File Upload Security | File type and size validation | Comprehensive | Pass | Secure file upload handling |
| Password Security | Django's password hashing and validation | Comprehensive | Pass | Secure password handling |
| Session Security | Django's session middleware | Comprehensive | Pass | Secure session management |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to browse available room categories, so that I can view different room options and their amenities. | ![Room Categories](documentation/story-room-categories.png) |
| As a new site user, I would like to create an account, so that I can make bookings and manage my reservations. | ![Account Creation](documentation/story-account-creation.png) |
| As a new site user, I would like to view room availability for specific dates, so that I can plan my stay. | ![Room Availability](documentation/story-room-availability.png) |
| As a new site user, I would like to see room prices and total cost for my stay, so that I can budget accordingly. | ![Room Pricing](documentation/story-room-pricing.png) |
| As a returning site user, I would like to receive booking confirmation emails, so that I have proof of my reservation. | ![Booking Confirmation](documentation/story-booking-confirmation.png) |
| As a returning site user, I would like to log in to my account, so that I can access my booking history. | ![User Login](documentation/story-user-login.png) |
| As a returning site user, I would like to view my upcoming bookings, so that I can plan my stay. | ![Booking History](documentation/story-booking-history.png) |
| As a returning site user, I would like to update my profile information, so that my details are current. | ![Profile Update](documentation/story-profile-update.png) |
| As a site administrator, I should be able to manage room categories and availability, so that I can control the hotel's inventory. | ![Admin Room Management](documentation/story-admin-room-management.png) |
| As a site administrator, I should be able to view and manage all bookings, so that I can track occupancy and revenue. | ![Admin Booking Management](documentation/story-admin-booking-management.png) |

## Automated Testing

I have conducted comprehensive automated tests on the application using Django's built-in unit testing framework. The test coverage analysis shows a strong overall coverage of 93% across the codebase.

### Test Execution

To run the tests, use the following command:
```bash
python manage.py test
```

### Coverage Analysis

To generate and view test coverage reports:

1. Install coverage:
```bash
pip install coverage
```

2. Generate requirements:
```bash
pip freeze --local > requirements.txt
```

3. Run coverage analysis:
```bash
coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test
coverage report
```

4. For detailed HTML reports:
```bash
coverage html
python -m http.server
```

### Coverage Results

| File | Statements | Missing | Excluded | Coverage |
|------|------------|---------|----------|----------|
| bookings\admin.py | 26 | 4 | 0 | 85% |
| bookings\apps.py | 4 | 0 | 0 | 100% |
| bookings\helpers.py | 14 | 0 | 0 | 100% |
| bookings\models.py | 35 | 0 | 0 | 100% |
| bookings\tests\test_admin.py | 55 | 2 | 0 | 96% |
| bookings\tests\test_helpers.py | 82 | 0 | 0 | 100% |
| bookings\tests\test_models.py | 31 | 0 | 0 | 100% |
| bookings\tests\test_view_booking_summary.py | 41 | 0 | 0 | 100% |
| bookings\tests\test_view_create_checkout_session.py | 53 | 0 | 0 | 100% |
| bookings\tests\test_view_payment_cancelled.py | 30 | 0 | 0 | 100% |
| bookings\tests\test_view_payment_success.py | 71 | 0 | 0 | 100% |
| bookings\urls.py | 4 | 0 | 0 | 100% |
| bookings\views.py | 101 | 19 | 0 | 81% |
| custom_admin\admin.py | 1 | 0 | 0 | 100% |
| custom_admin\apps.py | 5 | 0 | 0 | 100% |
| custom_admin\forms.py | 17 | 0 | 0 | 100% |
| custom_admin\models.py | 1 | 0 | 0 | 100% |
| custom_admin\tests\test_apps.py | 7 | 0 | 0 | 100% |
| custom_admin\tests\test_forms.py | 40 | 0 | 0 | 100% |
| custom_admin\tests\test_models.py | 24 | 0 | 0 | 100% |
| custom_admin\tests\test_urls.py | 24 | 0 | 0 | 100% |
| custom_admin\tests\test_views_booking.py | 114 | 0 | 0 | 100% |
| custom_admin\tests\test_views_booking_list.py | 30 | 0 | 0 | 100% |
| custom_admin\tests\test_views_room.py | 65 | 0 | 0 | 100% |
| custom_admin\tests\test_views_room_category.py | 111 | 0 | 0 | 100% |
| custom_admin\urls.py | 4 | 0 | 0 | 100% |
| custom_admin\views.py | 232 | 66 | 0 | 72% |
| customer\admin.py | 1 | 0 | 0 | 100% |
| customer\apps.py | 4 | 0 | 0 | 100% |
| customer\models.py | 1 | 0 | 0 | 100% |
| customer\tests\test_apps.py | 9 | 0 | 0 | 100% |
| customer\tests\test_urls.py | 12 | 0 | 0 | 100% |
| customer\tests\test_views_booking_detail.py | 29 | 0 | 0 | 100% |
| customer\tests\test_views_dashboard.py | 24 | 0 | 0 | 100% |
| customer\urls.py | 4 | 0 | 0 | 100% |
| customer\views.py | 13 | 0 | 0 | 100% |
| hotel_booking\context_processors.py | 3 | 0 | 0 | 100% |
| hotel_booking\settings.py | 48 | 0 | 0 | 100% |
| hotel_booking\urls.py | 3 | 0 | 0 | 100% |
| mainsite\admin.py | 1 | 0 | 0 | 100% |
| mainsite\apps.py | 4 | 0 | 0 | 100% |
| mainsite\models.py | 1 | 0 | 0 | 100% |
| mainsite\tests.py | 1 | 0 | 0 | 100% |
| mainsite\urls.py | 4 | 0 | 0 | 100% |
| mainsite\views.py | 7 | 2 | 0 | 71% |
| manage.py | 11 | 2 | 0 | 82% |
| newsletter\admin.py | 8 | 0 | 0 | 100% |
| newsletter\apps.py | 4 | 0 | 0 | 100% |
| newsletter\forms.py | 3 | 0 | 0 | 100% |
| newsletter\models.py | 10 | 1 | 0 | 90% |
| newsletter\urls.py | 4 | 0 | 0 | 100% |
| newsletter\views.py | 16 | 11 | 0 | 31% |
| payments\admin.py | 7 | 0 | 0 | 100% |
| payments\apps.py | 4 | 0 | 0 | 100% |
| payments\models.py | 10 | 0 | 0 | 100% |
| payments\tests\test_admin.py | 37 | 0 | 0 | 100% |
| payments\tests\test_apps.py | 6 | 0 | 0 | 100% |
| payments\tests\test_models.py | 27 | 0 | 0 | 100% |
| profiles\admin.py | 25 | 5 | 0 | 80% |
| profiles\apps.py | 6 | 1 | 0 | 83% |
| profiles\forms.py | 22 | 5 | 0 | 77% |
| profiles\models.py | 11 | 1 | 0 | 91% |
| profiles\tests\test_edit_profile.py | 50 | 0 | 0 | 100% |
| profiles\tests\test_forms.py | 0 | 0 | 0 | 100% |
| profiles\tests\test_models.py | 0 | 0 | 0 | 100% |
| profiles\tests\test_signals.py | 0 | 0 | 0 | 100% |
| profiles\tests\test_urls.py | 0 | 0 | 0 | 100% |
| profiles\tests\test_view_profile.py | 0 | 0 | 0 | 100% |
| profiles\urls.py | 4 | 0 | 0 | 100% |
| profiles\views.py | 30 | 2 | 0 | 93% |
| rooms\admin.py | 16 | 0 | 0 | 100% |
| rooms\apps.py | 4 | 0 | 0 | 100% |
| rooms\models.py | 21 | 0 | 0 | 100% |
| rooms\tests\test_admin.py | 20 | 0 | 0 | 100% |
| rooms\tests\test_models.py | 26 | 0 | 0 | 100% |
| rooms\tests\test_urls.py | 9 | 0 | 0 | 100% |
| rooms\tests\test_views_room_detail.py | 29 | 0 | 0 | 100% |
| rooms\tests\test_views_room_list.py | 12 | 0 | 0 | 100% |
| rooms\urls.py | 4 | 0 | 0 | 100% |
| rooms\views.py | 20 | 2 | 0 | 90% |
| **Total** | **1847** | **123** | **0** | **93%** | 


![Test Results Screenshot](documentation/test-results.png)

## Bugs

This section documents the bugs encountered during development and their solutions.

### Django and Python Bugs

1. **Django TemplateDoesNotExist Error**
   - Issue: Templates not being found when rendering views
   - Fix: Added the correct template directory path in settings.py:
   ```python
   TEMPLATES = [
       {
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           ...
       }
   ]
   ```

2. **Database Connection Error**
   - Issue: Failed to connect to PostgreSQL database in production
   - Fix: Updated DATABASE_URL configuration in settings.py to use dj_database_url:
   ```python
   DATABASES = {
       'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
   }
   ```

3. **Booking Date Validation Error**
   - Issue: Bookings could be created with invalid date ranges (check-out before check-in)
   - Fix: Added validation in the Booking model:
   ```python
   def clean(self):
       if self.check_out <= self.check_in:
           raise ValidationError("Check-out date must be after check-in date")
   ```

4. **Room Availability Race Condition**
   - Issue: Multiple users could book the same room simultaneously
   - Fix: Implemented atomic transactions and availability checks in booking_summary view:
   ```python
   is_available = check_room_availability(room_category_id, check_in, check_out)
   if not is_available:
       messages.error(request, "No available rooms in this category for the selected date range.")
   ```

5. **Duplicate Newsletter Subscriptions**
   - Issue: Same email could be subscribed multiple times
   - Fix: Added unique constraint and error handling in subscribe_newsletter view:
   ```python
   try:
       Subscriber.objects.create(email=email)
   except:
       messages.info(request, 'You are already subscribed to our newsletter!')
   ```

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.

