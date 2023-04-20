from django.core.management.base import BaseCommand
from wiki.models import Category, Product
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Load initial data into the database"

    def handle(self, *args, **options):
        # Create initial categories
        category_names = ["Architectural", "Outdoors", "Componentry"]
        categories = [Category(name=name) for name in category_names]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS("Categories created successfully!"))

        # Create initial products
        product_0001 = Product(
            name="Product 0001",
            description="This is the first product",
            price=100.00,
            category=categories[0],
        )
        product_0002 = Product(
            name="Product 0002",
            description="This is the second product",
            price=200.00,
            category=categories[1],
        )
        product_0003 = Product(
            name="Product 0003",
            description="This is the third product",
            price=300.00,
            category=categories[2],
        )
        product_0004 = Product(
            name="Product 0004",
            description="This is the fourth product",
            price=400.00,
            category=categories[0],
        )
        product_0005 = Product(
            name="Product 0005",
            description="This is the fifth product",
            price=500.00,
            category=categories[1],
        )
        product_0006 = Product(
            name="Product 0006",
            description="This is the sixth product",
            price=600.00,
            category=categories[2],
        )

        Product.objects.bulk_create([product_0001, product_0002, product_0003, product_0004, product_0005, product_0006])
        self.stdout.write(self.style.SUCCESS("Products created successfully!"))


        # Create a superuser if one doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            username = "admin"
            email = "admin@example.com"
            password = "adminpassword"
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("A superuser already exists."))