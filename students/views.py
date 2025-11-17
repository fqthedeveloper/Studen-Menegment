from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import StudSelection
from .serializers import StudSelectionSerializer

class StudSelectionViewSet(viewsets.ModelViewSet):
    queryset = StudSelection.objects.all()
    serializer_class = StudSelectionSerializer

    def list(self, request):
        try:
            students = StudSelection.objects.all()
            serializer = self.get_serializer(students, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': f'Database error: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': f'Create error: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, request, pk=None):
        try:
            student = self.get_object()
            serializer = self.get_serializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': f'Update error: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, pk=None):
        try:
            student = self.get_object()
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': f'Delete error: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )