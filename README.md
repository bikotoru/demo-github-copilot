# 🤖 AI Document Reader Demo

Demo completo que muestra cómo funciona la IA para leer documentos y mantener conversaciones inteligentes.

## 🏗️ Arquitectura

- **Backend**: Python FastAPI + Google Gemini AI
- **Frontend**: Next.js 15 + ShadCN UI + Tailwind CSS
- **Funcionalidades**: Chat en tiempo real con streaming, modo oscuro, y UI elegante

## 🚀 Instalación Rápida

### Backend (Python)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edita `.env` y agrega tu API key de Google Gemini:
```bash
GEMINI_API_KEY=tu_api_key_aquí
```

Para obtener la API key: https://aistudio.google.com/app/apikey

Ejecutar:
```bash
python main.py
```

### Frontend (Next.js)

```bash
cd templatenextjs
npm install  # o bun install
npm run dev  # o bun dev
```

## 🔧 Uso

1. Inicia el backend (puerto 8000)
2. Inicia el frontend (puerto 3000)
3. Ve a http://localhost:3000
4. ¡Disfruta chateando con la IA!

## ✨ Características

- 💬 **Chat en tiempo real** con streaming de respuestas
- 🌙 **Modo oscuro/claro** elegante
- 🗑️ **Limpiar conversación** con un click
- 📱 **Diseño responsivo** y moderno
- 🎨 **UI atractiva** con ShadCN UI y animaciones
- 🔒 **CORS configurado** para desarrollo
- ⚡ **Respuestas rápidas** con Google Gemini

## 📁 Estructura

```
├── backend/                 # API Python FastAPI
│   ├── main.py             # Servidor principal
│   ├── requirements.txt    # Dependencias Python
│   └── .env.example       # Variables de entorno
└── templatenextjs/         # Frontend Next.js
    ├── app/ai-chat/       # Página del chat
    ├── components/ui/     # Componentes ShadCN
    └── package.json       # Dependencias Node
```

## 🛠️ Tecnologías

### Backend
- FastAPI (API REST)
- Google Generative AI (Gemini)
- Python Dotenv (variables de entorno)
- Uvicorn (servidor ASGI)

### Frontend
- Next.js 15 (React framework)
- TypeScript (tipado estático)
- ShadCN UI (componentes)
- Tailwind CSS (estilos)
- next-themes (modo oscuro)
- Lucide React (iconos)

## 🔍 API Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /health` - Status de la API
- `POST /chat` - Chat simple
- `POST /chat/stream` - Chat con streaming (recomendado)

## 📝 Próximas Mejoras

- [ ] Subida de documentos (PDF, Word, etc.)
- [ ] Análisis de imágenes
- [ ] Historial de conversaciones
- [ ] Autenticación de usuarios
- [ ] Rate limiting
- [ ] Métricas y analytics