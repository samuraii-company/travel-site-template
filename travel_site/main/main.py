from .models import Destinations, Blog
from .forms import UserForm
from .models import UserData, Subscirbe_Emails
from .views import logger
from django.http import JsonResponse


def get_destanations():

    dest_data = Destinations.objects.all()
    return dest_data


def get_blog():

    blog_data = Blog.objects.all()
    return blog_data


def post_req(response, type) -> JsonResponse:
    match type:
        case "new_order":
            save_data_to_db(response=response)
        case "subscribe":
            subscribe_emails(response=response)


def save_data_to_db(response):

    name = response.POST.get("username", "")
    phone_number = response.POST.get("phone_number", "")
    email = response.POST.get("email", "")
    t = UserData(name=name, phone_number=phone_number, email=email)
    t.save()
    logger.info("Data was saved")


def subscribe_emails(response):
    email = response.POST.get("email_subscribe", "")
    t = Subscirbe_Emails(email=email)
    t.save()
    logger.info("Data was saved")
