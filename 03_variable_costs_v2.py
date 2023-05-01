import pandas

def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer!!!!")

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == ""
            print("{}.  \nPlease try again.\n").format(error))
            continue

        return response

def currency(x):
    return f"${x:.2f}"

# gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name must not be blank")
        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity:",
                             "Tha amount must be a whole number,",
                             int)
        price = num_check("How much for a single item? $",
                          "The price must be a number <more than zero>",
                          float)
        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

        return [expense_frame, sub_total]
# main routine

# Get product name
product_name = not_blank('Product name: ', 'The product name cannot be blank')

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Printing area

print()
print(variable_frame)
print()

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Product name: ",
                         "The product name can't be blank.")

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ",
                          "The component name can't be blank.")
    if item_name.lower() == "xxx":
        break
    quantity = num_check ("Quantity:",
                          "The amount must be a whole number greater than zero",
                          int)

    price = num_chec("How much for a single item?: $",
                     "The price must be a number greater than zero.",
                     float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

#Calculate cost of each component

variable_frame['Cost'] = variable_frame['Quality']\
                        * variable_frame['Price']

# Find sub-total
variable_sub = variable_frame['Cost'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# Printing area

print(variable_frame)

print()

print("Variable Costs: ${:.2f}").format(variable_sub)
