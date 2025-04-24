# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.
 
## Code Validation

I have validated all the code files in my hotel booking project using industry-standard validators. This ensures that my code follows best practices and maintains high quality standards. The validation was performed on the deployed site to catch any potential issues that might arise in production.

### HTML

I have used the [HTML W3C Validator](https://validator.w3.org) to validate all HTML templates. This ensures proper HTML structure and helps identify any potential rendering issues across different browsers.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bookings | booking_summary.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | payment_cancelled.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | payment_success.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | booking_detail.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | dashboard.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | about.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | contact.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | home.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | edit_profile.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | view_profile.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | room_detail.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | room_list.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| templates | 404.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### CSS

I have used the [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files. This helps maintain consistent styling and identifies any CSS syntax errors or browser compatibility issues.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### JavaScript

I have used the [JShint Validator](https://jshint.com) to validate my JavaScript files. This ensures proper JavaScript syntax and helps identify potential runtime errors in the client-side code.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### Python

I have used the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files. This ensures that the code follows Python's style guide and best practices, making it more maintainable and readable.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bookings | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | helpers.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/helpers.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| bookings | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/bookings/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| customer | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/customer/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
|  | env.example.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/env.example.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| hotel_booking | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/context_processors.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| hotel_booking | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/custom_storages.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| hotel_booking | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/settings.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| hotel_booking | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/hotel_booking/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| mainsite | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/mainsite/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/manage.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| payments | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/payments/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| payments | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/payments/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| payments | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/payments/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/forms.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/signals.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/profiles/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| rooms | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/chrysanthusobinna/django-hotel/main/rooms/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |

## Browser Compatibility

I have thoroughly tested my hotel booking application across multiple browsers to ensure a consistent user experience. The testing was performed on the deployed site to verify that all features work correctly regardless of the browser being used.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |

## Responsiveness

I have conducted comprehensive responsive testing on my hotel booking application to ensure optimal user experience across all device sizes. The testing was performed on the deployed site to verify that the layout, navigation, and functionality adapt seamlessly to different screen sizes.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-about.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-etc.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/responsive-xl-home.png) | ![screenshot](documentation/responsiveness/responsive-xl-about.png) | ![screenshot](documentation/responsiveness/responsive-xl-contact.png) | ![screenshot](documentation/responsiveness/responsive-xl-etc.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsiveness/responsive-4k-home.png) | ![screenshot](documentation/responsiveness/responsive-4k-about.png) | ![screenshot](documentation/responsiveness/responsive-4k-contact.png) | ![screenshot](documentation/responsiveness/responsive-4k-etc.png) | Noticeable scaling issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsiveness/responsive-pixel-home.png) | ![screenshot](documentation/responsiveness/responsive-pixel-about.png) | ![screenshot](documentation/responsiveness/responsive-pixel-contact.png) | ![screenshot](documentation/responsiveness/responsive-pixel-etc.png) | Works as expected |
| iPhone 14 | ![screenshot](documentation/responsiveness/responsive-iphone-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-etc.png) | Works as expected |

## Lighthouse Audit

I have conducted comprehensive Lighthouse audits on all pages of my hotel booking application to ensure optimal performance, accessibility, and user experience. The audits were performed on the deployed site to get accurate metrics for both mobile and desktop views.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Excellent performance and accessibility scores |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | High scores across all metrics |
| Contact | ![screenshot](documentation/lighthouse/lighthouse-contact-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-contact-desktop.png) | Strong performance on both devices |
| Room List | ![screenshot](documentation/lighthouse/lighthouse-rooms-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-rooms-desktop.png) | Good performance with room images |
| Room Detail | ![screenshot](documentation/lighthouse/lighthouse-room-detail-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-room-detail-desktop.png) | High scores for image optimization |
| Booking Summary | ![screenshot](documentation/lighthouse/lighthouse-booking-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-booking-desktop.png) | Excellent form validation scores |
| Payment Success | ![screenshot](documentation/lighthouse/lighthouse-payment-success-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-payment-success-desktop.png) | Strong performance metrics |
| Payment Cancelled | ![screenshot](documentation/lighthouse/lighthouse-payment-cancelled-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-payment-cancelled-desktop.png) | Good error handling scores |
| User Dashboard | ![screenshot](documentation/lighthouse/lighthouse-dashboard-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-dashboard-desktop.png) | High accessibility scores |
| Profile View | ![screenshot](documentation/lighthouse/lighthouse-profile-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profile-desktop.png) | Strong performance on both devices |
| Profile Edit | ![screenshot](documentation/lighthouse/lighthouse-profile-edit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profile-edit-desktop.png) | Good form validation scores |
| 404 Error | ![screenshot](documentation/lighthouse/lighthouse-404-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-404-desktop.png) | Excellent error page performance |

## Defensive Programming

I have implemented comprehensive defensive programming measures throughout my hotel booking application to ensure security and data integrity. The following tests demonstrate the security features and access controls in place.

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Profile View | Attempt to access another user's profile | Redirected to home page with warning | Pass | Implemented user authentication and permission checks |
| Admin Dashboard | Attempt to access as regular user | Redirected to home page | Pass | Implemented staff-only access control |
| Booking Management | Attempt to modify booking as regular user | Redirected to home page | Pass | Implemented staff-only access control |
| Payment Processing | Attempt to access payment without booking | Redirected to booking page | Pass | Implemented booking validation |
| Room Management | Attempt to modify room as regular user | Redirected to home page | Pass | Implemented staff-only access control |
| User Authentication | Attempt to access protected pages without login | Redirected to login page | Pass | Implemented login_required decorator |
| Form Validation | Attempt to submit invalid data | Form rejected with error messages | Pass | Implemented form validation |
| API Endpoints | Attempt to access API without proper authentication | Request rejected | Pass | Implemented API authentication |

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/chrysanthusobinna/django-hotel/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Achrysanthusobinna%2Fdjango-hotel%20label%3Abug&label=bugs)](https://github.com/chrysanthusobinna/django-hotel/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/chrysanthusobinna/django-hotel/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/chrysanthusobinna/django-hotel/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/chrysanthusobinna/django-hotel/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/chrysanthusobinna/django-hotel/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/chrysanthusobinna/django-hotel)](https://github.com/chrysanthusobinna/django-hotel/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/chrysanthusobinna/django-hotel/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/chrysanthusobinna/django-hotel/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/chrysanthusobinna/django-hotel/issues/5) | Open |

## Unfixed Bugs
🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.

