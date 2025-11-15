pip install ultralytics

yolo predict model=yolo11m.pt source='https://ultralytics.com/images/bus.jpg'


from ultralytics import YOLO

# Load a model
model = YOLO("yolo11m.pt")

# Train the model
model = YOLO(r"yolov11.yaml") \.load(r'yolo11m.pt')  # build from YAML and transfer weights
# Train the model
results = model.train(
    data=r"acne.yaml",  # acne数据集路径
    epochs=100,
    batch=4,
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("path/to/image.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model