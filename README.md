# 🧠 GomMold – Model & Dataset Overview

This repository contains the machine learning components used to train and deploy the GomMold mold detection model.  
The system is built using **YOLOv8**, trained on a custom **Roboflow dataset**, and exported to **ONNX** for backend inference.

## Training Notebook

All training code, configuration settings, and evaluation outputs are documented in the training notebook:

🔗 **Training Notebook (`GomMold_ML.ipynb`)**  
https://github.com/GomMold/GomMold_ML/blob/3c9afa751b775e8e4ab3505b909dae3430e27480/training/GomMold_ML.ipynb

## Model Weights

The GomMold model was originally trained using YOLOv8 in PyTorch (.pt), but for deployment purposes it was exported to ONNX (.onnx) to ensure better compatibility and performance in our production environment. While the .pt file contains the full PyTorch training weights, it exceeds GitHub’s size limits and is not ideal for lightweight cloud deployment. The ONNX version, however, offers a more optimized, framework-agnostic format that runs efficiently on platforms like Railway, making it easier to load, faster to infer, and more portable across different environments.

You can download both versions below:

🔗 **Download Model (`new_best3.pt`):**  
https://github.com/GomMold/GomMold_ML/releases/download/v1.0/new_best3.pt

🔗 **Download Model (`best.onnx`):**  
https://firebasestorage.googleapis.com/v0/b/gommold-c6654.firebasestorage.app/o/models%2Fbest.onnx?alt=media&token=75667b68-4ed6-480a-895e-e9502ad5a95a

After downloading the file, place it in your backend's model directory before running inference.

## Dataset Information

The GomMold model is trained on a **custom mold detection dataset** created using Roboflow.  
The dataset contains **1,134 household images** across **two classes**:

| Class ID | Class Name |
|----------|------------|
| 0        | Mold       |
| 1        | No Mold    |

**🔗 Dataset Link** 

GomMold Roboflow Project Page:  
https://universe.roboflow.com/gommold-8opye/mold_detection_gommold-if0p0


### Dataset Version

- **Version:** v4  
- **Generated:** November 26, 2025  
- Includes improved annotations and additional **No Mold** samples for better class balance.

The YOLOv8 export contains the following structure:
```
mold_detection_gommold-v4/
├── train/
├── valid/
├── test/
└── data.yaml
```
Images were resized to **640×640**, following YOLOv8’s input requirements.  
Annotations follow the **YOLO TXT (normalized bounding box)** format.

A portion of the dataset images used for training were sourced from publicly available datasets on Roboflow, including https://universe.roboflow.com/dissertationproject/mould-detection-aaron and https://universe.roboflow.com/jisupark/wall-yqazk as well as from freely accessible images obtained through Google Search.

Additional images were manually collected and labeled for improved performance.

## Dataset Download Options

### **Option A — Roboflow Auto-Download (Python)**

```python
from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY_HERE")
project = rf.workspace("gommold-8opye").project("mold_detection_gommold-if0p0")
dataset = project.version(4).download("yolov8")
```

### **Option B — Manual Download** 

Visit the dataset page → Download → YOLOv8 format → Unzip into your workspace:

```python
unzip /content/mold_detection_gommold-v4.zip -d /content/
```
### Notes

- This dataset is intended for academic and research use within the GomMold project.
- Future dataset updates (v5, v6, …) can be created and managed through Roboflow.
- The model used in production is trained in Google Colab and later exported to ONNX for cloud deployment.

