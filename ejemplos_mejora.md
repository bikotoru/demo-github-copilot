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
#file:templatenextjs/app/ai-chat/page.tsx

En Python usando FastAPI y TypeScript usando Next.js con React, crea un sistema de historial de conversaciones persistente:

- Objetivo principal: Guardar y recuperar conversaciones completas entre el usuario y la IA
- Requisitos específicos:
  * Backend: Crear endpoints GET /conversations, GET /conversations/{id}, POST /conversations, DELETE /conversations/{id}
  * Cada conversación debe tener: id único (UUID), título auto-generado, timestamp de creación, array de mensajes
  * Almacenar datos en archivo JSON (conversations.json) sin base de datos
  * Frontend: Agregar sidebar izquierdo con lista de conversaciones, click para cargar conversación
  * Auto-generar títulos basados en los primeros 50 caracteres del primer mensaje del usuario
- Contexto: La aplicación actual es un chat con IA que usa streaming, pero las conversaciones se pierden al recargar
- Restricciones: 
  * No usar base de datos, solo archivos JSON
  * Mantener compatibilidad con el sistema de streaming actual
  * El sidebar debe ser responsive y colapsable en móviles
  * Máximo 100 conversaciones guardadas (eliminar las más antiguas automáticamente)
```

**Archivos a modificar:**
- `backend/main.py` (nuevos endpoints)
- `templatenextjs/app/ai-chat/page.tsx` (sidebar y funcionalidad)
- Crear: `backend/conversations.json` (almacenamiento)

---

# Mejora 2: Soporte para Renderizado de Markdown

**Prompt Estructurado:**

```
#file:templatenextjs/app/ai-chat/page.tsx

En TypeScript usando Next.js con React y ShadCN UI, implementa renderizado de Markdown en los mensajes del chat:

- Objetivo principal: Mostrar mensajes con formato Markdown (negrita, cursiva, código, listas, enlaces, etc.)
- Requisitos específicos:
  * Instalar y configurar react-markdown y react-syntax-highlighter
  * Renderizar mensajes de la IA con formato Markdown completo
  * Syntax highlighting para bloques de código con nombres de lenguajes
  * Soporte para tablas, listas, enlaces, imágenes
  * Mantener el estilo visual actual del chat (colores, espaciado, bordes redondeados)
  * Agregar botón "copiar código" en bloques de código
- Contexto: Los mensajes actualmente se muestran como texto plano, pero la IA a menudo responde con Markdown
- Restricciones:
  * Mantener compatibilidad con el streaming actual (renderizar Markdown incremental)
  * Los estilos deben respetar el tema oscuro/claro actual
  * Sanitizar contenido para evitar XSS
  * No afectar el rendimiento del streaming
```

**Archivos a modificar:**
- `templatenextjs/app/ai-chat/page.tsx` (renderizado de markdown)
- `templatenextjs/package.json` (nuevas dependencias)

---

# Mejora 3: Contador de Tokens de Entrada y Salida

**Prompt Estructurado:**

```
#file:backend/main.py
#file:templatenextjs/app/ai-chat/page.tsx

En Python usando FastAPI y TypeScript usando Next.js, implementa un sistema de conteo de tokens:

- Objetivo principal: Mostrar tokens de entrada y salida consumidos en cada mensaje para control de costos
- Requisitos específicos:
  * Backend: Calcular tokens antes y después de cada llamada a Gemini
  * Usar la función count_tokens() de la API de Gemini para conteo preciso
  * Retornar en la respuesta: input_tokens, output_tokens, total_tokens
  * Frontend: Mostrar contadores debajo de cada mensaje con iconos
  * Agregar contador total de la sesión en la parte superior del chat
  * Mostrar costo estimado basado en precios actuales de Gemini
- Contexto: Los usuarios necesitan controlar el consumo de tokens para gestionar costos de API
- Restricciones:
  * Mantener compatibilidad con streaming (actualizar contadores en tiempo real)
  * Los contadores deben ser discretos visualmente pero informativos
  * Incluir opción para ocultar/mostrar información de tokens
  * Calcular tokens solo cuando sea necesario para optimizar rendimiento
```

**Archivos a modificar:**
- `backend/main.py` (cálculo de tokens)
- `templatenextjs/app/ai-chat/page.tsx` (UI de contadores)

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

**¿Listo para probar? Copia cualquier prompt y pruébalo con tu IA favorita! 🚀**