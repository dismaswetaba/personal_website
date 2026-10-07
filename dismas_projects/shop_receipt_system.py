def login():
    saved_username = "DISMAS"
    saved_password = "KJV46T"
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username == saved_username and password == saved_password:
            print("Login successfull.")
            return True
        else:
            print("Error: username or password is incorrect")
def get_positive_float(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("Invalid input: please enter a number greater than zero.")
        except ValueError:
            print("Invalid input: The input should be a number greater than zero.")
def get_phone_number():
    while True:
        phone_number = input("Enter customer phone number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            print("Invalid phone number: Phone number should be digits only and exactly 10 digits.")
#Funtion to collect customer details
def collect_item_details():
    cart = []
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break
        price = get_positive_float(f"Enter the price for {item_name}: ")
        quantity = get_positive_float(f"Enter quantity for {item_name}: ")
        cost = price * quantity
        cart.append({"item": item_name, "price": price, "quantity": quantity, "cost": cost})
    return cart
def print_receipt(customer_name, phone_number, cart):
    total_cost = sum(item['cost'] for item in cart)
    print(f"The total cost is: Ksh. {total_cost}")
    money_paid = get_positive_float("Eter money paid by the customer: ")
    balance = money_paid - total_cost
    print("_" * 50)
    print("    CUSTOMER RECEIPT   ")
    print("_" * 50)
    print(f"Customer Name: {customer_name} \nPhone Number: {phone_number}\n")
    print("_" * 50)
    print(f"{'No.':<4} {'Item Name':<15} {'Price':<8} {'QTY':<6} {'Cost':<10}")
    print("_" * 50)
    for index, item in enumerate(cart, start = 1):
        print(f"{index:<4} {item['item']:<15} {item['price']:<8.2f} {item['quantity']:<6.1f} {item['cost']:<10.2f}")
    print("\n" + "_" * 50)
    print(f"{'Total Cost':<40} : Ksh.{total_cost:.2f} \n{'Money Paid':<40} : ksh.{money_paid:.2f} \n{'Balance':<40} : Ksh.{balance:.2f}")
    if balance < 0:
        print(f"\n?????????  Customer Underpaid by Ksh.{-balance:.2f} ?????")
    else:
        print("\nPayment successful. Thank you.")
    return total_cost, money_paid, balance
                    
#Function to save receipt to a file 
def save_receipt_to_file(customer_name, phone_number, cart, total_cost, money_paid, balance):
    with open("shop_receipt.txt", "w") as f:
        f.write("_" * 50)
        f.write("CUSTOMER RECEIPT")
        f.write("_" * 50)
        f.write(f"Customer Name: {customer_name}")
        f.write(f"Phone Number: {phone_number}")
        f.write("_" * 50)
        f.write(f"{'No':<4} {'Item Name':<15} {'Price':<8} {'Qty':<6} {'Cost':<10}")
        f.write("_" * 50)
        for index, item in enumerate(cart, start = 1):
            f.write(f"{index:<4} {item['item']:<15} {item['price']:<8.2f} {item['quantity']:<6.1f} {item['cost']:<10.2f}")
        f.write("_" * 50)
        f.write(f"Total Cost: Ksh.{total_cost:.2f} ")
        f.write(f"Money paid: Ksh.{money_paid:.2f}")
        f.write(f"Balance: Ksh.{balance:.2f}")
#Main function to control program flow
def main():
    print("_" * 50)
    print("SHOP RECEIPT PROGRAM")
    print("_" * 50)
    login()
    print("\n" + "_" * 50)
    print("         CUSTOMER DETAILS      ")
    print("_" * 50 + "\n")
    customer_name = input("Enter customer name: ").strip()
    phone_number = get_phone_number()
    print("\n" + "_" * 50)
    print("         COLLECTING ITEM DETAILS")
    print("_" * 50)
    cart = collect_item_details()
    if not cart:
        print("No items purchased")
        return
    total_cost, money_paid, balance = print_receipt(customer_name, phone_number, cart)
    save_receipt_to_file(customer_name, phone_number, cart, total_cost, money_paid, balance)
    print("Receipt saved successfully.")
    print("Thank you for shopping with us. God bless you.")

#Program entry point
if __name__ == "__main__":
    main()