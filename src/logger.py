import logging
import os
from datetime import datetime

# Obtener el directorio raíz del proyecto (subiendo un nivel desde src)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
logs_path = os.path.join(ROOT_DIR, 'logs')

# Asegurar que la carpeta logs existe
os.makedirs(logs_path, exist_ok=True)

# Definir el archivo de logs
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configurar logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    logging.info('Logging has started')
