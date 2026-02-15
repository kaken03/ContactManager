# Getting Started with Contact Manager

Quick setup guide to get the application running in 5 minutes!

## 🚀 Quick Start (5 minutes)

### 1. Activate Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Admin Account
```bash
python manage.py create_superuser
```
Or use the auto-creation with .env:
```bash
python manage.py create_superuser
```

### 5. Start Development Server
```bash
python manage.py runserver
```

### 6. Open in Browser
```
http://localhost:8000
```

## 📝 Default Credentials (from .env)

```
Username: admin
Password: admin123
```

## 🔗 URLs Quick Reference

| URL | Purpose |
|-----|---------|
| `http://localhost:8000/` | Dashboard |
| `http://localhost:8000/register/` | Register new account |
| `http://localhost:8000/login/` | Login |
| `http://localhost:8000/contacts/` | View all contacts |
| `http://localhost:8000/contacts/add/` | Add new contact |
| `http://localhost:8000/admin/` | Admin panel |

## ✅ What to Test

### 1. Register New User
- Click "Register" in navbar
- Create account with username and email
- Should redirect to login

### 2. Login
- Use registered credentials or admin/admin123
- Should redirect to dashboard

### 3. Add Contact
- Click "Add Contact" in navbar
- Fill in contact details
- Select category
- Save

### 4. Search Contacts
- Go to Contacts page
- Type in search box (name, email, or phone)
- Results should filter in real-time

### 5. Filter by Category
- Go to Contacts page
- Select category from dropdown
- Click Search
- Should show only contacts in that category

### 6. Mark as Favorite
- Click star icon on any contact
- Should toggle favorite status

### 7. Edit Contact
- Click "Edit" on any contact
- Modify details
- Click "Update Contact"

### 8. Delete Contact
- Click "Delete" on any contact
- Confirm deletion
- Contact should be removed

### 9. Admin Panel
- Go to http://localhost:8000/admin/
- Login with admin credentials
- Should see Contact management interface

## 🎨 Customization Ideas

### Change Colors
Edit `templates/contacts/base.html`:
```css
--primary-color: #0d6efd;  /* Change to your color */
```

### Add More Categories
Edit `contacts/models.py`:
```python
CATEGORY_CHOICES = [
    ('Family', 'Family'),
    ('Your New Category', 'Your New Category'),
    ...
]
```

### Add Contact Fields
1. Edit `contacts/models.py` - add new field
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Update templates and forms

## 🐛 Common Issues

### "Page not found" after register
- Make sure migrations were run
- Check database exists: `db.sqlite3`
- Try `python manage.py migrate`

### Static files not loading (images/CSS)
```bash
python manage.py collectstatic
```

### Can't login
1. Check username/password in admin
2. Go to http://localhost:8000/admin/
3. Click "Users"
4. Reset password if needed

### Contact not saving
1. Check browser console for errors (F12)
2. Check terminal for Django errors
3. Ensure all required fields are filled

## 📚 Learn More

- Full README: Read `README.md`
- Deployment Guide: Read `DEPLOYMENT.md`
- Django Docs: https://docs.djangoproject.com/
- Bootstrap Docs: https://getbootstrap.com/docs/

## 💡 Tips

1. **Use the admin panel** - Great way to manage contacts without UI
2. **Check browser console** - F12 to see any JavaScript errors
3. **Watch terminal** - Django errors appear in terminal window
4. **Use search** - Most powerful feature for finding contacts
5. **Set favorites** - Star your most important contacts

## 🚀 Next Steps

1. ✅ Test the application locally (you're here!)
2. 📝 Add more contacts and test features
3. 🎨 Customize colors and styling
4. 🚢 Deploy to Railway (see DEPLOYMENT.md)
5. 📱 Share with friends!

---

**Need help?** Check README.md or DEPLOYMENT.md for more details!
