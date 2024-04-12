
import cv2
from pycoral.adapters import classify
from pycoral.adapters import common
from pycoral.utils.edgetpu import make_interpreter
import sqlite3
import datetime

camera = cv2.VideoCapture(0)
interpreter = make_interpreter('mobilenet_v2_1.0_224_quant_edgetpu.tflite')
interpreter.allocate_tensors()

def store_inference(inference):
    connection = sqlite3.connect('inferences.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO results (datetime, inference) VALUES (?, ?)', (datetime.datetime.now(), inference))
    connection.commit()
    connection.close()

while True:
    ret, frame = camera.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (224, 224))
    input_tensor = common.set_input(interpreter, resized_frame)
    interpreter.invoke()
    results = classify.get_classes(interpreter, top_k=1)

    for result in results:
        store_inference(f"Label {result.id}, Score: {result.score}")

    cv2.imshow('Live Inference', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
