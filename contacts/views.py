from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from .models import Contact
from django.http import JsonResponse
import json


# ==================== Authentication Views ====================

def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name', '')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'All fields are required')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name
        )
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'contacts/register.html')


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    
    return render(request, 'contacts/login.html')


def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


# ==================== Dashboard & List Views ====================

@login_required(login_url='login')
def dashboard(request):
    """Dashboard view showing summary and recent contacts"""
    user = request.user
    total_contacts = Contact.objects.filter(user=user).count()
    favorite_contacts = Contact.objects.filter(user=user, is_favorite=True)
    recent_contacts = Contact.objects.filter(user=user)[:5]
    
    context = {
        'total_contacts': total_contacts,
        'favorite_count': favorite_contacts.count(),
        'recent_contacts': recent_contacts,
        'favorite_contacts': favorite_contacts,
    }
    
    return render(request, 'contacts/dashboard.html', context)


class ContactListView(LoginRequiredMixin, ListView):
    """List all contacts for the logged-in user"""
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10
    login_url = 'login'
    
    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user)
        
        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query)
            )
        
        # Filter by category
        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filter by favorite
        show_favorites = self.request.GET.get('favorites', '')
        if show_favorites == 'true':
            queryset = queryset.filter(is_favorite=True)
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['categories'] = Contact.CATEGORY_CHOICES
        return context


# ==================== CRUD Views ====================

class ContactCreateView(LoginRequiredMixin, CreateView):
    """Create a new contact"""
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'phone', 'email', 'address', 'category', 'is_favorite']
    success_url = reverse_lazy('contact_list')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Contact created successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Contact'
        context['button_text'] = 'Add Contact'
        return context


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing contact"""
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'phone', 'email', 'address', 'category', 'is_favorite']
    success_url = reverse_lazy('contact_list')
    login_url = 'login'
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Contact updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Contact'
        context['button_text'] = 'Update Contact'
        return context


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a contact"""
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')
    login_url = 'login'
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Contact deleted successfully!')
        return super().delete(request, *args, **kwargs)


class ContactDetailView(LoginRequiredMixin, DetailView):
    """View contact details"""
    model = Contact
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'
    login_url = 'login'
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


# ==================== AJAX Views ====================

@login_required(login_url='login')
def toggle_favorite(request, pk):
    """Toggle favorite status via AJAX"""
    contact = get_object_or_404(Contact, id=pk, user=request.user)
    contact.is_favorite = not contact.is_favorite
    contact.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'is_favorite': contact.is_favorite})
    
    return redirect('contact_list')
