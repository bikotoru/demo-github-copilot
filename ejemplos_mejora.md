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

En Python usando FastAPI y TypeScript usando Next.js con React, crea un sistema de historial de conversaciones persistente:

- Objetivo principal: Guardar y recuperar conversaciones completas entre el usuario y la IA
- Requisitos específicos:
  * Backend: Crear endpoints GET /conversations, GET /conversations/{id}, POST /conversations, DELETE /conversations/{id}
  * Cada conversación debe tener: id único (UUID), título auto-generado, timestamp de creación, array de mensajes
  * Almacenar datos en archivo JSON (conversations.json) sin base de datos
  * Frontend: Modificar el componente Chat existente para agregar sidebar izquierdo elegante con lista de conversaciones
  * Implementar funcionalidad para crear nueva conversación, cargar conversación existente, eliminar conversación
  * Auto-generar títulos basados en los primeros 50 caracteres del primer mensaje del usuario
  * Usar componentes ShadCN UI existentes (Button, ScrollArea, Separator, etc.) con diseño moderno y elegante
  * Aplicar hover effects, transiciones suaves y micro-interacciones para una experiencia premium
  * El sidebar debe verse profesional con iconos apropiados, espaciado correcto y jerarquía visual clara
- Contexto: La aplicación actual usa el componente Chat en frontend/components/chat.tsx con streaming hacia backend FastAPI, pero las conversaciones se pierden al recargar
- Restricciones: 
  * No usar base de datos, solo archivos JSON
  * Mantener compatibilidad con el sistema de streaming actual en /chat/stream
  * El sidebar debe ser responsive y colapsable en móviles usando componentes ShadCN UI con animaciones fluidas
  * Mantener el theme provider y modo oscuro existente con transiciones elegantes entre temas
  * Máximo 100 conversaciones guardadas (eliminar las más antiguas automáticamente)
  * Diseño general debe ser visualmente atractivo, moderno y profesional, similar a aplicaciones como ChatGPT o Claude
```

**Archivos a modificar:**
- `backend/main.py` (nuevos endpoints)
- `frontend/components/chat.tsx` (sidebar y funcionalidad)
- Crear: `backend/conversations.json` (almacenamiento)

---

# Mejora 2: Soporte para Renderizado de Markdown

**Prompt Estructurado:**

```
#file:frontend/components/chat.tsx
#file:frontend/package.json

En TypeScript usando Next.js con React y ShadCN UI, implementa renderizado de Markdown en los mensajes del chat:

- Objetivo principal: Mostrar mensajes con formato Markdown (negrita, cursiva, código, listas, enlaces, etc.)
- Requisitos específicos:
  * Instalar y configurar react-markdown y react-syntax-highlighter
  * Modificar el componente Chat existente para renderizar mensajes de la IA con formato Markdown elegante
  * Syntax highlighting para bloques de código con nombres de lenguajes y esquema de colores atractivo
  * Soporte para tablas, listas, enlaces, imágenes con estilos visuales pulidos
  * Mejorar el estilo visual del chat manteniendo colores ShadCN UI pero con mayor refinamiento
  * Agregar botón "copiar código" elegante en bloques de código con efectos hover y feedback visual
  * Integrar con el tema oscuro/claro existente usando next-themes con transiciones suaves
  * Aplicar tipografía mejorada, espaciado óptimo y jerarquía visual clara para contenido Markdown
  * Diseño debe ser moderno, limpio y profesional, similar a interfaces de documentación premium
- Contexto: La aplicación actual usa frontend/components/chat.tsx que muestra mensajes como texto plano, pero la IA Gemini responde con Markdown
- Restricciones:
  * Mantener compatibilidad con el streaming actual (renderizar Markdown incremental durante el streaming)
  * Los estilos deben respetar el tema oscuro/claro actual usando CSS variables de ShadCN
  * Sanitizar contenido para evitar XSS
  * No afectar el rendimiento del streaming en /chat/stream
  * Usar solo los componentes ShadCN UI ya instalados donde sea posible
  * El resultado final debe verse elegante, moderno y profesional con atención al detalle en UX/UI
```

**Archivos a modificar:**
- `frontend/components/chat.tsx` (renderizado de markdown)
- `frontend/package.json` (nuevas dependencias)

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

**¿Listo para probar? Copia cualquier prompt y pruébalo con tu IA favorita! 🚀**