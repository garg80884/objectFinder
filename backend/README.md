# Generic Object Locator AI Agent

This project uses Grounding DINO to detect arbitrary objects by name in your webcam feed.

## Setup

1. Clone or extract this repository.
2. Ensure you have weights/downloaded:
   - `weights/groundingdino_swint_ogc.pth` in a folder named `weights/`

3. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   mim install mmdet
   ```

5. Run:
   ```bash
   python universal_locator.py
   ```

6. Test:
   ```bash
   curl "http://localhost:5000/locate?object=your_item"
   ```

## Notes

- Adjust `box_threshold` in the code for sensitivity.
- Ensure no other application is using the webcam.
