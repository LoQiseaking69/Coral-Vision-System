
#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install numpy opencv-python tensorflow
pip3 install --extra-index-url https://google-coral.github.io/py-repo/ pycoral
