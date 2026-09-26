# Model Card — Damaged Box Detection Model (v1.0)

## 1. Overview

* **Goal:**
  This model aims to detect whether cardboard boxes are damaged or normal using computer vision techniques.

* **Task:**
  Object Detection

* **Classes:**

  * damaged_box
  * normal_box

* **Intended users:**
  Warehouse operators, quality assurance engineers, logistics companies, and developers working on automated inspection systems.

---

## 2. Intended Use and Scope

* **Intended environment:**
  Warehouse environments, storage facilities, logistics centers, and manufacturing areas.

* **Assumptions:**

  * Boxes are clearly visible in the image.
  * Images are captured under sufficient lighting conditions.
  * The camera is positioned at a reasonable distance from the boxes.
  * Most of the box surface is visible.

* **Out-of-scope uses:**

  * Detecting internal damage inside closed boxes
  * Detecting non-cardboard objects
  * Extremely low-quality or blurry images
  * Real-time industrial systems requiring advanced hardware optimization

---

## 3. Training Data

* **Data source:**
  The dataset was collected manually by taking photographs of cardboard boxes using a smartphone camera. Images were annotated using Roboflow.

* **Dataset size:**

  * Total images: 569
  * Training set: 372
  * Validation set: 114
  * Test set: 57

* **Class distribution:**

  * damaged_box: 256
  * normal_box: 288

* **Labeling guidelines:**
  Bounding boxes were drawn around the visible cardboard boxes.
  Boxes with visible dents, tears, crushes, or deformation were labeled as damaged_box.
  Boxes without visible defects were labeled as normal_box.

* **Augmentations:**
  Roboflow preprocessing and augmentation techniques were used, including resizing, flipping, rotation, and brightness adjustments to improve model generalization.

---

## 4. Evaluation

* **Test set description:**
  The test set contains unseen images separated from the training dataset to evaluate the model’s real-world performance.

* **Metrics:**

  * mAP@0.5: 0.98
  * mAP@0.5:0.95: 0.97
  * Precision: 0.98
  * Recall: 0.97

* **Qualitative analysis:**
  The model performs well on clearly visible boxes under normal lighting conditions.
  The model may struggle with partially occluded boxes, severe shadows, or very small damages.

* **Recommended confidence threshold(s):**
  A confidence threshold of 0.25 is recommended for balanced detection performance between false positives and false negatives.

---

## 5. Limitations and Failure Modes

* Known failure conditions:

  * Low lighting conditions
  * Motion blur
  * Extreme camera angles
  * Occluded boxes
  * Very small or subtle damages

* Typical false positives / false negatives:

  * Wrinkles or printed patterns on boxes may sometimes be detected as damage.
  * Minor damages may occasionally be classified as normal boxes.

---

## 6. Deployment Notes

* **Input requirements:**
  RGB images with approximately 640x640 resolution are recommended.

* **Output format:**
  The model outputs bounding boxes, predicted class labels, and confidence scores for detected boxes.

* **Compute:**
  The model was trained using YOLOv8n architecture and can run on standard consumer hardware.
  Inference time is approximately 40–50 ms per image on CPU.

---

## 7. Ethical / Safety / Privacy Considerations

* The dataset does not contain personal or sensitive information.
* Images only contain cardboard boxes and warehouse-like environments.
* No biometric or private data was used during training.
* The model is intended only for educational and quality-control purposes.

---

## 8. Versioning and Contact

* **Version:** v1.0
* **Date:** May 2026
* **Authors:** Batuhan Güzel
