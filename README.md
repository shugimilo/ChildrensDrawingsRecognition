# Children's Drawings Recognition Using YOLOv8

This is a deep learning university project focused on object detection in children’s drawings, using the YOLOv8 model.  
It was completed as part of the Deep Learning course during the third year of my Computer Science and Software Engineering studies.

The goal of the project was to build a model capable of recognizing various objects commonly found in children's drawings.  
Implementation was done in Python, using the YOLOv8 large variant due to the complexity and variation in object appearances.

### Dataset and Annotations
All images were manually annotated using [CVAT](https://www.cvat.ai/).  
Total number of annotations: **18,165**
Image sources:
 - [Indiana State University](https://childart.indstate.edu/choosefirstcriteria.php); - *defunct*
 - [Illinois State University](https://digital.library.illinoisstate.edu/digital/collection/icca/search/);
 - Local elementary schools:
   - OŠ Radoje Domanović, Kragujevac
   - OŠ Jovan Popović, Kragujevac

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

## Sample Images
Some sample images collected locally are provided within 'sampleimages/'.
