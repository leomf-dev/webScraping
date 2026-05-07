from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import random
#import pandas as pd
import os

from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
#opts.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp")

try:
    input_ruc = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "txtRuc"))
    )

    input_ruc.clear()
    input_ruc.send_keys("20291973851")

    btn_buscar = driver.find_element(By.ID, "btnAceptar")
    sleep(random.uniform(1, 3))
    btn_buscar.click()

    ### Volver al contenido principal
    ### driver.switch_to.default_content()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-group"))
    )

    # Nota: La SUNAT suele envolver los datos en un div con clase 'list-group' o una tabla
    tabla_elemento = driver.find_element(By.XPATH, "//div[@class='container']//div[@class='row']")
    codigo_tabla = tabla_elemento.get_attribute('outerHTML')

    carpeta = "descargas_sunat"
    #if not os.path.exists(carpeta):
    #    os.makedirs(carpeta)

    ruta_archivo = os.path.join(carpeta, "resultado_ruc.html")
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(codigo_tabla)

    print(f"¡Código fuente de la tabla guardado en: {ruta_archivo}!")

finally:
    driver.quit()