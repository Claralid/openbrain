# OpenBrain: Arquitectura del Producto

Esta es la estructura organizativa visible de OpenBrain, diseñada para ser intuitiva, modular y orientada a la base operativa. Cada sección agrupa las capacidades del sistema de manera lógica y accesible para el usuario.

## 1. Personality
*Define quién es OpenBrain y cómo interactúa con el usuario.*

* **Identidad:** El rol principal, los atributos base y los parámetros de comportamiento de la IA.
* **Tono:** El estilo de comunicación (ej. formal, amigable, técnico, conciso).
* **Forma de ser:** Rasgos de personalidad adaptables y directrices sobre cómo responder ante diferentes escenarios.

## 2. Context
*El ecosistema de conocimiento y memoria que alimenta a OpenBrain.*

* **Projects:** Agrupación y gestión de objetivos, documentos y estados de trabajo en curso.
* **Memory:** Base de datos persistente sobre el usuario, preferencias y aprendizajes pasados (evita tener que repetir contexto).
* **Chats:** Historial accesible de hilos de conversaciones activas y pasadas.
* **Plugins:** Integraciones y herramientas externas que actúan como "sentidos" adicionales para la IA dentro de su entorno.

## 3. Operative
*El motor de acción enfocado en la productividad diaria.*

* **Tasks:** Gestión clara de tareas pendientes, en progreso y completadas.
* **Reminders:** Sistema de alertas, notificaciones y recordatorios programados.
* **Routines:** Secuencias de acciones automatizadas o flujos de trabajo repetitivos predefinidos.

## 4. Settings
*La sala de máquinas: configuración técnica y administración del entorno.*

* **Providers:** Gestión de conexiones y claves API a proveedores de IA (OpenAI, Anthropic, etc.).
* **Models:** Selección del modelo de lenguaje específico o la ruta de modelos a utilizar según la tarea.
* **Security:** Controles de privacidad, límites de acceso, manejo de datos sensibles y seguridad local.
* **Updates:** Control de versiones, parches y actualizaciones del sistema base de OpenBrain.

---

## Componente Transversal: Viewer
*Visor integrado nativo para el manejo rápido de recursos.*

Más allá de las 4 secciones principales, OpenBrain incorpora un **Viewer** de alto rendimiento como capacidad central del sistema. 

* **Para Imágenes:** Previsualización rápida de referencias visuales, flujos y capturas adjuntas.
* **Para Documentos:** Lectura rápida de PDFs, archivos Markdown, código y texto rico sin necesidad de abrir aplicaciones externas.

*Nota de diseño:* El Viewer actúa de manera dinámica (como un panel lateral o modal emergente) sobre cualquier sección del sistema, permitiendo revisar información visual y documental sin interrumpir el flujo de conversación o trabajo en curso.
