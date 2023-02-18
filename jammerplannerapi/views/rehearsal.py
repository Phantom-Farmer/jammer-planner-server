from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Rehearsal, User, Band, Set

class RehearsalView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single dream journal
        Returns:
            Response -- JSON serialized dream journal
        """
        rehearsal = Rehearsal.objects.get(pk=pk)
        serializer = RehearsalSerializer(rehearsal)
        return Response(serializer.data)


    def list(self, request):
        """"Handle GET requests to handle all dream journals"""
        rehearsals = Rehearsal.objects.all()
        author_id = request.query_params.get('author', None )
        band_id = request.query_params.get('band', None )
        if author_id is not None:
            author = User.objects.get(pk=author_id)
            print('author_code_block')
            auth_rehearsals = rehearsals.filter(author=author)
            serializer = RehearsalSerializer(auth_rehearsals, many=True)
        if band_id is not None:
            band_rehearsal = rehearsals.filter(band_id=band_id)
            serializer = RehearsalSerializer(band_rehearsal, many=True)
        return Response(serializer.data)
        # bands = Band.objects.all()
        # band_id = request.query_params.get('band', None )
        # if band_id is not None:
        #     band_song = songs.filter(band_id=band_id)
        # serializer = SongSerializer(band_song, many=True)
        # return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized dream journal
        """
        author = User.objects.get(pk=request.data['author'])
        band = Band.objects.get(pk=request.data['band'])
        setlist = Set.objects.get(pk=request.data['setlist'])

        rehearsal = Rehearsal.objects.create(
            date=request.data["date"],
            time=request.data["time"],
            location=request.data["location"],
            show=request.data["show"],
            message=request.data["message"],
            author=author,
            band=band,
            setlist=setlist

        )
        serializer = RehearsalSerializer(rehearsal)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a dream journal
        Returns:
            Response -- Empty body with 204 status code
        """

        rehearsal = Rehearsal.objects.get(pk=pk)

        author = User.objects.get(pk=request.data["author"])
        band = Band.objects.get(pk=request.data["band"])
        setlist = Set.objects.get(pk=request.data['setlist'])

        rehearsal.date=request.data["date"]
        rehearsal.time=request.data["time"]
        rehearsal.location=request.data["location"]
        rehearsal.show=request.data["show"]
        rehearsal.message=request.data["message"]
        rehearsal.author=author
        rehearsal.band=band
        rehearsal.setlist=setlist
        rehearsal.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        rehearsal = Rehearsal.objects.get(pk=pk)
        rehearsal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RehearsalSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """
    class Meta:
        model = Rehearsal
        fields = ('id', 'date', 'time', 'location', 'show', 'message', 'author', 'band', 'set')
        depth = 1
