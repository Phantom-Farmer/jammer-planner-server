from jammerplannerapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated user
    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    try:
        user = User.objects.get(uid=uid)

    # If authentication was successful, respond with their token
        data = {
            'id': user.id,
            'name': user.name,
            'uid': user.uid,
            'email': user.email,
            'image_url': user.image_url,
        }
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the aethernetapi user table
    user = User.objects.create(
        name=request.data['name'],
        uid=request.data['uid'],
        image_url=request.data['image_url'],
        email=request.data['email'],
    )

    # Return the user info to the client
    data = {
            'id': user.id,
            'name': user.name,
            'uid': user.uid,
            'image_url': user.image_url,
            'email': user.email,
    }
    return Response(data)
