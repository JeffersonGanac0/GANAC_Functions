def display_menu():
    menu_items = {
        1: ("Burger", 5.00),
        2: ("Pizza", 8.00),
        3: ("Pasta", 7.00),
        4: ("Salad", 4.50),
        5: ("Soda", 1.50)
    }
    print("\nMenu:")
    for option_num, food_details in menu_items.items():
        print(f"{option_num}. {food_details[0]} - ${food_details[1]:.2f}")
    return menu_items

def take_order(menu_items):
    while True:
        try:
            selected_option = int(input("\nEnter the number of the item you want to order: "))
            if selected_option in menu_items:
                ordered_item, ordered_price = menu_items[selected_option]
                print(f"You selected: {ordered_item} (${ordered_price:.2f})")
                return ordered_price
            else:
                print("Invalid choice. Please select an item from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(final_cost):
    while True:
        try:
            payment_amount = float(input(f"\nTotal cost is ${final_cost:.2f}. Enter cash amount: "))
            if payment_amount >= final_cost:
                balance_due = payment_amount - final_cost
                print(f"Payment successful! Your change is ${balance_due:.2f}.")
                break
            else:
                print(f"Insufficient cash. You need at least ${final_cost - payment_amount:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    print("Welcome to the Food Ordering System!")
    menu_items = display_menu()
    final_cost = take_order(menu_items)
    process_payment(final_cost)
    print("\nThank you for your order! Enjoy your meal!")

if __name__ == "__main__":
    main()

    #Jefferson O. Ganac
    
    #IT - 103

