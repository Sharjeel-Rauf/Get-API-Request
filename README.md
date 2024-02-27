
# Create a GET API request

This Django project implements a simple Product API with the following features:










## Task 1: Model Creation

Django model named "Product" with fields:
* title (CharField, max_length=100)
* description (TextField)
* price (DecimalField, max_digits=10, decimal_places=2)
* created_at (DateTimeField, auto_now_add=True)
## Task 2: URL Mapping

URL mapping to display a list of all products at "/products/".
## Task 3: View/Method for "/products/"
View handling the URL "/products/" that returns a list of dummy products in the API.
## Task 4: Signals

Signal that automatically updates the "created_at" field of the product whenever a new product instance is saved.## Project Structure:

* **product_app/models.py:** Defines the "Product" model.
* **product_app/views.py:** Implements the view for handling "/products/".
* **product_app/signals.py:** Contains the signal for updating "created_at".
* **product_django/urls.py:** URL mapping for the project.
* **product_django/settings.py:** Django project settings.
## How to Run:

1. Install Django: `pip install django`
2. Run Migrations: `python manage.py migrate`
3. Create Superuser (Optional): `python manage.py createsuperuser`
4. Run the Development Server: `python manage.py runserver`
