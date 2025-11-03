# README.md

# Project Documentation

## Email Configuration Settings

To successfully send emails from the application, please ensure that the following configurations are set in your environment. These settings will be used for the email service integration.

### Required Email Configuration Parameters

1. **EMAIL_HOST**: The SMTP server to use for sending emails (e.g., `smtp.gmail.com`).
2. **EMAIL_PORT**: The port to use for the email service (e.g., `587` for TLS or `465` for SSL).
3. **EMAIL_USE_TLS**: A boolean that indicates whether to use TLS (Transport Layer Security). Set to `True` if you want to leverage TLS, otherwise `False`.
4. **EMAIL_USE_SSL**: A boolean that indicates whether to use SSL (Secure Sockets Layer). Set to `True` if you prefer SSL, otherwise `False`.
5. **EMAIL_HOST_USER**: The username for authenticating with the email service (typically your email address).
6. **EMAIL_HOST_PASSWORD**: The password for the email account (ensure this is kept secret).
7. **DEFAULT_FROM_EMAIL**: The default "from" address for outgoing emails (e.g., `no-reply@example.com`).

### Example `.env` Configuration

You can use a `.env` file to provide these configurations. An example configuration would look as follows:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
DEFAULT_FROM_EMAIL=no-reply@example.com
```

**Important Note**: Ensure that the email service you choose allows SMTP access, and check your account settings for any additional configuration requirements, such as enabling "less secure app access" (if applicable) or using application-specific passwords.

### Testing Email Functionality

When testing the email functionality, make sure to use valid email addresses and verify that your application can connect to the email service with the provided credentials. If you encounter issues, check the configurations against the documentation of your email provider for possible misconfigurations.