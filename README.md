
1. Use-case description
a. Industrial motivation and target scenario
This project addresses a critical need in modern industrial quality control: automating the visual inspection of cardboard packaging. Using computer vision techniques, this system aims to detect whether cardboard boxes are damaged or in normal condition. The target scenario involves automated inspection systems deployed within warehouse environments, logistics centers, storage facilities, and manufacturing areas. The intended end-users are warehouse operators, quality assurance engineers, and logistics managers seeking to minimize the dispatch of defective packaging.

b. What the model detects (classes) and what it explicitly does not cover
The object detection model is trained to identify and localize two specific, mutually exclusive classes:
damaged_box
normal_box
To maintain operational reliability, the model’s scope is strictly defined. It explicitly does not cover: detecting internal damage or compromised goods inside closed boxes, detecting non-cardboard objects (e.g., plastic crates, wooden pallets), operating effectively on extremely low-quality or blurry images, and functioning in real-time embedded systems that require advanced edge-hardware optimization.

c. Assumptions (camera type, distance, background, lighting)
The operational assumptions for this model are that the boxes are clearly visible in the image, captured under sufficient lighting conditions, and that the camera is positioned at a reasonable distance where most of the box surface is visible.

2. Dataset description
a. How images were collected (where, by whom, devices used)
The dataset was collected manually by taking photographs of cardboard boxes in warehouse-like environments using a smartphone camera.

b. Dataset size: images per split and per class
The dataset comprises a total of 569 images. To ensure rigorous training and unbiased evaluation, the data was split as follows:
Training set: 372 images
Validation set: 114 images
Test set: 57 images
The overall class distribution is well-balanced, containing 288 instances of normal_box and 256 instances of damaged_box.

c. Labeling policy ("annotation guidelines") and edge cases
Images were annotated utilizing Roboflow. Bounding boxes were drawn tightly around the visible boundaries of the cardboard boxes. Boxes exhibiting visible structural defects (dents, tears, crushes) were labeled as damaged_box. Boxes without visible defects were labeled as normal_box. Extremely minor damages were occasionally ambiguous; to prevent over-sensitivity, borderline cases were generally labeled as normal_box.

d. Augmentation strategy, including what was done in Roboflow
To enhance model generalization, Roboflow preprocessing and augmentation techniques were applied exclusively to the training set. Strategies utilized include image resizing (to 640x640), flipping, rotation, and brightness adjustments to simulate fluctuations in factory lighting and camera angles.

e. Data quality checks
The dataset underwent manual verification to ensure annotations accurately reflected the visual state of the boxes. Verification also confirmed that the dataset contains no personal, biometric, or sensitive information.

3. Model(s) and training setup

a. Architecture/training pipeline
To determine the optimal architecture for this specific industrial task, two different models were trained and compared:
YOLOv8n (Nano): A highly lightweight architecture prioritized for speed.
YOLOv8s (Small): A higher-capacity architecture with more parameters to evaluate if a deeper network yields better accuracy on this dataset.
Both models were trained locally utilizing the Ultralytics Python pipeline.

b. Hyperparameters
Both models were trained with identical configurations to ensure a fair comparison:
Input Resolution (imgsz): 640x640 pixels (RGB).
Epochs: 100 (with Early Stopping enabled via patience=50).
Batch Size: 16.

c. Compute used
The models were trained locally on an Apple M4 Pro / Intel Core i7 hardware setup.

4. Evaluation results (Primary Model: YOLOv8n)
Note: Based on the comparative analysis (detailed in Section 6), the YOLOv8n (Nano) model was selected as the final production artifact. The results below reflect the performance of this chosen model.

a. Standard object detection metrics on the test set
The model's evaluation on the unseen test set yielded exceptional performance metrics, demonstrating robust learning convergence:
mAP@0.5: 0.985
mAP@0.5:0.95: 0.970
Precision: 0.980
Recall: 0.970



b. Per-class results and error analysis with examples
Qualitative analysis indicates that the model performs exceptionally well on clearly visible boxes under normal lighting conditions. The Confusion Matrix confirms that the model successfully identified 96% of the damaged boxes and 97% of the normal boxes. The error margin was minimal: only 1 damaged box was misclassified as normal, and 2 normal boxes were incorrectly flagged as damaged.



c. Common failure modes and suggested mitigations
Typical false positives occur when wrinkles or printed patterns/labels on boxes are incorrectly detected as damage. False negatives occur when minor damages are too subtle and are classified as normal boxes. Mitigations include avoiding extreme camera angles, motion blur, and ensuring consistent lighting to minimize shadowing.
5. Deployment notes

a. Brief description of the developed app
A lightweight web application was developed using Streamlit to showcase the model. The application allows users to upload an image of a box, runs inference using the trained weights, and visually outputs the bounding boxes alongside structured JSON data containing the class labels and confidence scores.

b. Inference speed/model size
Due to the lightweight YOLOv8n architecture, the inference time is highly efficient, averaging approximately 40 to 50 ms per image on a standard CPU, with a total model size of just 6.2 MB.

c. Recommended confidence thresholds and any post-processing
While automated metrics indicate a mathematical F1 peak at 0.547, a visual engineering analysis of the F1-Confidence curve reveals a sustained plateau extending up to 0.85. By setting the threshold higher (0.75 - 0.80) near the right edge of this plateau, the system maximizes precision (drastically reducing false positive defect alerts on the factory floor). Crucially, visual analysis of the Recall-Confidence curve confirms that at this recommended threshold, the expected Recall remains exceptionally high at approximately 0.95 - 0.96. This means the system will still successfully intercept 95-96% of all actual damaged boxes while eliminating background noise, ensuring a highly robust, reliable, and production-ready automated inspection deployment.


Evaluation results (Secondary Model: YOLOv8s - Small)
a. Standard object detection metrics on the test set The YOLOv8s model was trained for 50 epochs, requiring 3.505 hours of computation. Evaluation on the validation and test splits yielded the following general metrics:
mAP@0.5: 0.972
mAP@0.5:0.95: 0.950
Precision: 0.972
Recall: 0.965


The training progression curves indicate a steady decrease in box, classification, and distribution focal loss over the 50 epochs, though convergence was slower compared to the Nano model.
b. Per-class results and error analysis with examples A detailed per-class breakdown reveals the following performance:
damaged_box: Precision of 0.977, Recall of 0.962, and a $mAP@0.5$ of 0.988.
normal_box: Precision of 0.967, Recall of 0.968, and a $mAP@0.5$ of 0.956.
According to the generated raw confusion matrix for YOLOv8s, out of the validation set:
51 damaged boxes were correctly identified as damaged, while 2 damaged boxes were incorrectly classified as normal boxes (false negatives).
60 normal boxes were correctly identified as normal, while 1 normal box was incorrectly predicted as damaged (false positive), and 1 normal box was lost to the background class.
Additionally, 2 background instances were falsely detected as normal boxes.

c. Common failure modes and suggested mitigations The YOLOv8s model struggled slightly more with localized, high-contrast print designs on undamaged boxes, leading to false defect alarms (normal boxes flagged as damaged). Increasing the dataset size or incorporating heavier grayscale/contrast augmentations could mitigate these localized texture misclassifications.

6. Model Comparison and Selection
To rigorously determine the most optimal architecture for industrial deployment, a comparative analysis was conducted between the lightweight model (YOLOv8n - Nano) and a larger, more complex architecture (YOLOv8s - Small). Both models were trained strictly on the exact same dataset splits to ensure a scientifically valid baseline.
Table 1: Architectural Comparison (YOLOv8n vs. YOLOv8s)
Metric / Attribute
YOLOv8n (Nano) - Selected
YOLOv8s (Small) - Evaluated
Parameters
~3.2 Million
11.1 Million
Model Size
6.2 MB
22.5 MB
Inference Speed (CPU)
~40 - 50 ms / image
~185.8 ms / image
mAP@0.5 (Overall)
0.985
0.972
mAP@0.5:0.95 (Overall)
0.970
0.941
Precision (Overall)
0.980
0.976
Recall (Overall)
0.970
0.965

Analysis and Engineering Conclusion
Contrary to the general assumption that larger models naturally yield better detection accuracy, the comparative data reveals that the YOLOv8n architecture outperforms the YOLOv8s architecture across critical validation metrics for this specific use-case.
The slight degradation in the YOLOv8s model’s accuracy can be attributed to the dataset's limited size (569 images). The significantly higher parameter count (~11.1M) in the YOLOv8s model increases its susceptibility to overfitting on smaller datasets compared to the Nano model, which was able to generalize much more effectively.
Furthermore, from an industrial deployment perspective, the YOLOv8s model is nearly four times larger in memory footprint and incurs a massive latency penalty, running at ~185 ms per image compared to the Nano’s ~45 ms. In a real-world warehouse scenario involving fast-moving conveyor belts, processing at 185 ms limits the system to approximately 5 frames per second (FPS), potentially introducing severe operational bottlenecks.
Final Decision: The YOLOv8n (Nano) is unequivocally selected as the final production artifact. It provides superior detection accuracy, avoids overfitting, requires drastically less computational overhead, and delivers the necessary real-time processing speeds required for automated logistics inspection.
