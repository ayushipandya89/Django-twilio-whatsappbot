# Django Twilio WhatsApp Bot

This project is a WhatsApp bot built using Django and Twilio's API. The bot allows users to interact with the application via WhatsApp messages. It can be used for various purposes such as customer support, information retrieval, and automated responses.

## Features

- **Receive WhatsApp Messages**: The bot can receive messages sent to your Twilio WhatsApp number.
- **Automated Responses**: Configure automated responses based on the content of the received messages.
- **Django Admin**: Manage and configure the bot via the Django admin interface.
- **Twilio API Integration**: Utilizes Twilio's API for sending and receiving WhatsApp messages.


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ayushipandya89/Django-twilio-whatsappbot.git
    cd django_twilio_whatsapp_bot
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Configure Twilio**:
    - Sign up for a [Twilio account](https://www.twilio.com/).
    - Obtain your Twilio Account SID and Auth Token.
    - Set up a Twilio WhatsApp sandbox and obtain the sandbox number.
    - Add the Twilio credentials to your project's settings:
    ```python
    # settings.py
    TWILIO_ACCOUNT_SID = 'your_account_sid'
    TWILIO_AUTH_TOKEN = 'your_auth_token'
    TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio sandbox number
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Send a WhatsApp Message**:
    - Send a WhatsApp message to your Twilio sandbox number.
    - The bot will process the message and respond based on your configured logic.

2. **Configure Automated Responses**:
    - You can configure automated responses in the Django admin interface.

