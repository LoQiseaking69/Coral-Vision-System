
# Raspberry Pi 4 Coral Edge TPU Vision System

This project implements a computer vision system using a Raspberry Pi 4 and a Coral USB Accelerator. The system captures video frames, performs inference using the Coral Edge TPU, and stores the inference results in a SQLite database.

## Hardware Requirements
- Raspberry Pi 4
- Coral USB Accelerator
- Compatible Pi Camera

## Software Requirements
- Python 3
- TensorFlow Lite
- PyCoral API
- OpenCV
- SQLite

## Setup
### 1. Install Required Libraries
Run the `install_dependencies.sh` script to install all necessary Python packages and libraries:
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

### 2. Setup the Database
Run the `setup_database.py` to create the SQLite database:
```bash
python3 setup_database.py
```

### 3. Download the Model
Download the Coral-compatible TensorFlow Lite model:
```bash
curl -O https://github.com/google-coral/test_data/raw/master/mobilenet_v2_1.0_224_quant_edgetpu.tflite
```

## Running the System
Execute the `run_inference.py` script to start the video capture, inference, and data logging:
```bash
python3 run_inference.py
```

## Exiting the Program
Press 'q' during the live video stream to safely close the program and release all resources.

## Notes
Ensure the Coral USB Accelerator is connected and that the camera is properly configured with your Raspberry Pi.
