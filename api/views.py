from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404 

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings


from .models import *
from .serializers import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_session(request):

    return Response(status=200)

DELEGATIONS_TYPES = [
    'Officie',
    'Membre du gouvernement',
    'Chef de délagation',
    'Chef de mission', 
    'Administrateif', 
    'Entraîneur',
    'Technique', 
    'Médical', 
    'Compétiteur',
]

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    conected_user = User.objects.get(username = user)
    # print(conected_user)
    # print(conected_user)
    serializer = UserProfileSerializer(conected_user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'infos': serializer.data
    }


@api_view(['POST'])
def login_view(request):
    # print(request.data)
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid()
        
        # key = "00112233445566778899AABBCCDDEEFF"
        # plaintext = decrypt_text(ciphertext, key)


        username =serializer.data.get('username')
        password =  serializer.data.get('password') 
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success',}, status= 200)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status= 400)



@api_view(['POST', 'GET'])
def users(request):
    if request.method == 'POST':

        serialiser = UserManageSerialiser(data = request.data)
        if serialiser.is_valid():
            user = serialiser.save()
            result = send_reset_password_get_token(user)
            return Response(result)
        else:
            return Response(serialiser.errors, status=400)
    elif request.method == 'GET':

        user = User.objects.exclude(id = request.user.id)
        serialiser = UserProfileSerializer(user, many = True)
        return Response(serialiser.data)

@api_view(['POST'])
def reset_password_get_token(request):
    if request.method == 'POST':
        email = request.data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Aucun utilisateur avec cette adrese mail'}, status=400)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        # reset_password_link = request.build_absolute_uri(f"/reset-password-confirm/{uid}/{token}/")
        reset_password_link = f"{settings.FRONTEND_URL} reset-password-confirm/{uid}/{token}/"
        print(token)
        # image_url = request.build_absolute_uri(static('img/Ovrat.PNG'))

        message = render_to_string('reset_password_email.html', {'reset_password_link': reset_password_link,})
        plain_message = strip_tags(message)
        # send_mail(subjet, message, settings.EMAIL_HOST_USER, [user.email])
        # send_mail('Reset password', message, settings.EMAIL_HOST_USER, [email], fail_silently=True,  content_subtype='html')
        # emails = EmailMessage('Bienvenue sur notre site', message,  settings.EMAIL_HOST_USER,  [email,]   )

        send_mail(
            subject="Reset Password",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=message,
            # content_subtype='html'
        )

        # emails.content_subtype = 'html'
        # emails.send(fail_silently = False)
	    # emails.send(fail_silently = False)
	    # # Envoyer l'e-mail
        return Response({'status': 'email envoyé'}, status=200)

    return Response({'error': 'Methode non valide'}, status=400)




def send_reset_password_get_token(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    # reset_password_link = request.build_absolute_uri(f"/reset-password-confirm/{uid}/{token}/")
    reset_password_link = f"{settings.FRONTEND_URL}reset-password-confirm/{uid}/{token}/"
    print(token)
    # image_url = request.build_absolute_uri(static('img/Ovrat.PNG'))

    message = render_to_string('reset_password_email.html', {'reset_password_link': reset_password_link,})
    plain_message = strip_tags(message)
    send_mail(
        subject="Reset Password",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email  ],
        html_message=message,
        # content_subtype='html'
    )
    return {'status': 'email envoyé'}



# @csrf_exempt
@api_view(['POST'])
def reset_password_confirm(request, uidb64, token):
    if request.method == 'POST':
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is None or not default_token_generator.check_token(user, token):
            print('')
            return Response({'error': 'Token invalide'}, status=400)

        print(request.data)
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        if password != confirm_password:
            return Response({'error': 'Les deux mots de passent de correspondent pas'}, status=400)

        user.set_password(password)
        user.save()

        return Response({'status': 'Mot de passe changé avec success'}, status= 200)

    return Response({'error': 'Invalid request method.'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_delegation_participant(request, type):

    if request.method == 'GET':
        participant = Participant.objects.filter(function = DELEGATIONS_TYPES[int(type)], parent = request.user)
        serializer = ParticipantSerializer(participant, many = True)
        return Response(serializer.data,status = 200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_participant(request):
    if request.method == 'GET':
        participant = Participant.objects.all()
        serializer = ParticipantSerializer(participant, many = True)
        return Response(serializer.data,status = 200)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_participant_details(request, id):
    if request.method == 'GET':
        participant = get_object_or_404(Participant, pk = id)
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data,status = 200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_delegation_participant(request):
    if request.method == 'POST':
        # participant = Participant.objects.filter(function = DELEGATIONS_TYPES[int(type)], parent = request.user)
        serializer = ParticipantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(parent = request.user)
            return Response(serializer.data,status = 200)
        else:    
            return Response(serializer.errors,status = 400)
    