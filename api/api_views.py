from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.models import Salary
from api.serializers import SalarySerializer


class SalaryAPIView(GenericAPIView):

    queryset = Salary.objects.all()

    serializer_class = SalarySerializer

    #1 - 3
    def get(self, request, pk=None, *args, **kwargs):

        name = self.request.query_params.get("name","")

        filters = {"name__icontains":name}

        if pk:
            filters.update({"pk":pk})

        queryset = self.paginate_queryset(queryset=self.queryset.filter(**filters))
        serializer = SalarySerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    #2
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    #3
    def put(self, request, pk=None, *args):

        salary = self.get_object()
        serializer = self.serializer_class(data=request.data, instance=salary)

        if serializer.is_valid():
            serializer.save()
            return Response({"salary":serializer.validated_data.get("salary","")}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
