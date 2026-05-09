**Proyecto: Pruebas Selenium (webScraping)**

Breve: Conjunto mínimo de pruebas automatizadas con Selenium para Chrome. Genera reportes HTML usando HtmlTestRunner.

**Requisitos**:
- **Python:** 3.8+ recomendado.
- **Dependencias:** Ver [requirements.txt](requirements.txt).

**Entorno**:
- **Virtualenv:** Hay un entorno en EnvironmentQA (activar con los scripts en EnvironmentQA/Scripts/).

**Instalación rápida (Windows PowerShell)**
```
.\EnvironmentQA\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Ejecutar pruebas**
- Ejecutar todo el suite (desde la raíz del proyecto):
```
python -m unittest discover -s src -p "test*.py"
```
- Ejecutar el test principal directamente:
```
python src/Test/test.py
```

**Archivo principal del test**
- [src/Test/test.py](src/Test/test.py) — contiene la clase `GoogleTest` con `setUp()`, `test_google_homepage()` y `tearDown()`.

**Reporte**
- HtmlTestRunner genera el reporte en: [src/reporthtmlrunner](src/reporthtmlrunner).

**Notas y consejos**
- `webdriver-manager` descarga ChromeDriver automáticamente; asegúrate de tener Google Chrome instalado y actualizado.
- Si ves errores de compatibilidad, actualiza Chrome o fuerza una versión de ChromeDriver compatible.
- Si necesitas ejecutar en CI, exporta variables de entorno o adapta las Options de Chrome para modo headless.

Si quieres, puedo ejecutar las pruebas ahora y subir el reporte.
