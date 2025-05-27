# Caption Generator Django Project

This project is a web application built with Django that allows users to upload images and generates captions using a CNN-LSTM based image caption generator model.

## Features

- User authentication with Django Allauth
- Image upload and caption generation
- Display user-specific caption history grouped by date
- Secure handling of user credentials and OAuth client secrets

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
Setup environment variables for OAuth credentials:
```
4. Create a .env file in the root directory (do not commit this file):

```env
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```
5. Run migrations:

```bash
python manage.py migrate
```
6. Create a superuser:

```bash
python manage.py createsuperuser
```
7. Run the development server:

```bash
python manage.py runserver
Visit http://127.0.0.1:8000/ to use the app.
```

## Model Reference
The image captioning model and logic used in this project is based on a CNN-LSTM architecture. For a detailed explanation and notebook, see my Kaggle notebook here:

Image Caption Generator using CNN and LSTM

## Notes
- Make sure to configure the django.contrib.sites framework and set up your Site object properly to avoid Site matching query does not exist errors.
- Store sensitive keys in environment variables or .env files to keep them secure.
- User authentication is handled by django-allauth.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, contact chaudharyankita@gmail.com
