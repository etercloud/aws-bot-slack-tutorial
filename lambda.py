import json
import urllib3

def lambda_handler(event, context):
    # Crear un objeto PoolManager
    http = urllib3.PoolManager()
    
    # Realizar la primera petición
    response = http.request('GET', 'https://api.thecatapi.com/v1/images/search')
    
    # Verificar que la petición fue exitosa
    if response.status == 200:
        # Decodificar la respuesta JSON
        data = json.loads(response.data.decode('utf-8'))
        
        cat = data[0]['url']
    data = { "blocks": [ { "type": "image", "image_url": cat, "alt_text": "Beautiful cat" } ] }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }
