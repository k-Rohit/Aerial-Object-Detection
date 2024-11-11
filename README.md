# Real-Time Object Detection and Classification in Surveillance Imagery

## Project Overview

This project aims to develop an AI-powered surveillance system designed to accurately detect and classify aerial and naval objects in real-time. The project leverages the YOLOv8-seg deep learning model, optimized for low-latency and high-accuracy object detection in military and defense contexts. The system is intended to address challenges such as latency, lower accuracy, and limited capability to handle multiple targets simultaneously, ultimately improving mission success and reducing false positives and negatives.

## Problem Statement

The current surveillance systems in military and defense contexts face significant challenges in detecting and classifying aerial and naval objects over long distances in dynamic environments. These challenges include high latency, low accuracy, and limited multi-target handling capabilities. This project aims to enhance real-time processing, improve detection accuracy, and reduce reliance on human operators.

- And many others...

## Technology Stack

- **Data Storage**: Local or cloud storage solutions (e.g., Google Drive)
- **Data Processing**: OpenCV, PyGoogle, BeautifulSoup
- **Annotation**: Labelme, Labelme2Yolo
- **Machine Learning**: YOLOv8
- **Integration and Deployment**: Flask, RESTful APIs

## System Architecture

The system is designed with a modular architecture to separate data ingestion, model processing, and output generation. It can easily integrate with existing military surveillance systems.

## Development and Implementation

### Data Collection and Annotation

A dataset of 600,000 images was created, covering various aerial and naval objects under different environmental conditions. Annotations were made using Labelme and converted to YOLO-compatible format.

### Model Training

The YOLOv8-seg model was trained on the annotated dataset, focusing on achieving high mean Average Precision (mAP) and low latency.

### System Integration

The model was integrated into a Flask-based web application to provide a seamless interface for military operators.

### Deployment

The system was deployed on a high-performance server with GPU acceleration, ensuring real-time processing with minimal latency.

## Testing and Debugging

### Unit Testing

Each system module underwent rigorous unit testing to ensure functionality in isolation.

### Image Selection Criteria

A thorough review process identified the most optimal images for training, ensuring data balance and accuracy.

### Performance Testing

The system was tested for mAP, accuracy, and latency, fine-tuned to meet real-time detection requirements in military scenarios.

### Debugging

Issues such as false positives/negatives were addressed through model refinement and code optimization.

## Workflow

1. constants
2. entities
3. components
4. pipelines
5. app.py


## Save pass
------


## Setting up Docker

docker build -t aodproject.azurecr.io/aod:latest .

docker login aodproject.azurecr.io

docker push aodproject.azurecr.io/aod:latest


## Conclusion

The project successfully developed a real-time object detection and classification system for surveillance imagery, optimized for military use. The system addresses key challenges in current surveillance technologies, offering enhanced accuracy, reduced latency, and the ability to handle multiple targets in complex environments.


