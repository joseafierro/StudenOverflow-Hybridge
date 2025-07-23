# StudenOverflow-Hybridge
Proyecto final StudentOverFlow Hybridge 
from pathlib import Path

readme_text = """# StudentOverflow

Portal web de **preguntas y respuestas entre estudiantes** (inspirado en StackOverflow), desarrollado en **Django 5**. Este repositorio cumple **todos los requisitos** del documento de “Catálogo de proyectos” (5 checkpoints). Además, se tomó como guía el repositorio público [`jesusvasquezjr3/StudentOverflow`](https://github.com/jesusvasquezjr3/StudentOverflow).

---

## 📌 Objetivos por Checkpoint

| CP | Entregable principal | Dónde guardarlo | Detalles |
|----|----------------------|-----------------|----------|
| **CP1** | PDF con prototipo de **todas** las vistas + repo público con estructura, README y `requirements.txt` | `documentation/prototypes/` y `Entregables/CP1/` | Home (guest/logeado), Login, Signup, Crear Pregunta, Detalle Pregunta, etc. |
| **CP2** | **ERD** y **diagramas de flujo** | `documentation/db/` y `documentation/flows/` + `Entregables/CP2/` | Archivos `.mmd` (Mermaid) + exportados PNG/SVG sin comprimir. |
| **CP3** | 4 screenshots (Home sin sesión, Home con sesión, Login, Signup) + **video corto** del flujo | `Entregables/CP3/` | Deben ser vistas funcionales reales. |
| **CP4** | Screenshots **registro, login y persistencia de sesión** | `Entregables/CP4/` | Muestra que el usuario sigue logeado al refrescar/navegar. |
| **CP5** | Screenshot del **Home con contenido dinámico** + video del flujo completo (preguntar, responder, comentar) | `Entregables/CP5/` | Usa datos reales desde la DB. |

Cada carpeta `Entregables/CP#/` incluye un `CHECKLIST.md` para que marques los requisitos.

---

## 🧱 Estructura del Repositorio

---

## 🚀 Quickstart (Local)

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r backend/requirements.txt

cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
