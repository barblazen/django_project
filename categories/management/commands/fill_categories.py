from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from categories.models import Category


class Command(BaseCommand):
    help = "Заполняет таблицу Category из списка"
    CATEGORIES = [
        "Технологии",
        "Наука",
        "Искусство",
        "Музыка",
        "Спорт",
        "Литература",
        "Образование",
        "Здоровье",
        "Кулинария",
        "Путешествия"
    ]

    def handle(self, *args, **options):
        created_count = 0
        for name in self.CATEGORIES:
            category, created = Category.objects.get_or_create(name=name)
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Добавлено {created_count} новых категорий"))



