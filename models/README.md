# Model Weights – GomMold Mold Detection

The trained YOLOv8 model used in this project is not stored directly inside the repository because the `.pt` file exceeds GitHub’s file size limit.

Instead, the model is provided through an external download link.  
This ensures the file does not become corrupted and remains accessible for deployment.

## Download the Trained Model

The GomMold model was originally trained using YOLOv8 in PyTorch (.pt), but for deployment purposes it was exported to ONNX (.onnx) to ensure better compatibility and performance in our production environment. While the .pt file contains the full PyTorch training weights, it exceeds GitHub’s size limits and is not ideal for lightweight cloud deployment. The ONNX version, however, offers a more optimized, framework-agnostic format that runs efficiently on platforms like Railway, making it easier to load, faster to infer, and more portable across different environments.

You can download both versions below:

PyTorch Model (.pt) — Training Weights

🔗 [new_best3.pt](https://github.com/GomMold/GomMold_ML/releases/download/v1.0/new_best3.pt)

ONNX Model (.onnx) — Deployment Model

🔗 [best.onnx](https://firebasestorage.googleapis.com/v0/b/gommold-c6654.firebasestorage.app/o/models%2Fbest.onnx?alt=media&token=75667b68-4ed6-480a-895e-e9502ad5a95a)

After downloading, place the selected model file into your backend’s model directory before running inference.


