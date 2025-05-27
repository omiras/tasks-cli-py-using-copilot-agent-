# tasks-cli-py

Gestor de tareas simple por línea de comandos en Python.
Project idea taken from this site: https://roadmap.sh/projects/task-tracker

## Características
- Añadir tareas con descripción
- Listar tareas (todas, o filtradas por estado: `todo`, `in-progress`, `done`)
- Marcar tareas como completadas o en progreso
- Actualizar la descripción de una tarea
- Eliminar tareas
- Cada tarea tiene:
  - `id`: identificador único
  - `description`: descripción
  - `status`: `todo`, `in-progress`, `done`
  - `createdAt`: fecha de creación
  - `updatedAt`: fecha de última actualización

## Uso

### Añadir tarea
```
python main.py add "Descripción de la tarea"
```

### Listar tareas
```
python main.py list           # Todas
python main.py list todo      # Solo pendientes
python main.py list done      # Solo completadas
python main.py list in-progress # Solo en progreso
```

### Marcar tarea como completada
```
python main.py done <id>
python main.py mark-done <id>
```

### Marcar tarea como en progreso
```
python main.py mark-in-progress <id>
```

### Actualizar descripción de una tarea
```
python main.py update <id> "Nueva descripción"
```

### Eliminar tarea
```
python main.py delete <id>
```

## Convertir a ejecutable

1. Instala pyinstaller:
   ```
   pip install pyinstaller
   ```
2. Genera el ejecutable:
   ```
   pyinstaller --onefile main.py
   ```
   El ejecutable estará en la carpeta `dist`.

---

Desarrollado por Óscar Miras.
