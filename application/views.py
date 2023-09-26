import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, ContactData
from django.db.models import Count, Min, Avg, Sum, Max


def home(request):
    return render(request, "home.html")


def generate_users(request):
    for _ in range(10):
        first_name = "User" + str(random.randint(1, 100))
        last_name = "Last" + str(random.randint(1, 100))
        age = random.randint(18, 60)
        Contact.objects.create(first_name=first_name, last_name=last_name, age=age)

    return HttpResponse("Сгенерировано 10 случайных пользователей.")


def statistics(request):
    contact_data_count = ContactData.objects.values("data").annotate(count=Count("data")).count()

    max_duplicate_data_count = (
        ContactData.objects.values("data").annotate(count=Count("data")).order_by("-count").first()
    )

    if max_duplicate_data_count:
        max_duplicate_data_count = max_duplicate_data_count["count"]
    else:
        max_duplicate_data_count = 0

    most_common_first_name = Contact.objects.values("first_name").annotate(count=Count("id")).order_by("-count").first()
    youngest_contact = Contact.objects.aggregate(youngest_age=Min("age"))
    oldest_contact = Contact.objects.aggregate(oldest_age=Max("age"))
    average_age = Contact.objects.aggregate(average_age=Avg("age"))
    total_age = Contact.objects.aggregate(total_age=Sum("age"))

    context = {
        "most_common_first_name": most_common_first_name,
        "youngest_contact": youngest_contact,
        "average_age": average_age,
        "total_age": total_age,
        "contact_data_count": contact_data_count,
        "max_duplicate_data_count": max_duplicate_data_count,
        "oldest_contact": oldest_contact,
    }

    return render(request, "statistics.html", context)


def view_users(request):
    users = Contact.objects.annotate(data_count=Count("contact_data"))

    context = {
        "users": users,
    }

    return render(request, "view_users.html", context)
