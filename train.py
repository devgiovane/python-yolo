import os
from ultralytics import YOLO

model_n = YOLO('yolov8n.pt')
model_n.train(
    data=os.path.abspath('./dataset/data.yaml'),
    epochs=150,
    cache='ram',
    batch=-1,
    imgsz=640,
    degrees=+180
)
model_n.export(format='ONNX')

model_s = YOLO('yolov8s.pt')
model_s.train(
    data=os.path.abspath('./dataset2/data.yaml'),
    epochs=120,
    cache='ram',
    batch=-1,
    imgsz=640,
    degrees=-180
)
model_s.export(format='ONNX')


model_b = YOLO('./runs/detect/train/weights/bets.pt')
model_b.train(
    data=os.path.abspath('./dataset2/data.yaml'),
    epochs=120,
    cache='ram',
    batch=-1,
    imgsz=640,
    degrees=-180
)
model_b.export(format='ONNX')
