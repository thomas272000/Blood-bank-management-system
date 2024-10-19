from django.shortcuts import render
from .models import DonorModel,BloodInventoryModel,BloodRequestModel
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status
from .serializer import DonorSerializer,BloodInventorySerializer,BloodRequestSerializer,UserRegistrationSerializer
from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = serializer.get_token(user)  
            return Response({
                'user': serializer.data,
                'token': token,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


       
class DonorAdminAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]


    def get(self, request, id=None):
        if id:
            try:
                donor = DonorModel.objects.get(id=id)
                serializer = DonorSerializer(donor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except DonorModel.DoesNotExist:
                return Response({"detail": "Donor not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            donors = DonorModel.objects.all()
            serializer = DonorSerializer(donors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # Add a new donor (POST)
    def post(self, request):
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a donor by ID (PUT)
    def put(self, request, id):
        try:
            donor = DonorModel.objects.get(id=id)
        except DonorModel.DoesNotExist:
            return Response({"detail": "Donor not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DonorSerializer(instance=donor, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Donor updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a donor by ID (DELETE)
    def delete(self, request, id):
        try:
            donor = DonorModel.objects.get(id=id)
            donor.delete()
            return Response({"detail": "Donor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except DonorModel.DoesNotExist:
            return Response({"detail": "Donor not found"}, status=status.HTTP_404_NOT_FOUND)
        
#ForBloodInventory

class BloodInventoryAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        blood_inventory = BloodInventoryModel.objects.all()
        serializer = BloodInventorySerializer(blood_inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BloodInventoryAdminAPIView(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]
    def post(self, request):
        serializer = BloodInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        try:
            blood_inventory_obj = BloodInventoryModel.objects.get(id=id)
        except BloodInventoryModel.DoesNotExist:
            return Response('Blood inventory not found', status=status.HTTP_404_NOT_FOUND)
        serializer = BloodInventorySerializer(instance=blood_inventory_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            blood_inventory_obj = BloodInventoryModel.objects.get(id=id)
            blood_inventory_obj.delete()
            return Response('Blood inventory deleted successfully', status=status.HTTP_204_NO_CONTENT)
        except BloodInventoryModel.DoesNotExist:
            return Response('Blood inventory not found', status=status.HTTP_404_NOT_FOUND)
        




class BloodRequestAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
       
        serializer = BloodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id=None):
        try:
            blood_request_obj = BloodRequestModel.objects.get(id=id)
            blood_request_obj.delete() 
            return Response('Blood request deleted successfully', status=status.HTTP_204_NO_CONTENT)
        except BloodRequestModel.DoesNotExist:
            return Response('Blood request not found', status=status.HTTP_404_NOT_FOUND)


    
class BloodRequestAdminAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, id):
        try:
            blood_request = BloodRequestModel.objects.get(id=id)
        except BloodRequestModel.DoesNotExist:
            return Response({"detail": "Blood request not found"}, status=status.HTTP_404_NOT_FOUND)

        if blood_request.status != 'Pending':
            return Response({"detail": "Request has already been processed"}, status=status.HTTP_400_BAD_REQUEST)


        if 'status' in request.data and request.data['status'] == 'Approved':

            try:
                blood_inventory = BloodInventoryModel.objects.get(blood_type=blood_request.blood_type)
            except BloodInventoryModel.DoesNotExist:
                return Response({"detail": "Blood group not found in inventory"}, status=status.HTTP_404_NOT_FOUND)


            if blood_inventory.units_available >= blood_request.units_requested :
              
                blood_inventory.units_available -= blood_request.units_requested 
                blood_inventory.save()

                blood_request.status = 'Approved'
                blood_request.save()

                return Response({"detail": "Request approved and inventory updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Not enough blood units available"}, status=status.HTTP_400_BAD_REQUEST)

        elif 'status' in request.data and request.data['status'] == 'Rejected':
            blood_request.status = 'Rejected'
            blood_request.save()
            return Response({"detail": "Request rejected"}, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)





