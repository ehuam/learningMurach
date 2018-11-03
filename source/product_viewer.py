from objects import Product, Book, Movie

def show_products(products):
    print("Products")
    for i in range(len(products)):
        product = products[i]
        # The show_product() function calls the getDescription() method of the current product object in the loop to print
        # the data for the product. Thanks to polymorphism, this calls the correct getDescription() method depnding on the 
        # the type of of the current product
        print(str(i+1) + ". " + product.getDescription())
    print()

def show_product(product):
    print("PRODUCT DATA")
    print("Name:\t\t", product.name)

    # The display is varied based on that object type
    if isinstance(product, Book):
        # isinstance is used to determine what type of object is being displayed.
        print("Author\t\t", product.author)
    if isinstance(product, Movie):
        print("Year:\t\t", product.year)
    
    print("Discount price:\t\t {:.2f}".format(product.getDiscountPrice()))
    print()

def main():
    print("The Product Viewer program")
    print()
    # The main function creates a tuple of Product Objects. To do that, it calls the constructer of the Product Class
    # to create each object, and it stores each object in the tuple without going through the intermediate step of
    # creating a variable name that refers to the object type.

    products = (Product('Stanley 13 Ounce Wood Hammer', 12.99, 62),
                Book("The Big Short", 15.95, 34, "Michael Lewis"),
                Movie("The Holy Grail - DVD", 14.99, 68, 1975))
    
    show_products(products)

    # This create the a loop to keep asking for prompts.
    while True:
        # Prompts the user to enter a number that corresponds with a product
        number = int(input("Enter product number: "))
        print()
    
        # it gets the number assigned to int, substracts 1 to adjust for the index
        product = products[number-1]
        # product is assigned the object at the inputted index.
        #  the product is passed to show_product(). show_product uses if statements to handle different object attributes.
        show_product(product)

        # prompt to continue.
        choice = input("Continue?\t (y/n):\t")

        print()
        if choice != "y":
            break

if __name__ == "__main__":
    main()