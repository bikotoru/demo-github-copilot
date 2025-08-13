# 🚀 Ejemplos de Mejoras para AI Document Reader

Esta lista contiene prompts específicos y claros para implementar mejoras en la aplicación. Cada mejora está diseñada para ser implementada de forma independiente y probar las capacidades de IA para desarrollo.

## 📋 Formato de Prompts

Cada prompt sigue esta estructura para mejores resultados:

```
#file:[nombre del archivo]
En [lenguaje de programación], usando [framework], crea [descripción de la tarea]:
- Objetivo principal: [qué se quiere lograr]
- Requisitos específicos: [lista detallada de características]
- Contexto: [situación actual y por qué se necesita]
- Restricciones: [limitaciones técnicas y de diseño]
```

## 🎯 Mejoras Prioritarias

Las siguientes 3 mejoras están listas para implementar con prompts estructurados:

---

# Mejora 1: Historial de Conversaciones Persistente

**Prompt Estructurado:**

```
#file:backend/main.py
#file:frontend/components/chat.tsx
#file:frontend/app/page.tsx

En Python usando FastAPI y TypeScript usando Next.js con React, implementa desde cero un sistema de historial de conversaciones persistente:

- Objetivo principal: Crear un sistema completo para guardar y navegar conversaciones entre el usuario y la IA
- Requisitos específicos:
  * Backend: Crear endpoints GET /conversations, GET /conversations/{id}, POST /conversations, DELETE /conversations/{id}, PUT /conversations/{id}
  * ESTRUCTURA CORRECTA del JSON: Una conversación = UN objeto con múltiples mensajes dentro
  * Estructura conversations.json:
    ```json
    [
      {
        "id": "uuid-unico",
        "title": "Título auto-generado",
        "created_at": "2025-01-01T12:00:00Z",
        "updated_at": "2025-01-01T12:05:00Z",
        "messages": [
          {"user": "Hola", "timestamp": "2025-01-01T12:00:00Z"},
          {"assistant": "¡Hola! ¿Cómo puedo ayudarte?", "timestamp": "2025-01-01T12:00:30Z"},
          {"user": "¿Qué es Python?", "timestamp": "2025-01-01T12:01:00Z"},
          {"assistant": "Python es un lenguaje...", "timestamp": "2025-01-01T12:01:30Z"}
        ]
      }
    ]
    ```
  * FLUJO CORRECTO: 
    1. Al enviar primer mensaje → crear nueva conversación con POST /conversations
    2. Al enviar mensajes siguientes → actualizar conversación existente con PUT /conversations/{id}
    3. Una conversación puede tener N mensajes, NO crear nueva conversación por cada mensaje
  * Frontend: Modificar el componente Chat para agregar sidebar elegante con lista de conversaciones
  * NAVEGACIÓN POR URL: Implementar ?id=xxx en la URL para navegar directamente a conversaciones específicas
    - URL: http://localhost:3000/?id=uuid-conversacion
    - Al cargar la página, detectar parámetro ?id y cargar esa conversación automáticamente
    - Al seleccionar conversación del sidebar, actualizar URL con ?id=xxx sin recargar página
    - Botón "Nueva conversación" debe limpiar el parámetro ?id de la URL
  * Implementar funcionalidad completa: crear, cargar, eliminar conversaciones
  * Auto-generar títulos basados en los primeros 50 caracteres del primer mensaje del usuario
  * Usar componentes ShadCN UI existentes (Button, ScrollArea, Separator, etc.) con diseño moderno y elegante
  * Aplicar hover effects, transiciones suaves y micro-interacciones para una experiencia premium
  * El sidebar debe verse profesional con iconos apropiados, espaciado correcto y jerarquía visual clara
- Contexto: La aplicación actual es un chat básico en frontend/components/chat.tsx que se conecta al backend FastAPI con streaming. Necesitamos agregar persistencia y navegación por URL.
- Restricciones: 
  * No usar base de datos, solo archivos JSON
  * Mantener compatibilidad con el sistema de streaming actual en /chat/stream
  * CRÍTICO: Una conversación = un objeto JSON con array de mensajes
  * Implementar navegación por URL con parámetros de query (?id=xxx)
  * PERSISTENCIA DE ESTADO: Al cambiar la URL/ruta, mantener la conexión activa con la conversación sin perder datos
  * CONFIRMACIÓN DE ELIMINACIÓN: Al eliminar conversación, mostrar dialog/alert de confirmación antes de proceder
  * ACTUALIZACIÓN DINÁMICA: Al eliminar conversación, remover inmediatamente del sidebar sin recargar página
  * DISEÑO RESPONSIVO COMPLETO: La aplicación debe funcionar perfectamente en móviles, tablets y desktop
    - Sidebar colapsable en móviles con animaciones fluidas usando componentes ShadCN UI
    - Chat area debe adaptarse correctamente a diferentes tamaños de pantalla
    - Input y botones deben ser touch-friendly en móviles
    - Textos y elementos UI deben escalar apropiadamente
  * Mantener el theme provider y modo oscuro existente con transiciones elegantes entre temas
  * Máximo 100 conversaciones guardadas (eliminar las más antiguas automáticamente)
  * Diseño general debe ser visualmente atractivo, moderno y profesional, similar a aplicaciones como ChatGPT o Claude
```

**Archivos a crear/modificar:**
- `backend/main.py` (agregar endpoints de conversaciones)
- `frontend/components/chat.tsx` (agregar sidebar y lógica de navegación URL)
- `backend/conversations.json` (archivo de almacenamiento)

---

# Mejora 2: Soporte para Renderizado de Markdown

**Prompt Estructurado:**

```
#file:frontend/components/chat.tsx

En TypeScript usando Next.js con React y ShadCN UI, agrega soporte para renderizado de Markdown en los mensajes del chat:

- Objetivo principal: Los mensajes de la IA deben mostrarse con formato Markdown (código, listas, enlaces, etc.) en lugar de texto plano
- Requisitos específicos:
  * Solo los mensajes de la IA deben renderizarse como Markdown (los mensajes del usuario siguen como texto plano)
  * Soporte para: bloques de código con syntax highlighting, código inline, listas, enlaces, tablas, citas, imágenes
  * Botón "copiar" en bloques de código con feedback visual
  * Diseño elegante que mantenga la consistencia visual del chat actual
  * Totalmente responsivo - no debe romper el diseño en móviles
  * Integración perfecta con tema oscuro/claro existente
  * Sanitización de contenido por seguridad
  * Compatible con streaming incremental (renderizar mientras se recibe el texto)
- Contexto: Chat con IA que actualmente muestra todos los mensajes como texto plano, pero la IA responde con Markdown
- Restricciones:
  * SOLO modificar el frontend - NO tocar backend/main.py ni endpoints
  * No afectar el streaming ni la funcionalidad existente del chat
  * Mantener el diseño responsivo actual
  * Usar componentes ShadCN UI existentes donde sea posible
```

**Archivos a modificar:**
- `frontend/components/chat.tsx` (agregar renderizado Markdown solo para mensajes IA)

---

# Mejora 3: Contador de Tokens de Entrada y Salida

**Prompt Estructurado:**

```
#file:backend/main.py
#file:frontend/components/chat.tsx

En Python usando FastAPI y TypeScript usando Next.js con ShadCN UI, implementa un sistema de conteo de tokens:

- Objetivo principal: Mostrar tokens de entrada y salida consumidos en cada mensaje para control de costos
- Requisitos específicos:
  * Backend: Modificar el endpoint /chat/stream para calcular tokens antes y después de cada llamada a Gemini
  * Usar la función count_tokens() de la API de Gemini para conteo preciso
  * Retornar en la respuesta streaming: input_tokens, output_tokens, total_tokens
  * Frontend: Modificar el componente Chat existente para mostrar contadores elegantes debajo de cada mensaje con iconos de Lucide React
  * Agregar contador total de la sesión visualmente atractivo en la cabecera del chat (junto al toggle de tema)
  * Mostrar costo estimado basado en precios actuales de Gemini (input: $0.000125/1K tokens, output: $0.000375/1K tokens) con formato monetario claro
  * Usar Badge component de ShadCN UI con colores apropiados y diseño pulido para mostrar la información de tokens
  * Implementar micro-animaciones y transiciones suaves para la actualización de contadores
  * Diseño de contadores debe ser discreto pero informativo, con jerarquía visual clara y estética profesional
- Contexto: La aplicación actual usa streaming en /chat/stream y el componente Chat, los usuarios necesitan controlar costos
- Restricciones:
  * Mantener compatibilidad con streaming actual (actualizar contadores en tiempo real durante el stream)
  * Los contadores deben ser discretos visualmente usando componentes ShadCN UI pero informativos
  * Incluir Toggle component elegante para ocultar/mostrar información de tokens con transiciones suaves
  * Calcular tokens solo cuando sea necesario para optimizar rendimiento
  * Respetar el tema oscuro/claro existente con diseño cohesivo y profesional
  * La interfaz completa debe mantener la elegancia y modernidad del chat existente
```

**Archivos a modificar:**
- `backend/main.py` (cálculo de tokens)
- `frontend/components/chat.tsx` (UI de contadores)

---

## 💡 Instrucciones de Uso

1. **Copia el prompt estructurado** de cualquiera de las 3 mejoras anteriores
2. **Pégalo directamente** en tu modelo de IA preferido (Claude, ChatGPT, etc.)
3. **El modelo tendrá contexto completo** sobre los archivos existentes y qué hacer
4. **Cada mejora es independiente** - puede implementarse sin las otras
5. **Formato probado** - esta estructura da mejores resultados que prompts simples

## 🔄 Próximas Mejoras

Si estas 3 mejoras funcionan bien, podemos crear más prompts estructurados para:
- Subida y análisis de documentos
- Sistema de plantillas de prompts  
- Análisis de imágenes con Gemini Vision
- Exportación de conversaciones
- Dashboard de estadísticas
- Búsqueda global en conversaciones

---

# Mejora 4: Migración del Backend a .NET 9

**Prompt Estructurado:**

```
#file:backend/main.py

En C# usando .NET 9 con ASP.NET Core Minimal APIs, migra completamente el backend actual de Python FastAPI a .NET:

- Objetivo principal: Reemplazar el backend Python por una implementación equivalente en .NET 9 manteniendo toda la funcionalidad
- Requisitos específicos:
  * Crear nuevo proyecto .NET 9 con Minimal APIs (Program.cs)
  * Implementar todos los endpoints existentes: GET /, GET /health, GET /test-gemini, POST /chat, POST /chat/stream
  * Integrar Google Gemini API usando HttpClient y JSON para las llamadas REST
  * Configurar CORS para permitir conexiones desde localhost:3000
  * Implementar streaming de respuestas usando Server-Sent Events (SSE)
  * Usar System.Text.Json para serialización/deserialización
  * Configurar variables de entorno con appsettings.json y User Secrets
  * Mantener la misma estructura de request/response que el Python actual
- Contexto: El backend Python funciona perfectamente, pero necesitamos una versión .NET para comparar rendimiento y explorar el ecosistema .NET
- Restricciones:
  * Mantener exactamente la misma API (mismos endpoints, mismos formatos JSON)
  * El frontend Next.js NO debe necesitar cambios
  * Usar solo librerías nativas de .NET, no paquetes third-party para Gemini
  * Configurar puerto 8001 para evitar conflictos con el Python (puerto 8000)
  * Incluir logging con ILogger para debugging
  * Manejar errores de forma robusta con try-catch
```

**Archivos a crear:**
- `backend-dotnet/Program.cs` (API principal)
- `backend-dotnet/Models/ChatModels.cs` (DTOs)
- `backend-dotnet/Services/GeminiService.cs` (integración con Gemini)
- `backend-dotnet/backend-dotnet.csproj` (proyecto)
- `backend-dotnet/appsettings.json` (configuración)
- `backend-dotnet/README.md` (instrucciones específicas .NET)

**Estructura esperada:**
```
backend-dotnet/
├── Program.cs
├── Models/
│   └── ChatModels.cs
├── Services/
│   └── GeminiService.cs
├── backend-dotnet.csproj
├── appsettings.json
└── README.md
```

---

