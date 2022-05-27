from requests import get
from zombie.models import Item

url = "https://zombie-items-api.herokuapp.com/api/items"


with get(url) as items:
    for item in items.json().get("items"):
        Item.objects.create(name=item.get("name"), price_pln=item.get("price"))
