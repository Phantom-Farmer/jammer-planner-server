from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Set_Song, Song, Set, Band
from jammerplannerapi.views import SongSerializer


class SetSongView(ViewSet):
    """song set view"""

    def retrieve(self, request, pk):
        try:
            set_song = Set_Song.objects.get(pk=pk)
            serializer = SetSongSerializer(set_song)
            return Response(serializer.data)
        except Set_Song.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        def get_songs_for_set(set_id):
            setlist = Set.objects.get(id=set_id)
            set_songs = Set_Song.objects.filter(setlist=setlist)
            return set_songs

        set_id = request.query_params.get('set', None)
        band_id = request.query_params.get('band', None )
        if set_id is not None:
            set_songs = get_songs_for_set(set_id)
            serializer = SetSongSerializer(set_songs, many=True)
            return Response(serializer.data)
        if band_id is not None:
            band = Band.objects.get(pk=band_id)
            print('author_code_block')
            band_set_songs = set_songs.filter(band=band)
            serializer = SetSongSerializer(band_set_songs, many=True)
            return Response(serializer.data)
        else:
            set_songs = Set_Song.objects.all()
            serializer = SetSongSerializer(set_songs, many=True)
            return Response(serializer.data)

    def create(self, request):
        song = Song.objects.get(id=request.data["song_id"])
        set = Set.objects.get(pk=request.data["set_id"])
        band= Band.objects.get(pk=request.data['band_id'])

        set_song = Set_Song.objects.create(
        song=song,
        set=set,
        band=band,
        order = request.data["order"],
        )
        serializer = SetSongSerializer(set_song)
        return Response(serializer.data)

    def update(self, request, pk):
        set_song = Set_Song.objects.get(pk=pk)
        set_song.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        set_song = Set_Song.objects.get(pk=pk)
        set_song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SetSongSerializer(serializers.ModelSerializer):
    set_id = serializers.ReadOnlyField(source='set.id')
    song_title = serializers.ReadOnlyField(source='song.title')
    song_id = serializers.ReadOnlyField(source='song.id')
    band_id = serializers.ReadOnlyField(source='band.id')
    class Meta:
        model = Set_Song
        fields = ('id', 'set_id', 'song_title', 'song_id', 'band_id', 'order')
