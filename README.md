# Pre-Entrega: Proyecto de Automation Testing con Selenium

Este proyecto contiene la suite de pruebas automatizadas para la plataforma **Swag Labs (SauceDemo)**. El objetivo es validar los flujos principales de autenticación, navegación del catálogo e interacción con el carrito de compras utilizando prácticas profesionales de QA Automation.

## 🚀 Tecnologías Utilizadas
* **Python** (Lenguaje principal)
* **Selenium WebDriver** (Automatización del navegador)
* **Pytest** (Framework de testing y estructura de pruebas)
* **Pytest-HTML** (Generación de reportes técnicos)

## 📁 Estructura del Proyecto
```text
pre-entrega-automation-testing/
│
├── reports/
│   └── reporte.html          # Reporte técnico e histórico de ejecuciones
│
├── tests/
│   ├── conftest.py          # Configuración de Fixtures y capturas en fallos
│   └── test_saucedemo.py    # Suite con los casos de prueba independientes
│
├── utils/
│   └── funciones.py         # Funciones auxiliares con esperas explícitas
│
├── pytest.ini               # Configuración interna de rutas de Python
└── README.md                # Documentación del proyecto
```

## 🧪 Casos de Prueba Automatizados
1. **`test_automatizacion_login`**: Realiza el inicio de sesión con credenciales válidas utilizando esperas explícitas, verificando la redirección correcta a `/inventory.html` y la presencia de los logos principales de la interfaz.
2. **`test_verificacion_catalogo`**: Valida que los productos se desplieguen correctamente en la pantalla principal, extrae los datos (nombre y precio) del primer ítem del catálogo e inspecciona componentes críticos como filtros y menú lateral.
3. **`test_interaccion_carrito`**: Añade un producto al carrito, valida el incremento dinámico del contador a "1", navega a la sección de compras y corrobora que el producto seleccionado coincida exactamente con el guardado en el carrito.

## 🛠️ Instalación de Dependencias
Para configurar el entorno y poder ejecutar este proyecto localmente, abre la terminal y ejecuta:

```bash
pip install selenium pytest pytest-html
```

## 📋 Ejecución de las Pruebas y Generación de Reportes
Para correr la suite de pruebas completa y generar de forma automática el reporte en formato HTML, ejecuta el siguiente comando en la raíz del proyecto:

```bash
python -m pytest -v -s --html=reports/reporte.html
```

*Nota: Si alguna prueba llegara a fallar, el archivo `tests/conftest.py` está configurado para capturar la pantalla del navegador en ese instante preciso y almacenarla dentro de la carpeta `reports/` como evidencia técnica.*