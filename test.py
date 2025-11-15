from ultralytics.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld

if __name__ == "__main__":
    # 使用自己的YOLOv11.yamy文件搭建模型并加载预训练权重训练模型
    model = YOLO(r"best.pt") \
 \
            results = model.val(data=r'data.yaml',
                                imgsz=640, split='test')\


