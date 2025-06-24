# 📸 Object Finder AI

This is an AI-powered web application that helps users detect and locate real-world objects using their webcam.

## 🔍 Features
- Live webcam preview
- Object name input
- Smart detection using GroundingDINO
- Bounding box or circle around found objects
- Works entirely from browser + backend

## 🛠 Tech Stack
- **Frontend**: HTML + JavaScript + CSS
- **Backend**: Python (Flask), OpenCV, Torch
- **Model**: GroundingDINO with `.pth` weights
- **Deployment**: Hostinger (frontend), Render (backend)

## 🚀 How to Run Locally
```bash
git clone https://github.com/garg80884/object-finder.git
cd object-finder/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python universal_locator.py
