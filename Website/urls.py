from django.urls import path
from django.contrib import admin
from Website import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("category/<slug:val>/", views.Categoryview.as_view(), name="category"),
    path("categorytitle/<val>/", views.CategoryTitle.as_view(), name="categorytitle"),
    path("productdetail/<int:id>/", views.Productdetail.as_view(), name="productdetail"),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateaddress/<int:pk>', views.UpdateAddress.as_view(), name='updateaddress'),

    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.check_out.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name="orders"),

    path('search/',views.search,name='search'),
    
    path('pluscart/',views.plus_cart,name='plus_cart'),
    path('minuscart/',views.minus_cart,name='minus_cart'),
    path('removecart/',views.remove_cart,name='remove_cart'),

    path('pluswishlist/',views.plus_wishlist,name='plus_wishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minus-wishlist'),



    # Authentication URLs
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name='website/login.html', authentication_form=LoginForm), name='login'),
    
    # Password Reset URLs
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='website/passwordreset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='website/passwordresetdone.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='website/passwordresetconfirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='website/passwordresetcomplete.html'), name='password_reset_complete'),

    path('logout/',views.logout,name='logout'),
    
    # Change Password URLs
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='website/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='website/passwordchangedone.html'), name='passwordchangedone'),

    # Static and Media Files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'First Step'
admin.site.site_title = 'First Step'
admin.site.site_index_title = "Welcome to First step"