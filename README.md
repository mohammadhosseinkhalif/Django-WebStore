# 🛒 Django WebStore

A full-featured **Django-based e-commerce web application** built with Python and Django.

This project is designed as a practical web store where users can browse products, explore categories and brands, manage a shopping cart, place orders, like products, and leave reviews. The project also includes a Django admin interface for managing the store's data.

> **Project:** Django-WebStore
> **Framework:** Django
> **Language:** Python
> **Database:** SQLite
> **Status:** Development / Educational Project

---

## 📌 Table of Contents

* [About the Project](#-about-the-project)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Project Architecture](#-project-architecture)
* [Project Structure](#-project-structure)
* [Application Modules](#-application-modules)
* [Data Models](#-data-models)
* [How the Application Works](#-how-the-application-works)
* [Getting Started](#-getting-started)
* [Installation](#-installation)
* [Running the Project](#-running-the-project)
* [Creating an Admin User](#-creating-an-admin-user)
* [Django Admin](#-django-admin)
* [Static and Media Files](#-static-and-media-files)
* [Development Workflow](#-development-workflow)
* [Troubleshooting](#-troubleshooting)
* [Future Improvements](#-future-improvements)
* [Contributing](#-contributing)
* [License](#-license)
* [Author](#-author)

---

## 🌐 About the Project

**Django WebStore** is an e-commerce web application developed with Django.

The main purpose of this project is to provide a structured online shopping experience while demonstrating how Django can be used to build a modular store application.

The application separates different responsibilities into Django apps, including:

* Product and catalog management
* Shopping cart functionality
* User profile functionality
* Product categories and brands
* Product media
* Orders
* Product likes
* Product reviews
* Store administration

The project follows Django's application-based architecture, making the codebase easier to maintain and extend.

---

## ✨ Features

### 🛍️ Product Management

The store supports managing products with information such as:

* Product name
* Price
* Description
* Stock quantity
* Category
* Brand
* Product pictures
* Sales count
* Product score
* Discount status
* Discounted price

Products are connected to categories and brands through Django model relationships.

---

### 🗂️ Categories

Products can be organized into different categories.

Each category contains:

* Name
* Optional image

This makes it possible to organize products into logical groups and provide a better browsing experience.

---

### 🏷️ Brands

The application also supports product brands.

A brand contains:

* Name
* Optional image

Products can be associated with a specific brand, allowing the store to organize and filter products based on their manufacturer or brand.

---

### 🖼️ Product Media

Products can have multiple media files.

The project supports:

* Images
* Videos
* Alternative text
* Custom ordering
* Upload timestamps

Media files are associated with their products and can be displayed as part of the product details.

---

### 🛒 Shopping Cart

The project contains a dedicated `cart` Django app responsible for shopping cart functionality.

The cart module includes:

* Cart management
* Cart models
* Cart views
* Cart URLs
* Context processors

This allows cart-related information to be handled separately from the main product application.

---

### 📦 Orders

Users can create orders for products.

An order contains information including:

* Product
* Quantity
* Customer
* Address
* Creation date
* Order status

Orders are connected to Django's built-in user model.

---

### ❤️ Product Likes

Authenticated users can like products.

The project uses a dedicated `LikedItems` model to associate users with products they have liked.

This provides the foundation for a favorites / liked-products experience.

---

### ⭐ Product Reviews

Users can submit reviews for products.

Each review contains:

* Product
* User
* Review text
* Star rating
* Creation date

The rating is restricted to a value between **1 and 5 stars**.

The project also prevents the same user from creating multiple reviews for the same product through a database-level unique constraint.

---

### 👤 User Profiles

The project contains a dedicated `user_profile` Django app for user-related functionality.

User-related templates are separated under:

```text
templates/profile/
```

This keeps profile-related presentation separate from the main store pages.

---

### ⚙️ Django Admin

The project uses Django's built-in administration system for managing store data.

The admin interface can be used to work with application data such as:

* Products
* Categories
* Brands
* Product media
* Orders
* Likes
* Reviews

This provides a convenient management interface without requiring a separate administration application.

---

## 🧰 Tech Stack

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| 🐍 Python        | Main programming language        |
| 🌐 Django        | Backend web framework            |
| 🗄️ SQLite       | Development database             |
| HTML5            | Page structure                   |
| CSS3             | Styling                          |
| JavaScript       | Client-side interactions         |
| Django Templates | Server-side rendering            |
| Pillow           | Image processing / image support |

The repository currently includes Django and Pillow in `requirements.txt`.

---

## 🏗️ Project Architecture

The project is organized around multiple Django applications.

At a high level, the architecture looks like this:

```text
                         ┌───────────────────┐
                         │      Browser      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Django URL Router │
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
              ┌──────────┐   ┌──────────┐   ┌──────────────┐
              │   Shop   │   │   Cart   │   │ User Profile │
              └────┬─────┘   └────┬─────┘   └──────┬───────┘
                   │              │                 │
                   └──────────────┼─────────────────┘
                                  │
                                  ▼
                         ┌───────────────────┐
                         │   Django Models   │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │      SQLite       │
                         └───────────────────┘
```

Django's template system is used for the presentation layer, while Django models handle the application's data layer.

---

## 📁 Project Structure

The main repository structure is:

```text
Django-WebStore/
│
├── cart/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── cart.py
│   ├── context_processors.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── user_profile/
│   ├── migrations/
│   ├── ...
│   └── ...
│
├── static/
│   ├── assets/
│   └── css/
│
├── templates/
│   ├── cart/
│   ├── profile/
│   ├── shop/
│   ├── base.html
│   ├── footer.html
│   ├── header.html
│   └── navbar.html
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

The repository currently contains the `cart`, `config`, `shop`, `static`, `templates`, and `user_profile` directories alongside `manage.py` and `requirements.txt`.

---

## 🧩 Application Modules

### `shop`

The `shop` application is the core of the e-commerce system.

It contains the main product-related functionality:

```text
shop/
├── models.py
├── views.py
├── urls.py
├── admin.py
└── tests.py
```

The application contains models for products, categories, brands, product media, orders, likes, and reviews.

---

### `cart`

The `cart` application is responsible for shopping cart functionality.

```text
cart/
├── cart.py
├── models.py
├── views.py
├── urls.py
├── context_processors.py
├── admin.py
└── tests.py
```

The presence of a dedicated cart service/module and context processor allows cart information to be integrated into the site's templates.

---

### `user_profile`

The `user_profile` application contains functionality related to user profiles.

Its templates are separated from the shop templates:

```text
templates/
└── profile/
```

This separation makes it easier to maintain account and profile-related pages independently.

---

### `config`

The `config` directory contains the main Django project configuration.

It is responsible for project-level configuration such as:

* Django settings
* Root URL configuration
* ASGI configuration
* WSGI configuration

---

## 🗃️ Data Models

The main store models include:

### `Category`

Represents a product category.

```text
Category
├── name
└── image
```

---

### `Brand`

Represents a product brand.

```text
Brand
├── name
└── image
```

---

### `Product`

Represents an item available in the store.

```text
Product
├── name
├── pictures
├── price
├── description
├── category
├── brand
├── stock
├── score
├── sell
├── discounted
└── discounted_price
```

The product model is connected to both `Category` and `Brand`.

---

### `ProductMedia`

Provides additional media for products.

```text
ProductMedia
├── product
├── file
├── media_type
├── alt_text
├── order
└── uploaded_at
```

Supported media types currently include:

```text
image
video
```

Media items are ordered by their custom order and upload time.

---

### `Order`

Represents a customer's order for a product.

```text
Order
├── product
├── quantity
├── address
├── customer
├── date
└── status
```

The customer is connected to Django's built-in `User` model.

---

### `LikedItems`

Connects users with products they have liked.

```text
LikedItems
├── user
└── product
```

---

### `Review`

Represents a product review submitted by a user.

```text
Review
├── product
├── user
├── text
├── star
└── created_at
```

The star rating accepts values from **1 to 5**, and each user can have only one review for a specific product.

---

## 🔄 How the Application Works

A typical user flow looks like this:

```text
1. User visits the store
          │
          ▼
2. Browses products
          │
          ▼
3. Selects a product
          │
          ▼
4. Views product information
          │
          ├───────────────┐
          │               │
          ▼               ▼
      Like Product     Add to Cart
                          │
                          ▼
                    Review Cart
                          │
                          ▼
                    Place Order
                          │
                          ▼
                     Order Created
```

The application separates product browsing, cart management, user functionality, and store data management into different Django components.

---

# 🚀 Getting Started

## 📋 Prerequisites

Before running the project, make sure you have the following installed:

* Python 3
* pip
* Git

You can verify your Python installation with:

```bash
python --version
```

or, depending on your operating system:

```bash
python3 --version
```

Verify Git:

```bash
git --version
```

---

# 📥 Installation

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/mohammadhosseinkhalif/Django-WebStore.git
```

Move into the project directory:

```bash
cd Django-WebStore
```

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended so that the project's dependencies remain isolated from your global Python installation.

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

After activation, your terminal should indicate that the virtual environment is active.

---

## 3. Upgrade pip

It is recommended to use an up-to-date version of pip:

```bash
python -m pip install --upgrade pip
```

---

## 4. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The repository provides a `requirements.txt` file for installing the project's Python dependencies.

---

## 5. Apply Database Migrations

Run:

```bash
python manage.py migrate
```

This creates and updates the required database tables.

---

## 6. Create a Superuser

To access Django Admin, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to configure:

* Username
* Email
* Password

---

# ▶️ Running the Project

Start Django's development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

Open the address in your browser.

---

## 🛠️ Useful Django Commands

### Run the development server

```bash
python manage.py runserver
```

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Run tests

```bash
python manage.py test
```

### Open Django shell

```bash
python manage.py shell
```

---

# 🔐 Django Admin

After creating a superuser, open:

```text
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials.

The Django admin interface can be used as the management panel for the application's store data.

Depending on the registered models, administrators can manage entities such as:

* Categories
* Brands
* Products
* Product media
* Orders
* Likes
* Reviews

This is particularly useful during development because products and other store data can be created without building a separate management dashboard.

---

# 🖼️ Static and Media Files

The project contains a dedicated `static` directory:

```text
static/
├── assets/
└── css/
```

The repository also uses file fields for product/category/brand media, including product media uploads.

When working locally, make sure Django's static and media configuration is correctly configured in the project's settings.

For production deployments, static and uploaded media files should be handled using an appropriate production setup rather than relying on Django's development server.

---

# 🧪 Testing

The repository contains `tests.py` files inside the Django applications.

You can run the Django test suite with:

```bash
python manage.py test
```

For a specific application:

```bash
python manage.py test shop
```

or:

```bash
python manage.py test cart
```

---

# 🔧 Development Workflow

A typical development workflow for this project can look like:

```bash
# Activate environment
.venv\Scripts\activate

# Install/update dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run tests
python manage.py test

# Start development server
python manage.py runserver
```

When modifying models, remember to create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 🐛 Troubleshooting

## `python` command is not recognized

If Windows cannot find Python, make sure Python is installed and added to your system PATH.

You can also try:

```bash
py --version
```

and use:

```bash
py -m venv .venv
```

---

## Virtual environment is not activated

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Then verify that the correct Python environment is being used.

---

## Missing dependencies

If Django or another package cannot be imported, reinstall the project dependencies:

```bash
pip install -r requirements.txt
```

---

## Database errors

If the database is not synchronized with the Django models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Static files are not loading

Check:

* `STATIC_URL`
* `STATICFILES_DIRS`
* Static file locations
* Template references to static files
* Whether the development server is running

For production, static files should be collected and served through an appropriate web server or hosting configuration.

---

# 🗺️ Future Improvements

The current project provides a solid foundation for an e-commerce application. Some possible future improvements include:

### 💳 Payment Integration

Add an online payment gateway to support real transactions.

### 📦 Advanced Order Management

Improve order handling with multiple statuses, for example:

```text
Pending
Confirmed
Processing
Shipped
Delivered
Cancelled
```

### 🔎 Advanced Product Search

Add:

* Keyword search
* Brand filtering
* Category filtering
* Price range filtering
* Sorting
* Availability filtering

### 📱 Responsive UI Improvements

Improve the frontend experience across:

* Desktop
* Tablet
* Mobile

### 🔔 Notifications

Add notifications for events such as:

* Order confirmation
* Order status updates
* New reviews
* Stock changes

### 📊 Admin Dashboard

Create a dedicated dashboard with:

* Sales statistics
* Order statistics
* Popular products
* Stock information
* User statistics

### 🧪 Expanded Automated Tests

Increase test coverage for:

* Models
* Views
* URLs
* Cart operations
* Authentication
* Orders
* Reviews

### 🔐 Production Security

Before deploying publicly, review and configure:

* `SECRET_KEY`
* `DEBUG`
* `ALLOWED_HOSTS`
* Database configuration
* HTTPS
* Static files
* Media files
* Environment variables

### 🚀 Production Deployment

The project can be extended for deployment using services such as:

* VPS
* Docker
* Cloud hosting
* Managed databases
* Reverse proxies
* Production WSGI/ASGI servers

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you want to contribute:

### 1. Fork the repository

Create your own fork of the project.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR-USERNAME/Django-WebStore.git
```

### 3. Create a feature branch

```bash
git checkout -b feature/your-feature
```

### 4. Make your changes

Implement your feature or fix.

### 5. Run tests

```bash
python manage.py test
```

### 6. Commit your changes

```bash
git add .
git commit -m "Add your feature"
```

### 7. Push the branch

```bash
git push origin feature/your-feature
```

### 8. Open a Pull Request

Create a Pull Request and describe your changes clearly.

---

# 📄 License

No explicit open-source license is currently specified in this repository.

If you intend to distribute or reuse this project publicly, consider adding a `LICENSE` file with the license you want to use.

---

# 👨‍💻 Author

**Mohammad Hossein Khalif**

GitHub:

**[@mohammadhosseinkhalif](https://github.com/mohammadhosseinkhalif)**

Project:

**[Django-WebStore](https://github.com/mohammadhosseinkhalif/Django-WebStore)**

---

# ⭐ Support the Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

It helps the project get more visibility and provides useful feedback for future development.

---

## 📌 Project Summary

Django WebStore is a modular e-commerce project built with Django that demonstrates how a web-based store can be structured using multiple Django applications.

The project currently includes:

```text
Product Management
       │
       ├── Categories
       ├── Brands
       ├── Product Media
       ├── Stock
       ├── Discounts
       └── Product Scores
       
Shopping
       │
       ├── Cart
       └── Orders

User Interaction
       │
       ├── Likes
       └── Reviews

Administration
       │
       └── Django Admin
```

The codebase is structured so that additional e-commerce functionality can be added incrementally as the project evolves.

## 📄 License

Copyright © 2026 Mohammad Hossein Khalif. All Rights Reserved.

This repository is publicly available for portfolio, recruitment,
and educational viewing purposes.

The source code may not be copied, modified, redistributed,
published, or used in commercial or production projects
without prior written permission from the author.

See the [LICENSE](LICENSE) file for the complete terms.
