from django.shortcuts import render
from loguru import logger
from .main import get_destanations, get_blog, post_req
from .forms import UserForm, Subscribe_form


@logger.catch
def home(response) -> render:
    """Отображение Домашней страницы"""

    form = UserForm(response.POST)
    if response.method == 'POST':
        if 'subscribe' in response.POST:
            post_req(response=response, type="subscribe")
        else:
            post_req(response=response, type="new_order")
    else:
        form = UserForm()
    dest_data = get_destanations()
    blog_data = get_blog()
    return render(response, "main/index.html", {"dest_data": dest_data, "blog_data": blog_data, "form": form})
