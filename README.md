## Abstract
Accurate classification of brain tumors from Magnetic Resonance Imaging (MRI) is critical for supporting timely diagnosis and treatment planning. This study presents a comparative evaluation of a custom Convolutional Neural Network (CNN) and a VGG16-based transfer learning model for multi-class brain tumor classification across four categories: glioma, meningioma, no tumor, and pituitary tumor. The baseline CNN, trained from scratch, achieved a classification accuracy of 76.44%. Applying transfer learning with a pretrained VGG16 architecture improved accuracy to 93.56%, an increase of 17.12 percentage points. The results confirm that pretrained convolutional representations offer substantial performance gains over models trained from scratch on limited medical imaging data.
Keywords: Brain Tumor Classification, MRI, Convolutional Neural Network, VGG16, Transfer Learning, Medical Imaging

## 1. Introduction
Brain tumors are abnormal cellular growths within the brain and surrounding tissue, and their early and accurate diagnosis significantly affects clinical outcomes. MRI remains the primary imaging modality for tumor detection, but manual interpretation is time-intensive and dependent on radiologist expertise. Deep learning offers an automated alternative capable of learning discriminative visual features directly from imaging data. This study evaluates two deep learning approaches for classifying brain MRI scans into four categories — glioma, meningioma, no tumor, and pituitary tumor — and compares a CNN trained from scratch against a VGG16 model adapted through transfer learning.
# 2. Dataset
The dataset comprises brain MRI images organized into four classes: glioma, meningioma, no tumor, and pituitary tumor. All images were resized to 128 × 128 pixels prior to model input to ensure consistency across the CNN and VGG16 pipelines.
# 3. Methodology
 ### 3.1 Baseline CNN 
 A convolutional neural network was designed and trained from scratch to establish a baseline. The architecture uses stacked convolutional and pooling layers to extract hierarchical spatial features, followed by fully connected layers for four-class classification. <br>
 ### 3.2 VGG16 Transfer Learning
 To improve feature extraction, a pretrained VGG16 network was adapted to the classification task. The convolutional base, pretrained on a large-scale natural image dataset, was fine-tuned and coupled with a new classification head suited to the four brain tumor categories. Transfer learning enables the model to leverage generalized low- and mid-level visual features, which is particularly beneficial when the target dataset is limited in size.


