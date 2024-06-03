
# DKT Micro Art: Your Destination for Miniature Masterpieces

## Introduction

Welcome to DKT Micro Art, your premier destination for discovering and purchasing exquisite miniature masterpieces from talented artists around the nation. DKT Micro Art is dedicated to showcasing the intricate beauty of micro art, offering a diverse collection of tiny paintings, sculptures, photography, and more.

![Screenshot (67)](https://github.com/Srikanth-343/My-DKT-Store.github/assets/57741770/3b1f8a43-575d-481a-9d82-894709d43bba)


## Technical Details

### Technology Used

DKT Micro Art is made using these technologies:

- **Frontend**: HTML, CSS, Bootstrap 3, JavaScript
- **Backend**: Python with Django framework
- **Database**: SQLite3
- **Development Environment**: PyCharm IDE
- **Template desiginer**: Jinja


### Features

Enjoy these features on DKT Micro Art:

- **Explore**: Find a wide range of micro art pieces including tiny paintings, sculptures, and photography.
- **Search**: Use filters to narrow down your search by artist, style, or price.
- **Checkout**: PayTm - Buy securely with payment options.
- **Accounts**: Create an account to save your favorite micro art, track orders, and get personalized recommendations.

### In summary, the MVC/MVT pattern in Django works as follows:

**Model (M)**: Defines the data structure and interacts with the database.

- **models.py** - in this python file we create django.db models like Product, Order, OrderUpdate and Contact.

View (V): Processes requests, retrieves data from models, and passes it to templates for rendering.

- **views.py** - ProductView, Product tracker, product search, Paytm checkout, signupView, signinView and signoutView.

Template (T) /Controllers(C): Renders HTML pages, incorporating dynamic content provided by views.

- **urls.py** - Renders HTML pages, incorporating dynamic content provided by views.
  
### Deployment

DKT Micro Art is hosted on reliable cloud platforms like AWS.

## Getting Started

To start exploring the world of miniature masterpieces with DKT Micro Art. Browse, shop, and enjoy tiny treasures!

### Installation
Clone the repository: git clone

Navigate to the project directory: cd project_name

Install dependencies: pip install -r requirements.txt

Run migrations: python manage.py migrate

Start the development server: python manage.py runserver

### Usage
Access the admin panel to manage company records: http://localhost:8000/admin

Username: admin

Password: admin

Use the provided views and templates to interact with the application

---

This version emphasizes the focus on micro art while still providing technical details and information about the platform. Adjustments can be made as needed to better fit your project's specifics.
