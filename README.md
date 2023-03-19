# Dealzng
Your one stop shop for discounted prices in Hotel, Travel, Restaurant, Spa, and Training.

This is an online discount-shopping platform built with Flask, SQLAlchemy, Bulma, and Flask-mail. It allows users to view and purchase discounted items from the platform, save items to cart, and make payments.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation
To install and run this project, please follow the steps below:

1. Clone the project repository to your local machine by running the following command in your terminal:
``` bash
    git clone https://github.com/foreign1/dealzng.git
```
2. Navigate to the project directory using the command:
``` bash
    cd <project-name>
```
3. Create a virtual environment for the project using the command:
```
    python -m venv venv
```
4. Activate the virtual environment by running the command below:
For Windows:
``` bash 
    venv\Scripts\activate
```
For Unix or Linux:
``` bash
    source venv/bin/activate
```
5. Install the project dependencies using the command:
``` bash
    pip install -r requirements.txt
```
6. Set up the environment variables by creating a .env file in the root directory of the project and populating it with the required environment variables. You can copy the contents of .env.example file and update the values as necessary.
``` bash
    cp .env.example .env
```
7. Start the application by running the command:
``` bash
    flask run
```
8. Open your browser and enter http://localhost:5000 in the address bar to access the application.
Note: This project assumes that you have Python and pip installed on your machine. If not, please install them before proceeding.

## Usage
As a shopper, you can use this application to:

- View discounted products: On the homepage, you can see all available products listed with their name, description, actual price, and discount price.
- Add products to cart: Click on the "Add to Cart" button to add a product to your cart. You can then view the items in your cart by clicking on the cart link at the top right corner of the page.
- Remove products from cart: In the cart page, you can remove products from your cart by clicking on the "Delete" button next to the product you want to remove.
- Make payment: In the cart page, you can make payment for the items in your cart by filling in your card details and clicking on the "Make Payment" button.

## Feature list
- [x] ``User Authentication``: allows users to register, log in and log out of the application
- [x] ``Product Listing``: displays a list of products available for purchase, including the product name, actual price, discount price, and an image
- [x] ``Product Detail``: shows the details of a selected product, including the product name, actual price, discount price, image, and description
- [x] ``Add to Cart``: allows users to add a product to their cart
- [x] ``Cart``: displays a list of products in the user's cart, including the product name, actual price, discount price, and total cost of items in the cart. Users can also delete items from their cart.
- [x] ``Checkout``: allows users to enter their payment details, including card number, cvv, expiry date, and pin, and complete the payment process. Upon successful payment, users receive a notification email containing the summary of their cart items and the total amount paid.

## Technologies Used
Flask
SQLAlchemy
Bootstrap 4
Stripe API
SQLite database
Flask Mail

## Contributing
Contributions are welcome. Feel free to open a pull request or submit an issue.

## License
Distributed under the MIT License. See LICENSE for more information.