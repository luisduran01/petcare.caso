# PetCare API Backend - Arquitectura Hexagonal

Proyecto full-stack desarrollado para la evaluación de Back End. Consta de un servidor en Django (implementando arquitectura hexagonal) conectado a un Front End existente en React. La API simula una base de datos documental (NoSQL) hacia el cliente, mientras persiste los datos de manera relacional (SQL) utilizando `db.sqlite3`.

## ⚙️ Arquitectura del Back End (Hexagonal)

El proyecto Django está dividido en 4 capas estrictas para separar la lógica de negocio del framework:

*   **`domain/`**: Entidades puras (`Servicio`, `Reserva`) y contratos de los repositorios. Cero dependencias de Django.
*   **`application/`**: Casos de uso con la lógica del CRUD y excepciones de negocio (`ListarReservasUseCase`, `CrearReservaUseCase`, etc.).
*   **`infrastructure/`**: Modelos ORM de Django (`ServicioModel`, `ReservaModel`), implementación de los repositorios y contenedor de inyección de dependencias (`di.py`).
*   **`api/`**: Adaptadores primarios que manejan HTTP. Serializers, Vistas (`views.py`) que traducen las peticiones y Rutas (`urls.py`).

## 🚀 Cómo levantar el Back End

1.  Abre una terminal en la carpeta del backend (`hexagonal_api`).
2.  Crea y activa un entorno virtual:
    ```bash
    python -m venv entorno
    # Windows:
    entorno\Scripts\activate
    # Mac/Linux:
    source entorno/bin/activate
    ```
3.  Instala las dependencias necesarias:
    ```bash
    pip install django djangorestframework django-cors-headers
    ```
4.  Aplica las migraciones para construir la base de datos SQL:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Levanta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## 🔑 Autenticación y Token

Toda la API está protegida y requiere autenticación mediante Token (`Authorization: Token <tu_token>`).

1.  Con el entorno virtual activado, crea un administrador:
    ```bash
    python manage.py createsuperuser
    ```
2.  Para obtener el Token, realiza una petición **POST** a `http://127.0.0.1:8000/api/token/` enviando en el Body (formato *Form-encode*) tu `username` y `password`.
3.  Copia el token devuelto.
4.  Abre el archivo `src/services/api.js` en el proyecto de React y actualiza la constante `TOKEN` (Ej: `const TOKEN = 'Token tu_codigo_aqui';`).

**⚠️ IMPORTANTE ANTES DE USAR EL FRONTEND:**
Antes de crear la primera reserva desde React, ingresa al panel de administración (`http://127.0.0.1:8000/admin/`) y crea al menos un **Servicio** en el catálogo. La base de datos relacional exige que cada reserva esté asociada a un servicio válido mediante una llave foránea (ID).

## 🌐 Cómo levantar el Front End (React)

1.  Abre una nueva terminal en la carpeta del frontend (`petcare`).
2.  Instala las dependencias:
    ```bash
    pnpm install
    # o npm install
    ```
3.  Inicia el entorno de desarrollo:
    ```bash
    pnpm dev
    # o npm run dev
    ```

## 📡 Lista de Endpoints

### Catálogo: Servicios
*   `GET /api/servicios/` - Listar todos los servicios
*   `POST /api/servicios/` - Crear un nuevo servicio
*   `GET /api/servicios/<id>/` - Obtener detalle de un servicio
*   `PUT /api/servicios/<id>/` - Actualizar un servicio existente
*   `DELETE /api/servicios/<id>/` - Eliminar un servicio

### Transaccional: Reservas
*   `GET /api/reservas/` - Listar todas las reservas médicas
*   `POST /api/reservas/` - Crear una reserva médica (Acepta JSON anidado)
*   `GET /api/reservas/<id>/` - Obtener detalle de una reserva
*   `PUT /api/reservas/<id>/` - Actualizar una reserva existente
*   `DELETE /api/reservas/<id>/` - Eliminar una reserva