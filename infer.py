import argparse
import json
import cv2
from ultralytics import YOLO

def main():
   
    parser = argparse.ArgumentParser(description="Run YOLOv8 inference on a single image.")
    parser.add_argument("--model", type=str, required=True, help="Path to the model weights file (.pt)")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image file")
    args = parser.parse_args()

    
    try:
        model = YOLO(args.model)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    
    results = model.predict(source=args.image, conf=0.25, verbose=False)
    result = results[0]

    
    detections = []
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        detections.append({
            "class_name": model.names[int(box.cls)],
            "confidence": round(float(box.conf), 4),
            "bbox": {
                "x1": round(x1, 2), 
                "y1": round(y1, 2), 
                "x2": round(x2, 2), 
                "y2": round(y2, 2)
            }
        })

    
    output_image_name = "output_detection.jpg"
    res_plotted = result.plot()
    cv2.imwrite(output_image_name, res_plotted)

    
    print("\n--- Detection Results (JSON) ---")
    print(json.dumps(detections, indent=2))
    print("--------------------------------")
    print(f"\nVisualized output saved locally as: {output_image_name}")

if __name__ == "__main__":
    main()