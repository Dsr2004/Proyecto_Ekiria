from datetime import timedelta
from email import message
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from datetime import datetime

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time
    
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)
    
    def expiration_time_controller(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()
            all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
            if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id_usuario == int(session_data.get('_auth_user_id')):
                                session.delete()
    
    def authenticate_credentials(self, key):
        message,token,user = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token inválido.'
            self.expired = True
        
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo.'
                
        if token is not None:
            is_expired = self.expiration_time_controller(token)
            if is_expired:
                message = 'Su Token ha expirado.'
        return (user, token, message, self.expired)
        