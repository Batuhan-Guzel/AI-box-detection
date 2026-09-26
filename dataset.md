# Dataset Description: Industrial Cardboard Box Detection

## 1. Classes and Naming
The dataset consists of two mutually exclusive classes:
* `damaged_box`: Represents cardboard boxes that exhibit visible structural defects.
* `normal_box`: Represents intact cardboard boxes suitable for standard logistics and warehouse operations.

## 2. How to Interpret Labels (Semantics)
* **Bounding Box Rules:** Bounding boxes are drawn tightly around the visible boundaries of the cardboard boxes. If a box is partially occluded, the box only covers the visible extent.
* **`damaged_box` Semantics:** A box is classified and labeled as damaged if it presents clear, visible signs of physical impact or degradation. This includes dents, deep creases, tears, holes, severe crushes, or major shape deformations. 
* **`normal_box` Semantics:** A box is labeled as normal if its structural integrity is visually intact. Standard packaging tape, shipping labels, and minor, superficial scuffs do not disqualify a box from being classified as normal.

## 3. Known Issues and Ambiguous Cases
* **Subtle Damages:** Extremely minor damages, such as small surface scratches or slight corner wear, were occasionally ambiguous during the labeling process. In borderline cases, these might be labeled as `normal_box` to prevent over-sensitivity.
* **Printed Patterns and Tape:** Heavy use of glossy shipping tape, reflections under industrial lighting, or complex printed patterns on the cardboard occasionally mimic the visual appearance of tears or creases.
* **Internal Damage:** The labels strictly represent the external visual state of the boxes. A `normal_box` label does not guarantee that the internal contents are undamaged.