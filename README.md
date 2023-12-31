# Business Total Web Application

Welcome to the Business Total Web Application repository! This web application allows you to manage your business products and details.

## Features

- View and manage products associated with your business.
- Create, edit, and delete products.
- Organize your products by categories.
- Keep track of important business information.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django (install using `pip install Django`)

### Installation

Clone the repository:

```shell
git clone https://github.com/MayersScott/Business-Total.git
```

Navigate to the project directory:
  `cd business-total`
  
Create a virtual environment:
  `python -m venv .venv`

Activate the virtual environment:
  On Windows:
    `.venv\Scripts\activate`
  On macOS and Linux:
    `source .venv/bin/activate`

Make migrations:
  ```python
    python manage.py makemigrations

    python manage.py migrate
  ```

Run the development server:
  `python manage.py runserver`
  
Open your browser and access the application at http://localhost:8000/

![photo](https://github.com/MayersScott/Business-Total/assets/148715834/7671ab5a-e012-428a-934a-013f7557a6ef)

## Usage
Create a business profile and add your products.
Edit and delete products as needed.
Categorize your products for better organization.
Keep track of your business information.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
