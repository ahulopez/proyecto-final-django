# Playground Final - Blog (Django)

Proyecto final estilo blog con:
- Herencia de templates + Navbar (Bootstrap blanco/beige)
- App principal (`mainapp`): Home, About, Dashboard protegido (@login_required)
- App `pages`: **Post** (modelo principal con CKEditor, imagen, fecha, code, autor) y **Libro** (segundo modelo). Ambos con **CRUD** y **buscador**.
- App `accounts`: Signup, Login, Logout, Profile (ver/editar), cambio de contraseña. Perfil con avatar/bio/fecha de nacimiento.
- Admin con modelos registrados.
- Mensajes de éxito con `django.contrib.messages`.

## Rutas principales
- `/` Home
- `/about/` About me
- `/dashboard/` (requiere login)
- `/pages/posts/` (listado + buscar) | crear/editar/eliminar con login
- `/pages/libros/` (listado + buscar) | crear/editar/eliminar con login
- `/accounts/signup/` | `/accounts/login/` | `/accounts/logout/`
- `/accounts/profile/` | `/accounts/profile/edit/` | `/accounts/password/`

## Requisitos (checklist)
- [x] Herencia de HTML (base.html + templates específicos)
- [x] Modelo principal con 2 CharField, texto enriquecido (CKEditor), imagen, fecha y code
- [x] CRUD completo para Post (CBV + LoginRequiredMixin)
- [x] CRUD completo para Libro (FBV + decoradores @login_required)
- [x] Buscador en listados, con mensaje de “No hay …”
- [x] Admin con modelos registrados
- [x] App de cuentas con login, logout, signup, perfil (ver/editar), cambio de pass
- [x] Mínimo 2 CBV y 1 mixin (LoginRequiredMixin) + 1 decorador (@login_required)
- [x] `.gitignore` con pycache, db.sqlite3, media
- [x] `requirements.txt` actualizado
- [x] About visible en navbar
- [x] 3 apps en total

## Cómo correr
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
# source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser  # opcional para admin
python manage.py runserver
```

> Nota: No subir `db.sqlite3` ni `media/` al repo (ya están en `.gitignore`). Recomendado usar imágenes livianas en `/media`.
