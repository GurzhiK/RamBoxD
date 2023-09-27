# from django.shortcuts import render, redirect
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth import get_user_model
# from django.utils.http import urlsafe_base64_decode
# from django.http import HttpResponse
# from django.contrib import messages
# from django.utils.encoding import DjangoUnicodeDecodeError, smart_text
# from django.urls import reverse

# User = get_user_model()


# def activation_view(request, uidb64, token):
#     try:
#         # Decode the UID and get the user
#         uid = smart_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)

#         # Check if the token is valid
#         if default_token_generator.check_token(user, token):
#             # Activate the user account
#             user.is_active = True
#             user.save()

#             messages.success(
#                 request, 'Your account has been activated. You can now log in.')
#             # Replace 'login' with the name of your login view.
#             return redirect('login')
#         else:
#             messages.error(request, 'Invalid activation link.')
#             # Redirect to a login page or another appropriate page.
#             return redirect('login')
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist, DjangoUnicodeDecodeError):
#         messages.error(request, 'Invalid activation link.')
#         # Redirect to a login page or another appropriate page.
#         return redirect('login')
