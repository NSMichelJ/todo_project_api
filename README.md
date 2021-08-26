## TODO Project API
Una API simple que te permitirá agregar/recuperar proyectos con las tareas para cada proyecto.

## Instalación
Clona este repo
```bash
git clone https://github.com/NSMichelJ/todo_project_api.git
```

Instala las dependencias
```bash
pip install requirements.txt
```

Configura las variables de entorno
```bash
set FLASK_APP=entrypoint:app
set FLASK_ENV=development
```

Ejecuta las migraciones
```bash
flask db upgrade
```

Corre la app
```bash
flask run
```

## Estructura del proyecto
```
todo_project_api
├── app
│   ├── todo
│   │   ├── __init__.py   
│   │   ├── models.py       // Modelos de la app
│   │   ├── resources.py    // Endpoints de la api
│   │   ├── schema.py       // Esquema para serializar los modelos
│   │   └── todo.py         // Lógica para mostrar los recursos
│   └── __init__.py         // Configuración de la app
│          
├── config  
│   ├── __init__.py
│   └── default.py          // Configuración por defecto
│   
└── entrypoint.py           // Crea la instancia de la app
```

## Recursos
```
Methods           Route
----------------  ------------------------
GET               /
DELETE, GET, PUT  /api/v1/project/<int:id>
GET, POST         /api/v1/projects/
DELETE, PUT       /api/v1/task/<int:id>
```

## Ejemplo
### Obtener todos los proyectos

Realiza una petición GET a la URL http://localhost:5000/api/v1/projects/

### Agregar un proyecto

Realiza una petición POST a la URL http://localhost:5000/api/v1/projects/ con el siguiente contenido:
```json
{
  "title": "some project",
  "description": "some decription",
  "tasks": [
    {"task": "task 1"},
    {"task": "task 2"}
  ]
}
```

### Obtener un proyecto por id
Realiza una petición GET a la URL http://localhost:5000/api/v1/project/1

### Actualizar un proyecto

Realiza una petición PUT a la URL http://localhost:5000/api/v1/project/1

#### Actualizar el titulo
```json
{
  "title": "new some project"
}
```

#### Actualizar la descripción
```json
{
  "description": "new some project"
}
```

#### Agregar tareas
```json
{
  "tasks": [
    {"task": "task 3"}
  ]
}
```

#### O todo junto
```json
{
  "title": "new, new some project",
  "description": "new some project",
  "tasks": [
    {"task": "task"}
  ]
}
```

#### Actualizar la tarea de un proyecto

Realiza una petición PUT a la URL http://localhost:5000/api/v1/task/1 con el siguiente contenido

```json
{
    "done": true
}
```

O actualiza la tarea
```json
{
    "task": "new task 1"
}
```   

#### Eliminar la tarea de un proyecto

Realiza una petición DELETE a la URL http://localhost:5000/api/v1/task/1

#### Eliminar un proyecto

Realiza una petición DELETE a la URL http://localhost:5000/api/v1/project/1
