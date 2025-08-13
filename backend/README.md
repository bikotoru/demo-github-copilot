# AI Document Reader - Backend

API backend para el demo de IA con Google Gemini.

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
```

Editar `.env` y agregar tu API key de Google Gemini:
```
GEMINI_API_KEY=tu_api_key_aquí
```

Para obtener una API key de Gemini:
1. Ve a https://aistudio.google.com/app/apikey
2. Crea una nueva API key
3. Copia y pégala en el archivo `.env`

## Ejecución

```bash
python main.py
```

O usando uvicorn:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: http://localhost:8000

## Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /health` - Check de salud
- `POST /chat` - Chat sin streaming
- `POST /chat/stream` - Chat con streaming en tiempo real

## Documentación

La documentación interactiva estará disponible en:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)