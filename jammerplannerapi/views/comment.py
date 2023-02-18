from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from jammerplannerapi.models import Comment, User, Rehearsal

class CommentView(ViewSet):
    """Comment view"""

    def retrieve(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        comments = Comment.objects.all()
        rehearse = self.request.query_params.get("rehearse", None)
        if rehearse is not None:
            comments = comments.filter(rehearse=rehearse)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        author = User.objects.get(id=request.data["author"])
        rehearse = Rehearsal.objects.get(pk=request.data["rehearse"])

        comment = Comment.objects.create(
          rehearse=rehearse,
          author=author,
          content=request.data["content"],
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'rehearse')
        depth = 1
