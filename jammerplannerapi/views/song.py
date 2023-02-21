from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Song, User, Band

class SongView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single dream journal
        Returns:
            Response -- JSON serialized dream journal
        """
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)


    def list(self, request):
        songs = Song.objects.all()
        band_id = request.query_params.get('band', None )
        author_id = request.query_params.get('author', None )
        if band_id is not None:
            band = Band.objects.get(pk=band_id)
            print('author_code_block')
            band_songs = songs.filter(band=band)
            serializer = SongSerializer(band_songs, many=True)
            return Response(serializer.data)
        if author_id is not None:
            author = User.objects.get(pk=author_id)
            print('author_code_block')
            auth_songs = songs.filter(author=author)
            serializer = SongSerializer(auth_songs, many=True)
            return Response(serializer.data)
        else:
            serializer = SongSerializer(songs, many = True)
            return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized dream journal
        """
        author = User.objects.get(pk=request.data['author'])
        band= Band.objects.get(pk=request.data['band'])

        song = Song.objects.create(
            title=request.data["title"],
            key=request.data["key"],
            signature=request.data["signature"],
            vibe=request.data["vibe"],
            lyric=request.data["lyric"],
            author=author,
            band=band

        )
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a dream journal
        Returns:
            Response -- Empty body with 204 status code
        """

        song = Song.objects.get(pk=pk)

        author = User.objects.get(pk=request.data["author"])
        band = Band.objects.get(pk=request.data["band"])

        song.title=request.data["title"]
        song.key=request.data["key"]
        song.signature=request.data["signature"]
        song.vibe=request.data["vibe"]
        song.lyric=request.data["lyric"]
        song.author=author
        song.band=band
        song.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'key', 'signature', 'vibe', 'lyric', 'author', 'band')
        depth = 2
