import json

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, path, product):
        self.products.append((path, product))

    def search_products(self, query):
        results = []
        for path, product in self.products:
            if any(query.lower() in part.lower() for part in path) or query.lower() in product['name'].lower() or query.lower() in product.get('description', '').lower():
                results.append((path, product))
        return results

def traverse(data, path=[]):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                traverse(value, path + [key])
            elif isinstance(value, str) and key == "name":
                manager.add_product(path, data)  # Add the entire product
    elif isinstance(data, list):
        for item in data:
            traverse(item, path)

if __name__ == "__main__":
    # Read JSON data from file
    with open("products.json") as f:
        products_json = json.load(f)

    manager = ProductManager()
    traverse(products_json["subcategories"])

    # Searching for root category
    search_results = manager.search_products("Electronics")
    print("Search Results:")
    for path, result in search_results:
        print("Product:", result)

    # Searching for sub category
    search_results = manager.search_products("Laptops")
    print("Search Results:")
    for path, result in search_results:
        print("Product:", result)

    # Searching for particular product using name and description
    search_results = manager.search_products("Exynos")
    print("Search Results:")
    for path, result in search_results:
        print("Category:", path)
        print("Product:", result)
