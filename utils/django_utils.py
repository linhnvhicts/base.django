from backend.models import User
from datetime import datetime, timedelta
from django.utils.timezone import utc
from rest_framework.authtoken.models import Token

def check_reset_password_token(token):
    user = None
    try:
        user_token = Token.objects.get(key=token)
    except Exception:
        status = 'invalid'
        return {
            'status': status,
            'user': user
        }

    current_time = datetime.utcnow().replace(tzinfo=utc)
    if user_token.created < current_time - timedelta(minutes=15):
        user_token.delete()
        status = 'expired'
    else:
        user = user_token.user
        status = 'valid'
    
    return {
        'status': status,
        'user': user
    }