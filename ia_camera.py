from playsound import playsound
from ultralytics import YOLO
import threading
import time

# Função para tocar o som em uma thread separada
def tocar_som(caminho):
    playsound(caminho)

# Carregar o modelo YOLO
modelo = YOLO("yolov8n.pt")

# Predição em tempo real com stream
results = modelo.predict(source='0', show=True, stream=True)

# Flag para verificar se o som já foi tocado
som_tocado = False

# Processar as detecções em tempo real
for result in results:
    pessoa_detectada = False
    for r in result.boxes.data.tolist():
        # Classe da detecção
        cls = int(r[5])
        # Verificar se a classe é "person" (0) ou "cell phone" (67)
        if cls == 0:
            thread = threading.Thread(target=tocar_som, args=('som_alarme/beep-warning-6387.mp3',))
            thread.start()
            time.sleep(0.10)
            print("\033[91m ===========> Pessoa detectada! <=========== \033[0m")
        elif cls == 67:
            print("\033[92m ===========> Celular detectado! <=========== \033[0m")
    
   
