from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = {
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='Account_Management/password_reset.html'), name='password_reset'), #submit email form
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='Account_Management/password_reset_sent.html'), name='password_reset_done'), #Email sent success message
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Account_Management/password_reset_form.html'), name='password_reset_confirm'), #Link to password reset form in email 
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='Account_Management/password_reset_done.html'), name='password_reset_complete'), #Password successfully changed message
}