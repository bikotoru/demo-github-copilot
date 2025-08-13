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
  * El sidebar debe ser responsive y colapsable en móviles usando componentes ShadCN UI con animaciones fluidas
  * Mantener el theme provider y modo oscuro existente con transiciones elegantes entre temas
  * Máximo 100 conversaciones guardadas (eliminar las más antiguas automáticamente)
  * Diseño general debe ser visualmente atractivo, moderno y profesional, similar a aplicaciones como ChatGPT o Claude
