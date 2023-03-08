from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Set, User, Band

class SetView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single dream journal
        Returns:
            Response -- JSON serialized dream journal
        """
        setlist = Set.objects.get(pk=pk)
        serializer = SetSerializer(setlist)
        return Response(serializer.data)



    def list(self, request):
        setlists = Set.objects.all()
        band_id = request.query_params.get('band', None )
        author_id = request.query_params.get('author', None )
        if band_id is not None:
            band = Band.objects.get(pk=band_id)
            print('band_code_block')
            band_sets = setlists.filter(band=band)
            serializer = SetSerializer(band_sets, many=True)
            return Response(serializer.data)
        if author_id is not None:
            author = User.objects.get(pk=author_id)
            print('author_code_block')
            auth_sets = setlists.filter(author=author)
            serializer = SetSerializer(auth_sets, many=True)
            return Response(serializer.data)
        else:
            serializer = SetSerializer(setlists, many = True)
            return Response(serializer.data)
        # sets = Set.objects.all()
        # band_id = request.query_params.get('band', None )
        # if band_id is not None:
        #     band_set = sets.filter(band_id=band_id)
        # serializer = SetSerializer(band_set, many=True)
        # return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized dream journal
        """
        author = User.objects.get(pk=request.data['author'])
        band= Band.objects.get(pk=request.data['band'])

        setlist = Set.objects.create(
            title=request.data["title"],
            note=request.data["note"],
            author=author,
            band=band

        )
        serializer = SetSerializer(setlist)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a dream journal
        Returns:
            Response -- Empty body with 204 status code
        """

        setlist = Set.objects.get(pk=pk)

        author = User.objects.get(pk=request.data["author"])
        band = Band.objects.get(pk=request.data["band"])

        setlist.title=request.data["title"]
        setlist.note=request.data["note"]
        setlist.author=author
        setlist.band=band
        setlist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        setlist = Set.objects.get(pk=pk)
        setlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SetSerializer(serializers.ModelSerializer):
    """JSON serializer for Sets
    """
    class Meta:
        model = Set
        fields = ('id', 'title', 'note', 'author', 'band')
        depth = 1
