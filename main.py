
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow, cv2
import requests
import base64
import numpy
import tensorflow as tf
import time


# corre modelo tflite
def run_tflite_model(interpreter, image):
    # converter imagem grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # faz resize para 96x96
    width = 96
    height = 96
    dim = (width, height)

    resizedImage = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)
    resizedImage = numpy.expand_dims(resizedImage, axis=2)

    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]

    # Verifica o input, e faz rescale para uint8
    if input_details['dtype'] == numpy.uint8:
        input_scale, input_zero_point = input_details["quantization"]
        test_image = resizedImage / input_scale + input_zero_point

    test_image = numpy.expand_dims(test_image, axis=0).astype(input_details["dtype"])
    interpreter.set_tensor(input_details["index"], test_image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details["index"])[0]

    return output.argmax() == 1


def readPlate(file_bytes):
    # print(file_bytes[0:100]) # isto é só para mostrar o conteudo

    # %% Converte para base64
    file_in_base64 = base64.b64encode(file_bytes)

    # print(file_in_base64[0:100]) # isto é só para mostrar o conteudo

    # %% Cabecalho do pedido http
    header = {
        'accept': 'application/json',
        'X-API-Key': 'KrOEIZr3N28Ih62Frj7ee9rYBnaqI6Nj7KjMnQEY'
    }

    # %% efectuar pedido
    response = requests.post('https://api.plate.vision/dev/recognize/base64?profile=eu_ir',
                             headers=header, data=file_in_base64)

    
    message_in_json = response.json()
    
    print(message_in_json)

    
    print(message_in_json['plates'][0]['results'][0]['rawText'])
    time.sleep(1)
    return


# define a video capture object
vid = cv2.VideoCapture(0)

interpreter = tf.lite.Interpreter(model_path=str('model.tflite'))
interpreter.allocate_tensors()

while (True):

    # captura o feed de video
    ret, frame = vid.read()

    # mostra o feed
    cv2.imshow('frame', frame)

    # envia a imagem guardada para a função de leitura da matricula

    if run_tflite_model(interpreter, frame) == 1:
        readPlate(cv2.imencode('.jpg', frame)[1])

    # define que a tecla 'q' termina o programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
