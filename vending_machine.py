class VendingMachine:

    """Represents a vending machine that tracks products, credit, and revenue."""

    def __init__(self, products):

        """
        Initialize a vending machine with a list of products.

        Parameters:
            products (list): Each product is a list or tuple [name, quantity, price].

        Instance Variables:
            self.products (list): The products in the machine.
            self.credit (float): Current credit inserted by the user.
            self.revenue (float): Total revenue earned by the machine.
        """

        self.__products = products # Initialize the vending machine with a list of products
        self.__credit = 0.0 # Current credit inserted by the user
        self.__revenue = 0.0 # Total revenue earned by the machine

    def insert_money(self, amount):
        """
        Insert money into the vending machine.

        Parameters:
            amount (float): The amount of money inserted.

        Outputs:
            Updates self.credit if the amount is valid.

        Returns:
            True if the money is accepted; otherwise, a string indicating invalid amount.
        """

        # Try to insert money into the vending machine
        try:
            # Only accept certain amount
            if amount in [0.05, 0.10, 0.25, 1.00, 2.00, 5.00, 10.00, 20.00]:
                self.__credit += amount
                return True # Successful insertion
            else:
                # Reject invalid amount
                return f"\nInvalid amount."
        except TypeError:
            # Handle non-numeric input
            return f"\nInvalid amount."

    def vend(self, product_num):

        """
        Dispense a product if enough credit is available.

        Parameters:
            product_num (int or str): The number of the product to vend.

        Outputs:
            Reduces product quantity and updates revenue and credit if the purchase is successful.

        Returns:
            A string indicating success, insufficient credit, or invalid product number.
        """

        # Try to vend a product by number
        try:
            # Ensure product_num is an integer
            product_num = int(product_num)
            index = product_num -1 # Convert to zero-based index

            # Check if product number is valid
            if index < 0 or index >= len(self.__products):
                return "\nProduct number does not exist."

            # Check if product is in stock and user has enough credit
            if self.__products[index][1] > 0 and self.__credit >= self.__products[index][2]:

                self.__products[index][1] -= 1 # Deduct one item from stock
                self.__revenue += self.__products[index][2] # Add price to revenue
                self.__credit -= self.__products[index][2] # Deduct price from user's credit
                return f"\nYou got {self.__products[index][0]}!"

            # If not enough credit or product unavailable
            return "\nNot enough credits."

        except TypeError:

            # Handle invalid product_num input
            return "\nProduct number does not exist"

    def return_credit(self):

        """
        Return all remaining credit to the user.

        Outputs:
            Resets self.credit to zero.

        Returns:
            A formatted string showing the amount refunded.
        """

        # Return all remaining credit to the user
        refunded = self.__credit # Store current credit
        self.__credit = 0 # Reset credit to zero
        return f"\nYou got ${refunded:.2f}."

    def __str__(self):

        """
        Return a string representing the current state of the vending machine.

        Outputs:
            Lists products with their quantity and price, along with current credit and total revenue.

        Returns:
            A formatted multi-line string showing products, credit, and revenue.
        """

        output = []

        # List all products with their quantity and price
        for i in range(len(self.__products)):
            output.append(f"{i+1}. {self.__products[i][0]} ({self.__products[i][1]}), ${self.__products[i][2]:.2f}")

        output.append(f"Credit: ${self.__credit:.2f}") # Append current credit
        output.append(f"Revenue: ${self.__revenue:.2f}\n") # Append total revenue
        return "\n".join(output) # Join all lines into a single string and return

    def get_credit(self):
        """ Return current credit"""
        return self.__credit

    def get_revenue(self):
        """ Return current revenue"""
        return self.__revenue

    def get_products(self):
        """ Return copy of current products list"""
        products_copy = []

        # Append to new list
        for i in range(len(self.__products)):
            products_copy.append(self.__products[i])
        return products_copy

