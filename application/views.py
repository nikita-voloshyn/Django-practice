from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import random
from django.db.models import Count, Min, Avg, Sum


def home(request):
    return render(request, "home.html")


def generate_users():
    for _ in range(10):
        first_name = "User" + str(random.randint(1, 100))
        last_name = "Last" + str(random.randint(1, 100))
        age = random.randint(18, 60)
        Contact.objects.create(first_name=first_name, last_name=last_name, age=age)

    return HttpResponse("Сгенерировано 10 случайных пользователей.")


def statistics(request):
    # Получаем данные для статистики
    most_common_first_name = Contact.objects.values("first_name").annotate(count=Count("id")).order_by("-count").first()
    youngest_contact = Contact.objects.aggregate(youngest_age=Min("age"))
    average_age = Contact.objects.aggregate(average_age=Avg("age"))
    total_age = Contact.objects.aggregate(total_age=Sum("age"))

    context = {
        "most_common_first_name": most_common_first_name,
        "youngest_contact": youngest_contact,
        "average_age": average_age,
        "total_age": total_age,
    }

    return render(request, "statistics.html", context)


def view_users(request):
    users = Contact.objects.all()

    context = {
        "users": users,
    }

    return render(request, "view_users.html", context)
