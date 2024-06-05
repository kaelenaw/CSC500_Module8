class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.item_total = self.item_price * self.item_quantity
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}")

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item) # Adds item name to cart items

    def remove_item(self, item_name):
        removed = False
        for item in self.cart_items[:]:  # Iterate over a copy of the list
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f'{item_name} removed from cart.')
                removed = True
                break
        if not removed:
            print('\nItem not found in cart. Nothing removed.\n')

    def modify_item(self, ItemToPurchase):
        item_found = False
        for cart_item in self.cart_items: # For every cart item in the list
            if cart_item.item_name == ItemToPurchase.item_name: # If a cart item name is also a name in ItemToPurchase
                item_found = True
                if ItemToPurchase.item_price != 0.0 and ItemToPurchase.item_price != 'p':
                    cart_item.item_price = ItemToPurchase.item_price # Modifies item price
                    cart_item.item_total = cart_item.item_price * cart_item.item_quantity # Update total of item

                    print(f"{ItemToPurchase.item_name} price modified to {ItemToPurchase.item_price}.")
                if ItemToPurchase.item_quantity != 0.0 and ItemToPurchase.item_quantity != 'q':
                    cart_item.item_quantity = ItemToPurchase.item_quantity # Modifies item quantity
                    cart_item.item_total = cart_item.item_price * cart_item.item_quantity # Update total of item

                    print(f"{ItemToPurchase.item_name} quantity modified to {ItemToPurchase.item_quantity}.")
                if ItemToPurchase.item_description != '' and ItemToPurchase.item_description != 'd':
                    cart_item.item_description = ItemToPurchase.item_description # Modifies item description

                    print(f"{ItemToPurchase.item_name} description modified to {ItemToPurchase.item_description}.")
                break
        if not item_found:
            print('Item not found in cart. Nothing modified.')
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items:', self.get_num_items_in_cart())
            for item in self.cart_items:
                print('{n} {q} @ ${p:.2f} = ${t:.2f}'.format(n = item.item_name, p = item.item_price, q = item.item_quantity, t = item.item_total))
            print(f'Total: ${self.get_cost_of_cart():.2f}')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            print('{n}: {d}'.format(n = item.item_name, d = item.item_description))

def print_menu(ShoppingCart):
    selection = ''

    while selection != 'q':
        print('\nMENU\n')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        selection = input('\nChoose an option: ')
        if selection == 'a':
            print('\nADD ITEM TO CART')
            # Get input for item information from user
            name = input('Enter the item name: \n')
            description = input('Enter the item description: \n')
            price = float(input('Enter the item price: \n'))
            quantity = int(input('Enter the item quantity: \n'))

            item = ItemToPurchase(name, price, quantity, description)  # Creates ItemToPurchase with input info
            ShoppingCart.add_item(item)

        elif selection == 'r':
            print('\nREMOVE ITEM FROM CART')
            item = input('Enter name of item to remove: \n')
            ShoppingCart.remove_item(item)

        elif selection == 'c':
            print('\nCHANGE ITEM QUANTITY')
            name = input('Enter the item name: \n')
            new_quantity = int(input('Enter the new quantity: \n'))

            item = ItemToPurchase(name, 'p', new_quantity, 'd')
            ShoppingCart.modify_item(item)

        elif selection == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_descriptions()

        elif selection == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()

        elif selection != 'q':
            print('Please enter a valid menu option')

####

# Get customer input for name and date
name = input('Enter customer\' name: ')
date = input('Enter today\'s date: ')

ShoppingCart = ShoppingCart(name, date)

print_menu(ShoppingCart)
