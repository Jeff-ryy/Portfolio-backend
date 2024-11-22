from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContactForm
from .serializers import ContactFormSerializer

@api_view(['POST'])
def submit_form(request):
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_submissions(request):
    submissions = ContactForm.objects.all()
    serializer = ContactFormSerializer(submissions, many=True)
    return Response(serializer.data)
