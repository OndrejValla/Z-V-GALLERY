from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """ A view to return the contact page """

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # Send email to customer
            cust_email = request.POST['email']
            full_name = request.POST['full_name']
            message = request.POST['message']
            subject = ('We have received your message with subject: ' +
                       request.POST['subject'])
            body = render_to_string('contact/confirmation_emails/' +
                                    'customer_confirmation_email.txt',
                                    {'full_name': full_name,
                                        'subject': subject,
                                        'message': message,
                                     })

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email],
                fail_silently=False,
            )

            # Send message to admin
            admin_mail = settings.DEFAULT_FROM_EMAIL
            subject = contact_form.cleaned_data['subject']
            body = render_to_string('contact/confirmation_emails/' +
                                    'admin_confirmation_email.txt',
                                    {'full_name': full_name,
                                        'subject': subject,
                                        'message': message,
                                        'cust_email': cust_email,
                                     })

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [admin_mail],
                fail_silently=False,
            )
            # Save message to database
            contact_form.save()

            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            try:
                contact_form = ContactForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'subject': '',
                    'message': '',
                })

            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

        context = {
            'form': contact_form,
            'on_profile_page': True,
        }

        return render(request, 'contact/contact.html', context)
