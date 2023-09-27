from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.encoding import DjangoUnicodeDecodeError, force_str

User = get_user_model()


def activate_account(request, uidb64, token):
    try:
        # Decode the UID and get the user
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        # Check if the token is valid
        if default_token_generator.check_token(user, token):
            # Activate the user account
            user.is_active = True
            user.save()

            messages.success(
                request, 'Your account has been activated. You can now log in.')
            # Redirect to a success page or any other appropriate page.
            # Replace with your success page.
            return redirect('account_activated')
        else:
            messages.error(request, 'Invalid activation link.')
            # Redirect to an error page or any other appropriate page.
            # Replace with your error page.
            return redirect('activation_error')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, DjangoUnicodeDecodeError):
        messages.error(request, 'Invalid activation link.')
        # Redirect to an error page or any other appropriate page.
        return redirect('activation_error')  # Replace with your error page.


def account_activated(request):
    return render(request, 'account_activated.html')


def activation_error(request):
    # Replace 'activation_error.html' with the actual template name.
    return render(request, 'activation_error.html')
