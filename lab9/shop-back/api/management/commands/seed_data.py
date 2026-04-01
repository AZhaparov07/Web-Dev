"""
Management command: python manage.py seed_data
Creates 4 categories and 20 products for Lab 9.
"""

from django.core.management.base import BaseCommand
from api.models import Category, Product


CATEGORIES = [
    {"name": "Electronics", "description": "Gadgets, devices and consumer electronics"},
    {"name": "Clothing", "description": "Men's, women's and children's apparel"},
    {"name": "Books", "description": "Fiction, non-fiction, textbooks and more"},
    {"name": "Sports & Outdoors", "description": "Equipment and gear for sports and outdoor activities"},
]

PRODUCTS = [
    # Electronics (8 products)
    {"name": "Wireless Headphones", "description": "Noise-cancelling over-ear headphones", "price": "129.99", "stock": 50, "category": "Electronics"},
    {"name": "Mechanical Keyboard", "description": "RGB backlit mechanical keyboard", "price": "89.99", "stock": 30, "category": "Electronics"},
    {"name": "USB-C Hub", "description": "7-in-1 multiport USB-C hub", "price": "39.99", "stock": 100, "category": "Electronics"},
    {"name": "Webcam HD", "description": "1080p webcam with built-in microphone", "price": "59.99", "stock": 45, "category": "Electronics"},
    {"name": "Portable SSD", "description": "500GB portable solid-state drive", "price": "74.99", "stock": 60, "category": "Electronics"},
    {"name": "Smart Watch", "description": "Fitness tracking smart watch", "price": "199.99", "stock": 25, "category": "Electronics"},
    {"name": "Bluetooth Speaker", "description": "Waterproof portable Bluetooth speaker", "price": "49.99", "stock": 80, "category": "Electronics"},
    {"name": "LED Desk Lamp", "description": "Adjustable LED lamp with USB charging port", "price": "34.99", "stock": 70, "category": "Electronics"},
    # Clothing (4 products)
    {"name": "Classic White T-Shirt", "description": "100% cotton unisex white t-shirt", "price": "19.99", "stock": 200, "category": "Clothing"},
    {"name": "Denim Jeans", "description": "Slim-fit denim jeans in dark wash", "price": "59.99", "stock": 120, "category": "Clothing"},
    {"name": "Hooded Sweatshirt", "description": "Pullover hoodie in fleece fabric", "price": "44.99", "stock": 90, "category": "Clothing"},
    {"name": "Running Shoes", "description": "Lightweight mesh running shoes", "price": "84.99", "stock": 55, "category": "Clothing"},
    # Books (4 products)
    {"name": "Clean Code", "description": "A handbook of agile software craftsmanship by Robert C. Martin", "price": "29.99", "stock": 40, "category": "Books"},
    {"name": "The Pragmatic Programmer", "description": "Your journey to mastery by Hunt & Thomas", "price": "34.99", "stock": 35, "category": "Books"},
    {"name": "Python Crash Course", "description": "A hands-on, project-based introduction to programming", "price": "24.99", "stock": 60, "category": "Books"},
    {"name": "Dune", "description": "Science fiction novel by Frank Herbert", "price": "14.99", "stock": 75, "category": "Books"},
    # Sports & Outdoors (4 products)
    {"name": "Yoga Mat", "description": "Non-slip 6mm thick yoga mat", "price": "27.99", "stock": 100, "category": "Sports & Outdoors"},
    {"name": "Resistance Bands Set", "description": "Set of 5 resistance bands for strength training", "price": "21.99", "stock": 150, "category": "Sports & Outdoors"},
    {"name": "Water Bottle 1L", "description": "Stainless steel insulated water bottle", "price": "17.99", "stock": 200, "category": "Sports & Outdoors"},
    {"name": "Hiking Backpack", "description": "35L waterproof hiking backpack", "price": "69.99", "stock": 40, "category": "Sports & Outdoors"},
]


class Command(BaseCommand):
    help = "Seed database with 4 categories and 20 products"

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        cat_map = {}
        for cat_data in CATEGORIES:
            cat, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={"description": cat_data["description"]},
            )
            cat_map[cat.name] = cat
            status = "created" if created else "already exists"
            self.stdout.write(f"  Category '{cat.name}' — {status}")

        for prod_data in PRODUCTS:
            category = cat_map[prod_data["category"]]
            prod, created = Product.objects.get_or_create(
                name=prod_data["name"],
                defaults={
                    "description": prod_data["description"],
                    "price": prod_data["price"],
                    "stock": prod_data["stock"],
                    "category": category,
                },
            )
            status = "created" if created else "already exists"
            self.stdout.write(f"  Product '{prod.name}' — {status}")

        self.stdout.write(self.style.SUCCESS("Done! 4 categories and 20 products seeded."))
