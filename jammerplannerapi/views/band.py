from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Band, User

class BandView(ViewSet):

    def retrieve(self, request, pk):

        band = Band.objects.get(pk=pk)
        serializer = BandSerializer(band)
        return Response(serializer.data)

    def list(self, request):
        bands = Band.objects.all()
        author_id = request.query_params.get('author', None )
        if author_id is not None:
            author = User.objects.get(pk=author_id)
            print('author_code_block')
            auth_bands = bands.filter(author=author)
            serializer = BandSerializer(auth_bands, many=True)
            return Response(serializer.data)
        else:
            serializer = BandSerializer(bands, many = True)
            return Response(serializer.data)

    def create(self, request):

        author = User.objects.get(pk=request.data["author"])

        band = Band.objects.create(
            name = request.data["name"],
            author = author
        )
        serializer = BandSerializer(band)
        return Response(serializer.data)

    def update(self, request, pk):

        band = Band.objects.get(pk=pk)
        author = User.objects.get(pk=request.data["author"])

        band.name = request.data["name"]
        band.author = author
        band.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        band = Band.objects.get(pk=pk)
        band.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = ('id', 'name', 'author')
        depth = 1
