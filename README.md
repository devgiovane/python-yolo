<img src="./python.png" width="80" height="80" alt="logo" />

# Python YOLO V8

> My Study for data science and artificial intelligence

### Concepts

- Artificial Intelligence (AI)
- Python (3.12)
- YOLO V8
- Stratification Dataset
- Sklearn

### CLI Commands

**Train:**
```bash
yolo mode=train task=detect model=yolov8n.pt data=$(pwd)/dataset/data.yaml epochs=150 cache=ram batch=-1 imgsz=640 degrees=+180
```