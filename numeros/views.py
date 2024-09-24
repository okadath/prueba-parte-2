from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import json
from .number import NumberSet

number_set = NumberSet()

@swagger_auto_schema(
    method='post',
    operation_description="Extrae un número del conjunto de 100 números naturales",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'number': openapi.Schema(type=openapi.TYPE_INTEGER, description='Número a extraer'),
        }
    ),
    responses={
        200: openapi.Response('Número extraído con éxito'),
        400: openapi.Response('Número inválido o ya extraído'),
        500: openapi.Response('Error inesperado')
    }
)
@api_view(['POST'])
def extract_number(request):
    try:
        number = int(request.data.get('number'))

        number_set.extract(number)

        return Response({
            'message': f"El número {number} ha sido extraído exitosamente.",
            'missing_number': number_set.find_missing_number()
        }, status=200)

    except ValueError as ve:
        return Response({'error': str(ve)}, status=400)
    except Exception as e:
        return Response({'error': 'Error inesperado: ' + str(e)}, status=500)


@swagger_auto_schema(
    method='get',
    operation_description="Muestra todos los números restantes en el conjunto de 100 números",
    responses={
        200: openapi.Response('Lista de números restantes'),
        405: openapi.Response('Método no permitido')
    }
)
@api_view(['GET'])
def show_all_numbers(request):
    return Response({
        'numbers': list(number_set.numbers)
    }, status=200)
