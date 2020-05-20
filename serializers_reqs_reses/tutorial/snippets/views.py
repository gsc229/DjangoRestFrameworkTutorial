from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response 
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
The root of our API is going to be a view that supports listing all the existing snippets, or creating a new snippet.
"""

class SnippetList(APIView):
  """
  List all code snippets, or create a new snippet.
  """
  def get(self, request, format=None):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    
    serializer = SnippetSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)     
    return Response(serializer.errors)



class SnippetDetail(APIView):
  """  
  Retrieve, update or delete a code snippet.
  """
  # class function to be called in all the single-instance methods
  def get_object(self, pk):
    try:    
        return Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        raise Http404

  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = SnippetSerializer(snippet)

    
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = SnippetSerializer(snippet, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
  """ 
  https://www.django-rest-framework.org/tutorial/3-class-based-views/

  Refactoring to class based 
  """