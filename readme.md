# Backend Restaurante Izarza


## Cómo descargar y poner en funcionamiento el proyecto

Sigue estos pasos para clonar el repositorio y configurar tu entorno de desarrollo localmente.

### Paso 1: Clonar el repositorio

1. Abre una terminal o línea de comandos.
2. Ejecuta el siguiente comando para clonar el repositorio:

   ```sh
   git clone https://github.com/EpicScopeProject/epic_scope_backend.git
   cd epic_scope_backend
   ```

### Paso 2: Crear un entorno virtual (recomendado)

1. Crea un entorno virtual con el siguiente comando:

   * opción a:

   ```sh
   python -m venv venv
   ```

   * opción b:

   ```sh
   virtualenv -p python3 env  
   ```

2. Activa el entorno virtual:

   - En Windows:

     ```sh
     venv\Scripts\activate
     ```

   - En macOS/Linux:


      * opción a:

     ```sh
     source venv/bin/activate
     ```

      * opción b:

      ```sh
     source env/bin/activate
     ```
     

### Paso 3: Instalar las dependencias

1. Asegúrate de que estás en la raíz del proyecto.
2. Ejecuta el siguiente comando para instalar las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

### Paso 4: Configurar variables de entorno

1. Crea un archivo `.env` en la raíz del proyecto.
2. Añade las siguientes variables de entorno al archivo `.env`:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   MYSQL_HOST=localhost
   MYSQL_USER=nombre_usuario
   MYSQL_PASSWORD=contraseña_usuario
   MYSQL_DB=nombre_base_datos
   SECRET_KEY=clave
   ```

### Paso 5: Ejecutar la aplicación

1. Asegúrate de que el entorno virtual está activado.
2. Ejecuta el siguiente comando para iniciar la aplicación Flask:

   ```sh
   flask run
   ```

3. La aplicación debería estar ejecutándose en `http://localhost:5001`.

### Nota

Asegúrate de tener instalado MySQL y configurado correctamente con las credenciales proporcionadas en el archivo `.env`.

---

Siguiendo estos pasos, deberías tener el proyecto en funcionamiento en tu entorno local. Si encuentras algún problema o tienes alguna duda, no dudes en consultar la documentación o comunicarte con el equipo.
