#!/bin/bash
# ============================================
# ShopZone - Django E-Commerce Setup Script
# CodeAlpha Internship Task 1
# ============================================

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   ShopZone - E-Commerce Setup        ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install django pillow --break-system-packages -q
echo "✅ Django installed!"
echo ""

# Run migrations
echo "🗄️  Setting up database..."
python manage.py makemigrations store
python manage.py migrate
echo "✅ Database ready!"
echo ""

# Load fixture data (15 products)
echo "🛍️  Loading 15 products..."
python manage.py loaddata store/fixtures/initial_data.json
echo "✅ Products loaded!"
echo ""

# Create superuser (admin)
echo "👤 Creating admin user..."
echo "   Username: admin"
echo "   Password: admin123"
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@shopzone.com', 'admin123')
    print('✅ Admin user created!')
else:
    print('✅ Admin user already exists!')
"
echo ""

echo "╔══════════════════════════════════════╗"
echo "║   🚀 SETUP COMPLETE!                 ║"
echo "╠══════════════════════════════════════╣"
echo "║                                      ║"
echo "║   Run:  python manage.py runserver   ║"
echo "║                                      ║"
echo "║   🌐 Main Site: http://127.0.0.1:8000/  ║"
echo "║   ⚙️  Admin:    http://127.0.0.1:8000/admin/ ║"
echo "║                                      ║"
echo "║   Admin Login:                       ║"
echo "║   Username: admin                    ║"
echo "║   Password: admin123                 ║"
echo "║                                      ║"
echo "╚══════════════════════════════════════╝"
echo ""
