# 🛍️ ShopZone — E-Commerce Website
### CodeAlpha Full Stack Internship — Task 1

---

## 🚀 Quick Start (3 Commands Only!)

```bash
# 1. Install dependencies
pip install django pillow

# 2. Run setup (database + 15 products + admin user)
bash setup.sh

# 3. Start server
python manage.py runserver
```

Then open: **http://127.0.0.1:8000/**

---

## 🔑 Admin Panel

URL: `http://127.0.0.1:8000/admin/`  
Username: `admin`  
Password: `admin123`

---

## ✅ Features

- 🏠 **Home Page** — Product listings with hero section
- 🔍 **Search** — Search products by name
- 🏷️ **Categories** — Filter by Electronics, Fashion, Home & Living, Sports, Books
- 📦 **15 Products** — With real images from Unsplash
- 🛒 **Shopping Cart** — Add, remove, update quantities
- 👤 **User Auth** — Register, Login, Logout
- 💳 **Checkout** — Order placement with address
- 📋 **My Orders** — Order history for users
- ⚙️ **Admin Panel** — Full Django admin to manage products/orders

---

## 📁 Project Structure

```
ecshop/
├── ecommerce/          # Main Django project settings
│   ├── settings.py
│   └── urls.py
├── store/              # Main app
│   ├── models.py       # Product, Category, Order, OrderItem
│   ├── views.py        # All page views
│   ├── urls.py         # URL routes
│   ├── admin.py        # Admin panel config
│   ├── templates/store/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── auth.html
│   │   ├── order_success.html
│   │   └── my_orders.html
│   └── fixtures/
│       └── initial_data.json   # 15 products data
├── manage.py
├── requirements.txt
├── setup.sh            # Auto setup script
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python + Django |
| Database | SQLite (built-in) |
| Auth | Django Built-in Auth |
| Styling | Custom CSS with Google Fonts |

---

Built with ❤️ for CodeAlpha Internship
