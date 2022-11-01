from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Order
from organizations.models import Organization
from .serializers import OrderSerializer, OrderUpdateSerializer

class OrderListCreateViewSet(ModelViewSet):
  serializer_class = OrderSerializer
  permission_classes = [IsAuthenticated,]

  def list(self, request, slug):
    if request.user.organization is None:
      return Response(
        {'detail': 'You are not an admin of any organization'},
        status=status.HTTP_400_BAD_REQUEST
      )
    organization = Organization.objects.get(slug=slug)
    if request.user.organization != organization:
      return Response(
        {"detail": "You do not have permission to perform this action."},
        status=status.HTTP_403_FORBIDDEN
      )
    queryset = Order.objects.filter(charity_ord_id=organization.id)
    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def create(self, request, slug, *args, **kwargs):
    if request.user.organization is None:
      return Response(
        {'detail': 'You are not an admin of any organization'},
        status=status.HTTP_400_BAD_REQUEST
      )
    organization = Organization.objects.get(slug=slug)
    if request.user.organization != organization:
      return Response(
        {"detail": "You do not have permission to perform this action."},
        status=status.HTTP_403_FORBIDDEN
      )
    
    if organization.organization_type == 'Donor':
      return Response(
        {'detail': 'Donor organizations cannot create orders'},
        status=status.HTTP_400_BAD_REQUEST
      )

    request.data._mutable = True
    
    request.data['charity_org_name'] = organization.name
    request.data['charity_org_id'] = str(organization.id)

    request.data._mutable = False
    
    return super().create(request, *args, **kwargs)