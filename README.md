# Disk speed calculation

Folder assets contains photo and data folders. Data folder contains .txt files with YOLO bboxes that match the photos in the photo folder.
Program calculates disk speed between two adjacent photos after parsing data and photo from folders.

Project start:
1. Clone project from GitHub
2. Choose Python 3.9 as interpreter
3. run commands sequentially in terminal:
```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install --upgrade setuptools wheel pip
pip3 install -r requirements.txt

python3 -m src.main -p <path to assets folder>
```
4. Use **q** button to change photo. Speed calculation result will be at the top left corner of each photo