# Discount Calculator

This project implements a simple discount calculator in Python. It takes the original price and discount percentage as input, applies the discount if it's 20% or higher, and returns the final price.

## Description

This program calculates the final price of an item after applying a discount. It prompts the user for the original price and discount percentage.  A discount is applied only if the discount percentage is 20% or higher.  Otherwise, the original price is returned.

## Features

*   Calculates the final price after applying a discount.
*   Only applies discounts of 20% or more.
*   User-friendly input prompts.
*   Clear output of the final price or original price.

## Installation

1.  Make sure you have Python 3 installed on your system.  
2.  Clone this repository to your local machine:

    ```bash
    git clone <repository_url>  # Replace <repository_url> with the actual URL
    cd discount-calculator      # Navigate to the project directory
    ```

3. (Optional) It's good practice to create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate   # On Windows
    ```

     ```bash
     pip install virtualenv
     ```

## Usage

1.  Run the script:

    ```bash
    python discount_calculator.py
    ```

2.  The script will prompt you to enter the original price and the discount percentage.  Enter the values as requested.

3.  The script will then output the final price after applying the discount (if applicable) or the original price.

## Function Details

### `calculate_discount(price, discount_percent)`

*   **Parameters:**
    *   `price` (float or int): The original price of the item.
    *   `discount_percent` (float or int): The discount percentage (e.g., 10 for 10%).

*   **Returns:**
    *   float: The final price after applying the discount, or the original price if the discount is less than 20%.

*   **Logic:**

    1.  Checks if `discount_percent` is greater than or equal to 20.
    2.  If it is, calculates the discount amount: `discount_amount = price * (discount_percent / 100)`.
    3.  Calculates the final price: `final_price = price - discount_amount`.
    4.  Returns the `final_price`.
    5.  If the discount percentage is less than 20, returns the original `price`.

## Example
Enter the original price: 100 Enter the discount percentage: 25 Final price: 75.0

undefined
Enter the original price: 50 Enter the discount percentage: 10 Original price: 50.0


## Contributing

Contributions are welcome!  Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.