# 🍪 Dulce Bocatto – Sistema de Información I

[![Django](https://img.shields.io/badge/Django-5.2.7-092E20?logo=django)]()
[![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql)]()
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)]()
[![Status](https://img.shields.io/badge/Estado-Completado-brightgreen)]()

**Sistema web para la gestión completa de producción, ventas, inventario y reportes** de la microempresa *Dulce Bocatto*.  
Desarrollado como proyecto académico para **Sistemas de Información I – FICCT UAGRM**.

---

## ✨ Descripción General

El sistema permite administrar todos los procesos internos de la empresa:

- Registro de proveedores  
- Compras e inventario de insumos  
- Producción y control de stock  
- Ventas, pedidos y entregas  
- Facturación  
- Reportes PDF  
- Sistema de roles y bitácora  

Todo desarrollado con **Django + MySQL**, con arquitectura organizada y mantenible.

---

# 🚀 Características Principales

## 🔐 1. Seguridad y Gestión de Usuarios
- Registro / Login (`CU01`, `CU02`)
- Roles y permisos personalizados (`CU03`, `CU04`)
- Bitácora de operaciones (`CU05`)
- Modelo extendido de usuario (teléfono, email único)

---

## 🛒 2. Ventas y Gestión de Clientes
- Creación de pedidos con detalle (`CU16`)
- Confirmación, pago, entrega y cancelación de pedidos (`CU17`, `CU18`)
- Descuentos automáticos
- Facturas PDF (`CU19`)
- Seguimiento de entregas (`CU27`)

---

## 🧁 3. Producción e Inventario
- Recetas por producto (`CU31`)
- Validación de stock antes de producir (`CU32`)
- Descuento de insumos automático
- Reajuste de precios basado en costos

---

## 🏭 4. Compras y Proveedores
- Registro de compras (`CU14`)
- Kardex de inventario (`CU15`)
- Cálculo del **Precio Promedio Ponderado (PPP)**
- Nuevo campo: **tipo de proveedor**

---

## 📊 5. Reportes y Analíticas

Reportes con exportación a **PDF / CSV / HTML**:

- Ventas diarias (`CU23`)
- Entregas
- Proveedores
- Insumos y movimientos

---

# 🧱 Arquitectura del Sistema

Dulce Bocatto SI1
├── core/ # Configuración general del proyecto
├── accounts/ # Usuarios, roles, permisos, bitácora
├── pedidos/ # Pedidos, facturación, envíos
├── produccion/ # Recetas, producción, stock
├── compras/ # Proveedores, compras, kardex
├── reports/ # Reportes PDF
├── templates/ # Plantillas HTML
├── static/ # CSS, imágenes, JS
└── scripts/sql/ # Triggers y vistas SQL

---

# ⚙️ Tecnologías Utilizadas

| Capa / Funcionalidad | Tecnología |
|----------------------|-----------|
| Backend | Django 5.2.7 |
| Base de datos | MySQL |
| Frontend | HTML5, Bootstrap 5 |
| Reportes PDF | ReportLab |
| Variables .env | python-decouple |
| Seguridad | Django Auth + permisos |
| Filtros | django-filter |
| Entorno virtual | virtualenv |
| Control de versiones | Git + GitHub |

---

# 🧰 Instalación y Ejecución

# Clonar repositorio
git clone https://github.com/alecaballero17/DulceBocattoSI1.git
cd DulceBocattoSI1

# Crear entorno virtual
python -m venv env
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables (.env)
cp .env.example .env

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver
📌 Casos de Uso Implementados
Módulo	Casos de Uso	Descripción
Usuarios	CU01 – CU05	Autenticación, roles, permisos, bitácora
Pedidos	CU16 – CU19	Crear pedido, confirmar, facturar
Producción	CU31 – CU32	Receta, validación y producción
Compras	CU14 – CU15	Registrar compra, kardex
Reportes	CU23 – CU27	Ventas diarias, entregas, proveedores

🪄 Extras Técnicos
Scripts SQL de triggers y vistas en /scripts/sql/

Gestión de archivos estáticos y media

Configuración en .env seguro

Preparado para despliegue en Railway / Render / Docker

👨‍💻 Autor
Alejandro Caballero Pereira
Estudiante de Ingeniería Informática – FICCT UAGRM

📧 Email: alecaballeropereira@gmail.com
🔗 GitHub: https://github.com/alecaballero17

📄 Licencia
Proyecto con fines académicos y educativos.
