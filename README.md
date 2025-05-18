# Children's Drawings Recognition Using YOLOv8

This is a deep learning university project focused on object detection in children’s drawings, using the YOLOv8 model.  
It was completed as part of the Deep Learning course during the third year of my Computer Science and Software Engineering studies.

The goal of the project was to build a model capable of recognizing various objects commonly found in children's drawings.  
Implementation was done in Python, using the YOLOv8 large variant due to the complexity and variation in object appearances.

---

Unannotated Mock Image

![image](https://i.imgur.com/9mHSYXk.jpeg)

Annotated Mock Image

![image](https://i.imgur.com/8UECwUf.jpeg)

CVAT Annotation Tool

![image](https://i.imgur.com/HRcxFf4.jpeg)

Validation Set Batch - Manually Annotated

![image](https://i.imgur.com/sgRW1ib.jpeg)

Validation Set Batch - Predictions

![image](https://i.imgur.com/QRUHuKU.jpeg)

**Note**: In the last image, the decimal values next to class names represent the model's confidence score.

### Testing the model on your own
If you wish to run inference on your own images or drawings with this model, download the best parameters from my [Google Drive link](https://drive.google.com/file/d/1NiUkRWOgjV4qxKYdS0yJPau25mCbi-ZL/view?usp=drive_link).

## Project Overview

### Dataset and Annotations
All images were manually annotated using [CVAT](https://www.cvat.ai/).  
Total number of annotations: **18,165**
Image sources:
 - [Indiana State University](https://childart.indstate.edu/choosefirstcriteria.php) - *defunct*
 - [Illinois State University](https://digital.library.illinoisstate.edu/digital/collection/icca/search/)
 - Local elementary schools:
   - OŠ Radoje Domanović, Kragujevac
   - OŠ Jovan Popović, Kragujevac
  
### Classes
Below is a list of classes and the number of their appearances in the entire dataset, respectively:
 - sports_ball: 252
 - fish: 190
 - window: 3022
 - vehicle: 213
 - pet: 490
 - star: 414
 - bird: 895
 - flower: 1901
 - person: 3726
 - house: 1281
 - cloud: 1931
 - butterfly: 108
 - door: 1035
 - sun: 905
 - tree: 1424
 - heart: 378

### Dataset Split
**Total images**: 2,041
 - **Training set**: 85% (1,745 images)
 - **Validation set**: 15% (296 images)

### Evaluation Results
The final model's performance can be found in the `val3/` folder.  
It includes:
 - Confusion matrices
 - F1-confidence curves
 - Precision-confidence curves
 - Recall-confidence curves
 - Example images with predicted labels

### Sample Images
Some sample images collected locally are provided within `sampleimages/`.
