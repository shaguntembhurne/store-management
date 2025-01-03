
# **Offline Grocery Management System**

## Overview

This project is an **Offline Grocery Management System** designed to manage and track inventory, sales, and customers for a local grocery store. Initially, the system focuses on keeping track of groceries, quantities, prices, and customer details. The goal is to build a simple yet efficient application that allows store owners to handle day-to-day operations effectively.

In the future, the project will be extended into a full-fledged **E-commerce Website** that allows customers to view products, make online orders, and perform payments, integrating features such as user accounts, cart functionality, and order management.

## Features

### Current Features:
- **Inventory Management**: Keep track of products, their quantities, and prices.
- **Sales Management**: Record customer purchases, track total sales, and generate sales reports.
- **Customer Information**: Store customer details like name, contact, and address.
- **Product Search**: Easily search products by name or category.
  
### Future Enhancements (Planned):
- **User Registration & Login**: Allow customers to create accounts, log in, and manage their profiles.
- **Shopping Cart**: Add products to the cart, view cart contents, and proceed to checkout.
- **Payment Gateway**: Integration of online payment methods (credit card, PayPal, etc.).
- **Order History**: Track previous orders, manage order statuses (shipped, pending, delivered).
- **Admin Dashboard**: Advanced features for store owners to manage inventory, customer information, and sales.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Django (for future e-commerce integration)
- **Database**: MySQL (or any SQL-based system)
- **Version Control**: Git (for managing project versions)

## Installation

### Prerequisites:
- **Python 3.x**
- **MySQL** or **SQLite** (for local development)
- **Django** (for future backend integration)

### Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/grocery-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd grocery-management-system
   ```
3. Install the required Python libraries (using `pip` or `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database (MySQL or SQLite).
   - For MySQL: Create a database and configure the `settings.py` file for connection.
   - For SQLite: No setup needed; it’s default in Django.
5. Run migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser (admin) to manage the system:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Open your browser and visit `http://127.0.0.1:8000` to access the system.

## Usage

- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage inventory, customers, and sales.
- **Customer Interaction**: The system is designed to help store owners input and track sales manually. In the future, the e-commerce functionality will enable customers to place orders online.

## Contribution

Feel free to fork the repository and submit pull requests. We welcome contributions for:
- Bug fixes
- Feature enhancements
- Improving the UI/UX
- Adding more functionality

### How to Contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Added feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a pull request
