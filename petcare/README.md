# 🐾 PetCare - Landing Page & Sistema CRUD Médico

Proyecto frontend desarrollado para la evaluación del Caso 5: Aplicación móvil de salud veterinaria. Incluye una Landing Page completamente responsiva y un panel de administración CRUD conectado a una API centralizada.

## 🚀 Tecnologías Utilizadas

* **React 18+**: Desarrollo basado en componentes funcionales y manejo de estado con Hooks (`useState`, `useEffect`).
* **Vite**: Entorno de desarrollo y bundler ultrarrápido.
* **Bootstrap 5**: Utilizado para el sistema de grillas (Grid), diseño responsivo, y componentes interactivos (Modales, Acordeones).
* **JavaScript (ES6+)**: Lógica de peticiones asíncronas (`fetch`, `async/await`) y manipulación de datos.

## 📋 Características Principales

### 1. Landing Page Responsiva
* **Navegación:** Navbar responsivo con menú tipo hamburguesa y botones funcionales para alternar entre vistas.
* **Hero Section:** Propuesta de valor principal con Call to Action (CTA).
* **Interactividad:** Acordeón de funciones destacadas y Modal dinámico para la sección de testimonios.
* **Diseño Adaptable:** Optimizado para visualización en dispositivos móviles (360px), tablets (768px) y monitores desktop (1920px).

### 2. Panel CRUD (Gestión de Reservas)
Sistema completo de gestión conectado al endpoint de Inacode (`apiclases.inacode.cl/mascotas`) respetando estrictamente el modelo de datos anidado.
* **Create (Crear):** Registro de nuevas mascotas y dueños procesando formularios controlados y adaptando el payload al modelo JSON requerido.
* **Read (Leer):** Consumo asíncrono de la API para visualizar los datos en una tabla dinámica, con estado de carga (spinner) integrado.
* **Update (Actualizar):** Modificación de registros existentes utilizando el método `PUT`, precargando datos en el formulario mediante aplanamiento de objetos.
* **Delete (Borrar):** Eliminación segura de registros con confirmación de usuario y método `DELETE`.

## ⚙️ Arquitectura y Soluciones Técnicas

* **Estructura de Carpetas:** Separación lógica en `/components`, `/pages` y `/services` para un código limpio, escalable y mantenible.
* **Manejo de CORS y WAF:** Se configuró un proxy de desarrollo en Vite para gestionar las solicitudes a la API y evitar problemas de CORS durante el desarrollo.
* **Headers Estrictos:** Inyección de `Content-Type: application/json` en los servicios de API para evitar errores `415 Unsupported Media Type`.

## 🔧 Instalación y Ejecución Local

Sigue estos pasos para desplegar el proyecto en cualquier entorno local:

1.  **Instalar dependencias:**
    Asegúrate de tener Node.js instalado. Abre la terminal en la raíz del proyecto y ejecuta:
    ```bash
    pnpm install
    ```
    *(Nota: Si usas npm, ejecuta `npm install`)*

2.  **Iniciar el servidor de desarrollo:**
    ```bash
    pnpm dev
    ```

3.  **Visualización:**
    Abre tu navegador web e ingresa a la ruta local proporcionada por la terminal (generalmente `http://localhost:5173`).
