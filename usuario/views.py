
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Q 
from django.core.mail import send_mail
import secrets
from datetime import datetime

User = get_user_model()

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if Usuario.objects.filter(username=username).exists():
        return Response({'message': 'Usuário já existente!'}, status=status.HTTP_400_BAD_REQUEST)
    elif Usuario.objects.filter(email=email).exists():
        return Response({'message': 'Email já está sendo utilizado!'}, status=status.HTTP_400_BAD_REQUEST)
    if username and email and password:
        user = User.objects.create(username=username)
        user.email = email
        user.set_password(password)
        user.save()

        response_data = {
            'message': 'Usuário criado com sucesso.',
            'username': user.username,
            'email': user.email,
            'id': user.id,
            # Adicione outros campos do usuário que você deseja retornar
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Dados de usuário inválidos.'}, status=400)
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    value = request.data.get('value')
    password = request.data.get('password')

    if value is not None and password is not None:
        
        try:
            user = User.objects.get(Q(username=value) | Q(email=value))
            username = user.username
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
                user = None
    else:
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        response_data = {
            'refresh': str(refresh),
            'access': str(access),
            'username': user.username,
            'email': user.email,
            'id': user.id,
            # Adicione outros campos do usuário que você deseja retornar
        }
        return Response(response_data , status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Falha na autenticação'}, status=status.HTTP_401_UNAUTHORIZED)
        

import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    remetente = 'trottingtomes@gmail.com'
    senha = 'xektjmzuaveczuhh'

    # Criando a mensagem
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario

    # Conectando ao servidor SMTP do Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)

    # Enviando o e-mail
    server.send_message(msg)
    server.quit()

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def forget_password(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Email não encontrado'}, status=status.HTTP_401_UNAUTHORIZED)
        pass
    else:
        # Gerar token exclusivo
        token = secrets.token_hex(20)
        # Salvar o token, e-mail do usuário e data/hora
        user.password_reset_token = token
        user.password_reset_token_created = datetime.now()
        user.save()
        # Enviar e-mail
        subject = 'Redefinição de senha'
        message = f'Olá, {user.username}! Para redefinir sua senha, clique neste link: http://seusite.com/redefinir-senha/{token}'
        to_email = [email]
        enviar_email(to_email, subject, message,)
        # Exibir uma mensagem de sucesso na tela
        pass