from django.core.management.base import BaseCommand
from wiki.models import Category
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Load initial data into the database"

    def handle(self, *args, **options):
        # Create initial categories
        category_names = ["Architectural", "Outdoors", "Componentry"]
        categories = [Category(name=name) for name in category_names]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS("Categories created successfully!"))

        # Create a superuser if one doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            username = "admin"
            email = "admin@example.com"
            password = "adminpassword"
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("A superuser already exists."))