from app import app as application  # Import your Flask app

def handler(request):
    return application(request)
