import os
import json

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")

import django

django.setup()

from restaurant.models import Menu


def import_menu_data():
    # Load menu data from the JSON file
    with open('menu.json', 'r') as json_file:
        menu_data = json.load(json_file)

    # Iterate through menu items and create Menu instances
    for item in menu_data['menu']:
        menu = Menu(
            title=item['title'],
            price=float(item['price']),
            inventory=int(item['inventory'])
        )
        menu.save()


if __name__ == '__main__':
    import_menu_data()
