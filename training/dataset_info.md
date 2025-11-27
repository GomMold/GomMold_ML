# GomMold – Mold Detection Dataset Information
## 1. Dataset Overview

This project uses a custom mold detection dataset created using Roboflow.
The dataset contains household images categorized into two classes:
- Mold
- No Mold
  
It is used for training a YOLOv8-based mold detection model for the GomMold project.

## 2. Dataset Source
The dataset is publicly accessible on Roboflow Universe:

🔗 **Roboflow Project Page**  
https://universe.roboflow.com/gommold-8opye/mold_detection_gommold-if0p0

## 3. Dataset Version
- **Version:** v4  
- **Generated on:** November 26, 2025  
- **Total images:** 1134  

This updated version includes improved annotations and additional “No Mold” images to reduce class imbalance.

## 4. Dataset Structure
After downloading the YOLOv8 version, the folder contains:
```
mold_detection_gommold-v4/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```
---

## 5. Classes
The dataset contains **2 classes**:

| Class ID | Class Name |
|----------|------------|
| 0        | Mold       |
| 1        | No Mold    |

## 7. Dataset Download Options

### **Option A — Roboflow Auto Download**
Visit the project page:
https://universe.roboflow.com/gommold-8opye/mold_detection_gommold-if0p0

Note : Replace "YOUR_API_KEY_HERE" with your own API key from the project link (Dataset -> Download Dataset -> Show Download Code)
```python
from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY_HERE")
project = rf.workspace("gommold-8opye").project("mold_detection_gommold-if0p0")
dataset = project.version(4).download("yolov8")
```
### **Option B — Download Manually from Roboflow** 

Visit the project page:
https://universe.roboflow.com/gommold-8opye/mold_detection_gommold-if0p0

Download → YOLOv8 format, then unzip in Google Colab.
```python
!unzip /content/mold_detection_gommold-v4.zip -d /content/
```

## 8. Notes

- All images were resized to **640×640** to match YOLOv8 training settings.  
- Annotation format follows **YOLO TXT** (normalized bounding boxes).  
- A significant portion of the dataset images were sourced from the following public dataset:  
  🔗 https://universe.roboflow.com/dissertationproject/mould-detection-aaron  
- Additional images were added and relabeled to improve class balance and detection accuracy.  
- If new images are gathered in the future, create a dataset update (v5, v6, …) in Roboflow.  
- This dataset is intended solely for **academic and research purposes** within the GomMold project.
