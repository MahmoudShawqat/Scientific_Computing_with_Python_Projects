# Define a class called Category to represent a budget category
class Category:
    # Constructor initializes a Category with a given category name
    def __init__(self, category):
        self.category = category  # Set the category name
        self.ledger = []  # Initialize an empty list to store transactions

    # Deposit method adds an amount and optional description to the ledger
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Withdraw method subtracts an amount from the ledger if funds are sufficient
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Get_balance method calculates and returns the current balance
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    # Transfer method transfers funds from one category to another
    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    # Check_funds method checks if there are enough funds for a given amount
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # Override the string representation of the object for printing
    def __str__(self):
        title = f"{self.category:*^30}\n"  # Create a title line with centered category name
        items = ""  # Initialize an empty string to store transaction details
        total = 0  # Initialize a variable to track the total balance
        # Loop through ledger items and format them for display
        for item in self.ledger:
            description = item['description'][:23]
            amount = "{:.2f}".format(item['amount'])
            items += f"{description}{' '*(23-len(description))}{amount}\n"
            total += item['amount']
        # Combine title, items, and total to create the final output
        output = title + items + f"Total: {total:.2f}"
        return output


# Function to create a bar chart representing the percentage spent by each category
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    # Calculate spent percentages for each category
    spent_percentages = [(sum(item['amount'] for item in category.ledger if item['amount'] < 0) / category.get_balance()) * 100 for category in categories]

    # Loop through percentage values to create each line of the chart
    for i in range(100, -1, -10):
        chart += f"{i:3}|"  # Add the percentage label to the left
        # Loop through categories and add 'o' or space based on the percentage
        for percentage in spent_percentages:
            chart += ' o ' if percentage >= i else '   '
        chart += ' \n'

    chart += "    ----------\n     "  # Add the horizontal line below the bars
    # Loop through category names and add them vertically below the bars
    max_category_length = max(len(category.category) for category in categories)
    for i in range(max_category_length):
        for category in categories:
            chart += f" {category.category[i] if i < len(category.category) else ' '}  "
        chart += ' \n'

    return chart
