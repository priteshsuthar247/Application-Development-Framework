from django.shortcuts import render, redirect
from .models import Item

# View to list all inventory items
def inventory_list(request):
    query = request.GET.get("q", "")
    items = Item.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    return render(request, "myapp/inventory_list.html", {"items": items})


# View to add an item
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        description = request.POST.get("description", "")

        Item.objects.create(name=name, quantity=quantity, price=price, description=description)
        return redirect("inventory_list")  # Redirect to home after adding

    return render(request, 'myapp/add_item.html')

# View to delete an item
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect("inventory_list")

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.name = request.POST["name"]
        item.quantity = request.POST["quantity"]
        item.price = request.POST["price"]
        item.save()
        return redirect("inventory_list")

    return render(request, "myapp/edit_item.html", {"item": item})