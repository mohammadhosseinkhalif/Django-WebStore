import jdatetime
from PIL import Image

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.urls import reverse_lazy

from shop.models import Product
from django.contrib.auth.models import User
from .models import Profile
from .forms import (
    UpdateUsernameForm,
    UpdateProfileForm,
    ChangePasswordForm,
    UserLoginForm,
    UserSignUpForm,
)


# ----- Helpers -----

def jalali_date(date):
    """Convert a Gregorian datetime to a Jalali date string."""
    if not date:
        return ""
    return jdatetime.datetime.fromgregorian(datetime=date).strftime("%Y/%m/%d")


# ----- Profile views (class‑based) -----

class SelfProfileView(TemplateView):
    """View for the logged‑in user's own profile page."""
    template_name = 'profile//self_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context.update({
            'user': user,
            'profile': profile,
            'date_joined': jalali_date(user.date_joined),
        })
        return context


class ProfileDetailView(DetailView):
    """View for another user's public profile page."""
    model = User
    template_name = 'profile/profile.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        profile = get_object_or_404(Profile, user=user)
        context.update({
            'profile': profile,
            'date_joined': jalali_date(user.date_joined),
        })
        return context


class InterestsListView(ListView):
    """List all products liked by the current user."""
    model = Product
    template_name = 'profile//interests.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(likes__user=self.request.user)


class SettingsView(TemplateView):
    """User settings dashboard."""
    template_name = 'profile//settings.html'


class UpdateUsernameView(FormView):
    """Update the username with password confirmation."""
    form_class = UpdateUsernameForm
    template_name = 'profile//update_username.html'
    success_url = reverse_lazy('settings_view')

    def form_valid(self, form):
        user = self.request.user
        password = form.cleaned_data.get('password')
        if check_password(password, user.password):
            user.username = form.cleaned_data['username']
            user.save(update_fields=['username'])
            messages.success(self.request, 'نام کاربری با موفقیت تغییر کرد')
            return super().form_valid(form)
        else:
            form.add_error('password', 'رمز عبور وارد شده صحیح نیست.')
            return self.form_invalid(form)


class UpdateProfileView(FormView):
    """Update first name, last name, and email with password confirmation."""
    form_class = UpdateProfileForm
    template_name = 'profile//update_profile.html'
    success_url = reverse_lazy('settings_view')

    def get_initial(self):
        user = self.request.user
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }

    def form_valid(self, form):
        user = self.request.user
        password = form.cleaned_data.get('password')
        if check_password(password, user.password):
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(self.request, 'اطلاعات با موفقیت ویرایش شد')
            return super().form_valid(form)
        else:
            form.add_error('password', 'رمز عبور وارد شده صحیح نیست.')
            return self.form_invalid(form)


class ChangePasswordView(FormView):
    """Change the user's password with current password verification."""
    form_class = ChangePasswordForm
    template_name = 'profile//update_password.html'
    success_url = reverse_lazy('settings_view')

    def form_valid(self, form):
        user = self.request.user
        current_password = form.cleaned_data['current_password']
        if check_password(current_password, user.password):
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            messages.success(self.request, 'رمز عبور جدید ذخیره شد')
            return super().form_valid(form)
        else:
            form.add_error('current_password', 'رمز عبور فعلی صحیح نیست.')
            return self.form_invalid(form)


# ----- File upload views (function‑based) -----

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@login_required
def upload_avatar(request):
    """Handle AJAX avatar image upload."""
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    avatar = request.FILES.get("avatar")
    if not avatar:
        messages.error(request, "عکس پروفایل ارسال نشده است.")
        return JsonResponse({"error": "عکس پروفایل ارسال نشده است."}, status=400)

    if avatar.size > MAX_FILE_SIZE:
        messages.error(request, "حجم عکس پروفایل نباید بیشتر از 10 مگابایت باشد.")
        return JsonResponse({"error": "حجم عکس پروفایل نباید بیشتر از 10 مگابایت باشد."}, status=400)

    # Validate image integrity
    try:
        image = Image.open(avatar)
        image.verify()
    except Exception:
        messages.error(request, "فایل ارسال شده یک تصویر معتبر نیست.")
        return JsonResponse({"error": "فایل ارسال شده یک تصویر معتبر نیست."}, status=400)

    prf = Profile.objects.get(user=request.user)
    prf.avatar = avatar
    prf.save()

    messages.success(request, "عکس ذخیره شد")
    return JsonResponse({
        "success": True,
        "message": "عکس پروفایل با موفقیت ذخیره شد.",
        "image_url": prf.avatar.url,
    })


@login_required
def upload_banner(request):
    """Handle AJAX banner image upload."""
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    banner = request.FILES.get("banner")
    if not banner:
        messages.error(request, "عکس بنر ارسال نشده است.")
        return JsonResponse({"error": "عکس بنر ارسال نشده است."}, status=400)

    if banner.size > MAX_FILE_SIZE:
        messages.error(request, "حجم بنر نباید بیشتر از 10 مگابایت باشد.")
        return JsonResponse({"error": "حجم بنر نباید بیشتر از 10 مگابایت باشد."}, status=400)

    # Validate image integrity
    try:
        image = Image.open(banner)
        image.verify()
    except Exception:
        messages.error(request, "فایل ارسال شده یک تصویر معتبر نیست.")
        return JsonResponse({"error": "فایل ارسال شده یک تصویر معتبر نیست."}, status=400)

    prf = Profile.objects.get(user=request.user)
    prf.banner = banner
    prf.save()

    messages.success(request, "عکس ذخیره شد")
    return JsonResponse({
        "success": True,
        "message": "بنر با موفقیت ذخیره شد.",
        "image_url": prf.banner.url,
    })


@login_required
@require_POST
def update_description(request):
    """Update the user's profile description via AJAX."""
    description = request.POST.get('description', '').strip()
    prf = Profile.objects.get(user=request.user)
    prf.description = description
    prf.save(update_fields=['description'])
    messages.success(request, 'توضیحات پروفایل با موفقیت ذخیره شد.')
    return JsonResponse({'success': True})


# ----- Authentication views (function‑based) -----

def login_user(request):
    """Log in an existing user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'ورود با موفقیت انجام شد!')
            return redirect('home')
        else:
            messages.error(request, 'ورود انجام نشد!')
            return redirect('home')
    return render(request, 'profile//login.html', {'form': UserLoginForm})


def logout_user(request):
    """Log out the current user."""
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد!')
    return redirect('home')


def signup_user(request):
    """Register a new user account."""
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد!')
            return redirect('home')
        messages.error(request, 'اطلاعات وارد شده صحیح نیست.')
    else:
        form = UserSignUpForm()
    return render(request, 'profile//signup.html', {'form': form})


def delete_account(request):
    """Confirm and delete the user's account."""
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "no":
            return redirect("settings_view")
        if action == "yes":
            user = request.user
            user.delete()
            logout(request)
            return redirect("settings_view")
    return render(request, "profile//delete_account.html")