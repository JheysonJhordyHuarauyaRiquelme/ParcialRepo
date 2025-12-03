products = []
current_id = 1


def get_all_products():
    return products


def get_product(id: int):
    for p in products:
        if p["id"] == id:
            return p
    return None


def create_product(data: dict):
    global current_id
    data["id"] = current_id
    current_id += 1
    products.append(data)
    return data


def update_product(id: int, data: dict):
    for i, p in enumerate(products):
        if p["id"] == id:
            data["id"] = id
            products[i] = data
            return data
    return None


def delete_product(id: int):
    for i, p in enumerate(products):
        if p["id"] == id:
            del products[i]
            return True
    return False
