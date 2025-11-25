# Virtual-Mouse-Using-Hand-Gestures

Control your mouse cursor **just with your fingers** using your webcam!\
This project uses **OpenCV** and **MediaPipe** to detect your hand in real-time and move the mouse accordingly.

---

## 📌 Features

- ✅ Smooth mouse movement based on index finger position
- ✅ Single-click, continuous click, and right-click gestures
- ✅ Works with any standard webcam
- ✅ Lightweight — no deep learning model required

---

## 🎥 Demo

[![🎥 Watch Demo Video](https://img.shields.io/badge/Watch-Demo-red?logo=google-drive)](https://drive.google.com/file/d/1urbdOetol4fycuQtDLp9LncTnLwSv9Yq/view?usp=sharing)


---

## 📂 Project Structure


```
VirtualMouse/
│
├── Demo-VM(1)              # Demo Video
├── HandTrackingModule.py  # Hand detection helper
├── README.md              # This file
├── requirements.txt       # Python package dependencies
├── VirtualMouse.py      # Main program
```

---

## 🛠 Requirements

- Python **3.x** (check with `python --version`)
- Webcam

1. Make sure your webcam is connected.
2. Run the script:

```bash
python final.py
```

3. Move your **index finger** to move the mouse.
4. Gestures:
   - ✌ **Index + middle fingers close together** → Single click
   - ☝ **Index + middle + ring fingers** → Continuous click
   - 👍 **Thumb + index only** → Right click

---

## ⚙️ How It Works

- **MediaPipe** detects hand landmarks.
- **OpenCV** processes webcam frames.
- Cursor position is mapped to your screen resolution using `numpy.interp`.
- **PyAutoGUI** moves the actual mouse.

---

## 📌 Notes

- Adjust `frameR` and `smoothening` in `final.py` for different responsiveness.
- Works best in **good lighting**.
- Disable mouse acceleration in OS for more precise control.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss your ideas.

---
