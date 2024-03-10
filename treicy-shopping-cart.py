class ItemToPurchase:
  def __init__(self, item_name="none", item_description="none", item_price=0.00, item_quantity=0):
      self.item_name = item_name
      self.item_description = item_description
      self.item_price = item_price
      self.item_quantity = item_quantity

class ShoppingCart:
  def __init__(self, customer_name="none", current_date="March 9, 2024"):
      self.customer_name = customer_name
      self.current_date = current_date
      self.cart_items = []

  def add_item(self, item):
      self.cart_items.append(item)

  def remove_item(self, item_name):
          found_item = None
          for item in self.cart_items:
              if item.item_name.lower() == item_name.lower():
                  found_item = item
                  break

          if found_item:
              self.cart_items.remove(found_item)
              print(f"Item {item_name} removed successfully.")
          else:
              print("No item with that name was in the cart, nothing got removed.")

  def modify_item(self, modified_item):
          for item in self.cart_items:
              if item.item_name.lower() == modified_item.item_name.lower():
                  if modified_item.item_description != "none":
                      item.item_description = modified_item.item_description
                  if modified_item.item_price != 0:
                      item.item_price = modified_item.item_price
                  if modified_item.item_quantity != 0:
                      item.item_quantity = modified_item.item_quantity
                  print(f"Item {item.item_name} modified successfully.")
                  return
          print("No item with that name was in the cart, nothing modified.")

  def get_num_items_in_cart(self):
      return sum(item.item_quantity for item in self.cart_items)

  def get_cost_of_cart(self):
      return sum(item.item_quantity * item.item_price for item in self.cart_items)

  def print_total(self):
      print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
      print("Number of Items:", self.get_num_items_in_cart())
      for item in self.cart_items:
          print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
      print("Total: $" + str(self.get_cost_of_cart()))

  def print_descriptions(self):
      print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
      print("Item Descriptions")
      for item in self.cart_items:
          print(f"{item.item_name}: {item.item_description}")

def print_menu():
  print("\nMENU")
  print("a - Add item to cart")
  print("r - Remove item from cart")
  print("c - Change item quantity")
  print("i - Output items' descriptions")
  print("o - Output shopping cart")
  print("q - Quit")

def main():
  customer_type = input("Is the customer a company or a natural person? (Enter 'company' or 'person'): ").lower()

  if customer_type == 'company':
      ein_id = input("Enter the EIN ID number: ")
      customer_name = input("Enter company name: ")
  elif customer_type == 'person':
      identification_type = input("Enter 'ssn' for Social Security Number or 'passport' for Passport: ").lower()
      identification_number = input(f"Enter {identification_type}: ")
      customer_name = input("Enter your name: ")
  else:
      print("Invalid customer type. Exiting program.")
      return

  current_date = input("Enter the current date: ")
  shopping_cart = ShoppingCart(customer_name, current_date)
  print(f"\nCustomer name: {customer_name}")
  print(f"Today's date: {current_date}")

  while True:
      print_menu()
      choice = input("Choose an option: ").lower()

      if choice == 'a':
          item_name = input("Enter the item name: ")
          item_description = input("Enter the item description: ")
          item_price = float(input("Enter the item price: "))
          item_quantity = int(input("Enter the item quantity: "))
          item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
          shopping_cart.add_item(item)
      elif choice == 'r':
          item_name = input("Enter the item name to remove: ")
          shopping_cart.remove_item(item_name)
      elif choice == 'c':
          modified_item = ItemToPurchase()
          modified_item.item_name = input("Enter the item name to modify: ")
          modified_item.item_description = input("Enter the new item description (press Enter to keep current): ")
          modified_item.item_price = float(input("Enter the new item price (press Enter to keep current): ") or 0)
          modified_item.item_quantity = int(input("Enter the new item quantity (press Enter to keep current): ") or 0)
          shopping_cart.modify_item(modified_item)
      elif choice == 'i':
          shopping_cart.print_descriptions()
      elif choice == 'o':
          shopping_cart.print_total()
      elif choice == 'q':
          break
      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
if __name__ == "__main__":
  customer_name = input("Enter customer's name:\n")
  current_date = input("Enter today's date:\n")

  print(f"Customer name: {customer_name}")
  print(f"Today's date: {current_date}")

  # Create an object of type ShoppingCart
  shopping_cart = ShoppingCart(customer_name, current_date)

  while True:
      print_menu()
      choice = input("Choose an option: ").lower()

      if choice == 'a':
          print("\nADD ITEM TO CART")
          item_name = input("Enter the item name:\n")
          item_description = input("Enter the item description:\n")
          item_price = float(input("Enter the item price:\n"))
          item_quantity = int(input("Enter the item quantity:\n"))
          item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
          shopping_cart.add_item(item)
      elif choice == 'r':
          print("\nREMOVE ITEM FROM CART")
          item_name = input("Enter name of item to remove:\n")
          shopping_cart.remove_item(item_name)
      elif choice == 'c':
          print("\nCHANGE ITEM QUANTITY")
          modified_item = ItemToPurchase()
          modified_item.item_name = input("Enter the item name:\n")
          modified_item.item_quantity = int(input("Enter the new quantity:\n"))
          shopping_cart.modify_item(modified_item)
      elif choice == 'i':
          shopping_cart.print_descriptions()
      elif choice == 'o':
          shopping_cart.print_total()
      elif choice == 'q':
          break
      else:
          print("Invalid choice. Please try again.")