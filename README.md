# Contact Manager - Django Address Book

A full-stack Django web application for managing personal contacts with user authentication, PostgreSQL support for production, and ready for Railway deployment.

## 🎯 Features

- ✅ User authentication (Register, Login, Logout)
- ✅ Fully functional CRUD operations for contacts
- ✅ Search contacts by name, email, or phone
- ✅ Filter contacts by category
- ✅ Mark/unmark contacts as favorites
- ✅ Responsive Bootstrap UI (Mobile + Desktop)
- ✅ Admin panel for managing contacts
- ✅ SQLite for local development
- ✅ PostgreSQL for production (Railway-ready)
- ✅ Environment variables support
- ✅ Automated superuser creation management command

## 📋 Tech Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Server**: Gunicorn
- **Deployment**: Railway
- **Other**: dj-database-url, python-dotenv

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository** (or navigate to the project directory)
```bash
cd ContactList
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example .env file
cp .env.example .env

# Edit .env with your settings (optional for local development)
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser** (Admin account)
```bash
python manage.py create_superuser
```

Or use Django's built-in createsuperuser:
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📱 Project Structure

```
ContactList/
├── ContactList/                 # Project settings
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── contacts/                    # Main app
│   ├── models.py                # Contact model
│   ├── views.py                 # Views (authentication, CRUD)
│   ├── urls.py                  # App URL routing
│   ├── admin.py                 # Django admin configuration
│   ├── migrations/              # Database migrations
│   └── management/
│       └── commands/
│           └── create_superuser.py  # Custom management command
│
├── templates/contacts/          # HTML templates
│   ├── base.html                # Base template with navbar
│   ├── register.html            # Registration page
│   ├── login.html               # Login page
│   ├── dashboard.html           # Dashboard
│   ├── contact_list.html        # Contacts list
│   ├── contact_form.html        # Add/Edit contact form
│   ├── contact_detail.html      # Contact details
│   └── contact_confirm_delete.html  # Delete confirmation
│
├── static/                      # Static files (CSS, JS, images)
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (local)
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── Procfile                     # Railway deployment config
└── README.md                    # This file
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL - for production use Railway)
# Leave empty for SQLite in development
DATABASE_URL=

# Superuser Setup (For Railway deployment)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-secure-password-here
```

## 📚 Available Pages

### Authentication
- **Login**: `/login/` - User login
- **Register**: `/register/` - New user registration
- **Logout**: `/logout/` - User logout

### Dashboard & Contacts
- **Dashboard**: `/` - Main dashboard with statistics and recent contacts
- **Contact List**: `/contacts/` - View all contacts with search and filter
- **Add Contact**: `/contacts/add/` - Create new contact
- **Contact Detail**: `/contacts/<id>/` - View contact details
- **Edit Contact**: `/contacts/<id>/edit/` - Edit contact information
- **Delete Contact**: `/contacts/<id>/delete/` - Delete contact
- **Toggle Favorite**: `/contacts/<id>/toggle-favorite/` - Mark/unmark as favorite (AJAX)

### Admin
- **Admin Panel**: `/admin/` - Django admin interface

## 🔍 Contact Model

```python
class Contact(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    phone = CharField(max_length=20)
    email = EmailField(blank=True)
    address = TextField(blank=True)
    category = CharField(choices=CATEGORY_CHOICES, default='Other')
    is_favorite = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
```

**Categories**: Family, Friend, Work, Emergency, Other

## 🛠️ Management Commands

### Create Superuser
```bash
python manage.py create_superuser
```
Uses environment variables `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`.

### Make Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 🚀 Production Deployment (Railway)

### Prerequisites
- Railway account (https://railway.app)
- GitHub repository with the code

### Deployment Steps

1. **Update settings.py for production** (already configured)
   - `DEBUG` is controlled by environment variable
   - `ALLOWED_HOSTS` is configurable
   - Database uses `dj_database_url` for PostgreSQL

2. **Set environment variables in Railway**
   - `SECRET_KEY`: Generate a strong secret key
   - `DEBUG`: Set to `False`
   - `ALLOWED_HOSTS`: Your Railway domain
   - `DATABASE_URL`: Railway PostgreSQL URL (auto-provided)
   - `DJANGO_SUPERUSER_USERNAME`: Admin username
   - `DJANGO_SUPERUSER_EMAIL`: Admin email
   - `DJANGO_SUPERUSER_PASSWORD`: Admin password

3. **Deploy on Railway**
   - Connect your GitHub repository to Railway
   - Railway will automatically detect the `Procfile`
   - Migrations will run automatically
   - Superuser will be created automatically

4. **Access the application**
   - Your application will be available at `https://your-app.railway.app`

### Procfile Explained
```
web: gunicorn ContactList.wsgi
release: python manage.py migrate && python manage.py create_superuser
```

- `web`: Command to start the Gunicorn server
- `release`: Commands to run before deployment (migrations + superuser)

## 🔒 Security Features

- ✅ CSRF protection enabled
- ✅ Session-based authentication
- ✅ LoginRequiredMixin on all protected views
- ✅ User can only see their own contacts
- ✅ Environment variables for sensitive data
- ✅ DEBUG mode disabled in production
- ✅ ALLOWED_HOSTS configuration for production

## 📝 Usage Examples

### 1. Register a New User
```
1. Navigate to /register/
2. Fill in username, full name, email, and password
3. Click "Create Account"
4. You'll be redirected to login page
```

### 2. Login
```
1. Navigate to /login/
2. Enter username and password
3. Click "Login"
4. You'll be redirected to dashboard
```

### 3. Add a Contact
```
1. Click "Add Contact" in navbar
2. Fill in contact details
3. Select category (Family, Friend, Work, Emergency, Other)
4. Optionally mark as favorite
5. Click "Add Contact"
```

### 4. Search Contacts
```
1. Go to Contacts page
2. Type in search box
3. Search by name, email, or phone
4. Results will update automatically
```

### 5. Filter by Category
```
1. Go to Contacts page
2. Select category from dropdown
3. Click "Search"
4. View contacts in that category
```

## 🧪 Testing

### Test the application locally
```bash
# Start development server
python manage.py runserver

# Visit http://localhost:8000
# Test registration, login, and contact management
```

### Admin Panel
```
URL: http://localhost:8000/admin/
Username: admin
Password: admin123 (from .env)
```

## 🐛 Troubleshooting

### Static files not loading in development
```bash
python manage.py collectstatic --noinput
```

### Database errors
```bash
# Reset migrations (careful in production!)
python manage.py migrate contacts zero
python manage.py migrate contacts
```

### "Load template failed" error
- Ensure `templates/` directory exists in project root
- Check `TEMPLATES` configuration in `settings.py`

### psycopg2 installation issues (Windows)
- For development, use SQLite (default)
- Always use `psycopg2-binary==2.9.9` for production
- Or use pre-built wheels from Unofficial Windows Binaries

## 📞 Features Explained

### Dashboard
- Shows total contacts, favorite count
- Displays recent and favorite contacts
- Quick links to add new contact or view all contacts

### Contact List
- Displays all user contacts in a card layout
- Search functionality across name, email, phone
- Filter by category dropdown
- Toggle favorite status with star icon
- Edit and delete contacts
- Pagination support

### Admin Panel
- View all contacts with user information
- Filter by category and favorite status
- Search contacts
- Add/edit/delete contacts
- Bulk actions

## 📦 Dependencies

See `requirements.txt` for full list:
- Django: Web framework
- gunicorn: Production WSGI server
- dj-database-url: Database URL parsing
- python-dotenv: Environment variable management
- psycopg2-binary: PostgreSQL adapter (production)

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions:
1. Check this README
2. Review Django documentation: https://docs.djangoproject.com
3. Check Railway documentation: https://docs.railway.app

## 🎓 Learning Resources

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- Railway Documentation: https://docs.railway.app/
- PostgreSQL Documentation: https://www.postgresql.org/docs/

---

Happy Contact Managing! 📇
