This is a Django-based e-commerce application that allows users to register as vendors or buyers. Vendors can create and manage stores, add/edit/delete products, and monitor their inventory. Buyers can browse all products, add items to a shopping cart, checkout, and receive an invoice by email.
The platform supports verified/unverified product reviews, password reset via email, and uses session-based carts for buyers. User authentication and permissions are handled using Django’s built-in system with additional role-based access. MariaDB is used as the database backend.

To run the project:

Clone the repository and navigate to the project folder.

Create and activate a virtual environment:
python -m venv venv && source venv/bin/activate
(On Windows: venv\Scripts\activate)

Install dependencies:
pip install -r requirements.txt

Set up your database credentials in settings.py.

Run migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Start the server:
python manage.py runserver

Access the app at http://127.0.0.1:8000/