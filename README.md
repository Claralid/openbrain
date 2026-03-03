# OpenBrain 🧠✨

**OpenBrain** es una interfaz de gestión inteligente diseñada específicamente para **OpenClaw**. Transforma la experiencia de configuración local en un panel de control moderno, fluido y visualmente impactante.

## ✨ Características Principales

- **Arquitectura SPA (Single Page Application)**: Navegación instantánea entre secciones sin recargas de página.
- **Dashboard de Métricas**: Visualización de actividad de tokens, costo estimado y uso por modelo de IA (GPT-4, Claude, Llama, etc.).
- **Gestión de Skills**: Activa y desactiva tus habilidades instaladas con un solo clic.
- **Editor JSON Integrado**: Administra tu archivo `openclaw.json` con validación y resaltado de sintaxis.
- **Control de Backups**: Crea y gestiona puntos de restauración integrales de tu entorno.
- **Modo Oscuro/Claro**: Interfaz premium adaptable a tus preferencias visuales.

## 🚀 Instalación

Puedes instalar OpenBrain directamente desde el código fuente:

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/openbrain.git
cd openbrain

# Instalar el paquete en modo editable
pip install -e .
```

## 🛠️ Uso

OpenBrain incluye una interfaz de línea de comandos (CLI) extremadamente sencilla:

### Iniciar el Servidor Web
```bash
openbrain start
```
Luego abre tu navegador en `http://localhost:5050`.

### Ver Estado del Sistema
```bash
openbrain status
```

### Crear un Backup Manual
```bash
openbrain backup
```

## 📁 Estructura del Proyecto

- `openbrain/core.py`: Lógica de negocio (configuración, skills, backups, métricas).
- `openbrain/api.py`: Backend basado en FastAPI.
- `openbrain/templates.py`: Interfaz de usuario (HTML/JS/Tailwind) con arquitectura SPA.
- `openbrain/cli.py`: Interfaz de línea de comandos.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
