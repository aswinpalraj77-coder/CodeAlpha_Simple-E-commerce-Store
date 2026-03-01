# 🛍️ ShopZone — E-Commerce Website
### CodeAlpha Full Stack Internship — Task 1

![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)
![HTML CSS JS](https://img.shields.io/badge/Frontend-HTML%20CSS%20JS-orange?style=for-the-badge&logo=html5)

---

## 📌 About The Project

**ShopZone** is a full-stack e-commerce web application built using **Python (Django)** for the backend and **HTML, CSS, JavaScript** for the frontend. This project was developed as part of the **CodeAlpha Full Stack Development Internship — Task 1**.

It includes a fully functional shopping experience with product listings, cart management, user authentication, order processing, and an admin panel.

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/aswinpalraj77-coder/CodeAlpha_SimpleEcommerceStore.git
cd CodeAlpha_SimpleEcommerceStore/ecshop

# 2. Install dependencies
pip install django pillow

# 3. Setup database + load 15 products
python manage.py makemigrations store
python manage.py migrate
python manage.py loaddata store/fixtures/initial_data.json

# 4. Create admin user
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

Open: **http://127.0.0.1:8000/**

---

## 🔑 Admin Panel

| | |
|---|---|
| **URL** | http://127.0.0.1:8000/admin/ |
| **Username** | *aswin* |
| **Password** | *aswin@2007* |

---

## ✅ Features

| Feature | Description |
|--------|-------------|
| 🏠 Home Page | Product listings with hero section & stats |
| 🔍 Search | Search products by name in real-time |
| 🏷️ Categories | Filter by Electronics, Fashion, Home & Living, Sports, Books |
| 📦 15 Products | With real images from Unsplash |
| 🛒 Shopping Cart | Add, remove, update quantities |
| 👤 User Auth | Register, Login, Logout |
| 💳 Checkout | Order placement with delivery address |
| 📋 My Orders | Full order history for each user |
| ⚙️ Admin Panel | Manage products, categories, orders & users |

---

## 📁 Project Structure

```
ecshop/
├── ecommerce/                  # Main Django project config
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Root URL config
│   └── wsgi.py
├── store/                      # Main app
│   ├── models.py               # Product, Category, Order, OrderItem
│   ├── views.py                # All page views & logic
│   ├── urls.py                 # App URL routes
│   ├── admin.py                # Admin panel customization
│   ├── templates/
│   │   └── store/
│   │       ├── base.html       # Base layout (navbar, footer)
│   │       ├── home.html       # Home + product grid
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       ├── auth.html       # Login & Register
│   │       ├── order_success.html
│   │       └── my_orders.html
│   ├── fixtures/
│   │   └── initial_data.json   # 15 products seed data
│   └── migrations/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python 3.13 + Django 5.0 |
| Database | SQLite (built-in) |
| Auth | Django Built-in Authentication |
| Styling | Custom CSS + Google Fonts (Bebas Neue, DM Sans) |
| Images | Unsplash |

---

## 📞 Contact

| | |
|---|---|
| 👤 **Name** | Aswin Pal Raj |
| 📧 **Email** | [aswinpalraj77@gmail.com](mailto:aswinpalraj77@gmail.com) |
| 💼 **LinkedIn** | [linkedin.com/in/aswin-pal-raj-959ab4350](https://www.linkedin.com/in/aswin-pal-raj-959ab4350) |
| 🐙 **GitHub** | [github.com/aswinpalraj77-coder](https://github.com/aswinpalraj77-coder) |

---

> Built with ❤️ by **Aswin Pal Raj** for **CodeAlpha Internship**
