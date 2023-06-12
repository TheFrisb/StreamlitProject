from django.core.mail import EmailMessage
from decouple import config




def format_email_html_content(title, html_content): # this function formats the html content of the email and makes it html compliant
    valid_html = '''
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{title}</title>
                    <style>
                        /* Inline CSS styles for email compatibility */
                        body {{
                        margin: 0;
                        padding: 0;
                        font-family: Arial, sans-serif;
                        }}
                    </style>
                    </head>
                <body>
                    <div>
                        {html_content}
                    </div>
                </body>
                </html>'''.format(title=title, html_content=html_content)
    return valid_html


def send_user_confirmation_mail(user, registration_link_ob): # this function sends the user a confirmation email when he creates a new user
    title = 'Welcome to the shop!'
    user_email = str(user.email)
    html_content = '''
                    <h1>Thank you for registering!</h1>
                    <p>Please confirm your email address by clicking on the link below:</p>
                    <a href="{registration_link}" style="padding:8px;background-color:blue;color:white;text-decoration:none!important;margin-bottom:16px;">Confirm email</a>
                    <p>If the link does not work, please copy and paste it in your address bar: {registration_link}</p>
                    <p>Thank you!</p>
                    '''.format(registration_link=registration_link_ob.link)
    valid_html = format_email_html_content(title, html_content)
    email = EmailMessage(
        subject=title,
        body=valid_html,
        to=[user_email],
    )
    # EmailMessage is the default Django email class
    email.content_subtype = "html" # this is required for the email to be sent as html
    email.send() # this sends the email
    return True


def send_contact_message(from_mail, message):
    title = 'Contact message from the shop'
    admin_mail = config('ADMIN_EMAIL') # this is the email address of the admin where the contact form sends the mail to
    html_content = '''
                    <h1>Message from {user_email}</h1>
                    <p>{message}</p>
                    '''.format(user_email=str(from_mail), message=str(message))
    valid_html = format_email_html_content(title, html_content)
    email = EmailMessage(
        subject=title,
        body=valid_html,
        to=[admin_mail],
    )
    email.content_subtype = "html"
    email.send()
    return True


def new_orderItem_mail(orderItem):
    title = 'New Order'
    user_email = str(orderItem.user.email)
    html_content = '''
    <h1>You have successfully purchased {use_count} credits
    '''.format(use_count = orderItem.use_count)
    valid_html = format_email_html_content(title, html_content)
    
    email = EmailMessage(
        subject=title,
        body=valid_html,
        to=[user_email],
    )
    # EmailMessage is the default Django email class
    email.content_subtype = "html" # this is required for the email to be sent as html
    email.send() # this sends the email
    return True


def notify_user_for_credit_spent(userProfile):
    title = 'New Order'
    if userProfile.user.email != '':
        user_email = userProfile.user.email
    else:
        return False
    html_content = '''
    <h1>You have successfully accesed the dashboard</h1>
    <p>You now have {credits_balance} credits left
    '''.format(credits_balance = userProfile.credits_balance)
    valid_html = format_email_html_content(title, html_content)
    
    email = EmailMessage(
        subject=title,
        body=valid_html,
        to=[user_email],
    )
    # EmailMessage is the default Django email class
    email.content_subtype = "html" # this is required for the email to be sent as html
    email.send() # this sends the email
    return True





