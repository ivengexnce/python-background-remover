# 🖼️ Python Background Remover Collection

> Remove image backgrounds locally — **no API key, no internet, no login required.**
> Built for Python beginners. Works on Windows, Mac & Linux.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![rembg](https://img.shields.io/badge/Powered%20by-rembg-orange)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen)

---

## ✨ What This Does

This project gives you **4 different ways** to remove the background from any image using Python — pick the one that suits you best:

| Script | Interface | Best For |
|---|---|---|
| `bg_remove_normal.py` | Terminal (type path) | Quick single image |
| `bg_remover.py` | Terminal (type or browse) | CLI power users |
| `bg_removes_interactive.py` | GUI window | Click-and-go, single image |
| `bg_removes.py` | GUI window | Single **or** batch (multiple images) |

---

## 🚀 Getting Started (Beginner-Friendly)

### Step 1 — Make sure Python is installed

Download Python from [python.org](https://www.python.org/downloads/) if you don't have it.  
Check your version:
```bash
python --version
```

### Step 2 — Clone this repo
```bash
git clone https://github.com/ivengexnce/python-background-remover.git
cd python-background-remover
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

> ⏳ First run will download the AI model (~170MB). This only happens once.

---

## ▶️ How to Run

**Option 1 — Simple terminal tool (just type your image path):**
```bash
python bg_remove_normal.py
```

**Option 2 — Terminal with browse option:**
```bash
python bg_remover.py
```

**Option 3 — GUI window (click to select one image):**
```bash
python bg_removes_interactive.py
```

**Option 4 — GUI window (single or batch processing):**
```bash
python bg_removes.py
```

---

## 📦 Requirements
```
rembg
Pillow
```

> `tkinter` comes pre-installed with Python on most systems.

---

## 🗂️ Project Structure
```
python-background-remover/
│
├── bg_remove_normal.py          # Simple CLI tool
├── bg_remover.py                # CLI with browse support
├── bg_removes_interactive.py    # Basic GUI tool
├── bg_removes.py                # Full GUI with batch mode
├── requirements.txt
└── README.md
```

---

## 🖼️ Supported Image Formats

`.png` `.jpg` `.jpeg` `.webp`

---

## 💡 How It Works

This tool uses [rembg](https://github.com/danielgatis/rembg), which runs a deep learning model (U²-Net) locally on your machine to detect and remove image backgrounds — completely offline.

---

## 🛠️ Customization Ideas (Great for Beginners!)

- Add a drag-and-drop interface
- Add a before/after image preview
- Save outputs to a custom folder
- Add support for transparent background colors

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
If you're a beginner and want to contribute your first PR, this is a great project to start with. 🙌

---

## 📞 Contact — Meet Maru

[![LinkedIn](https://img.shields.io/badge/LinkedIn-meetmaru149-blue?logo=linkedin)](https://www.linkedin.com/in/meetmaru149)

[![GitHub](https://img.shields.io/badge/GitHub-ivengexnce-black?logo=github)](https://www.github.com/ivengexnce)

[![Instagram](https://img.shields.io/badge/Instagram-ivengexnce-E4405F?logo=instagram)](https://www.instagram.com/ivengexnce)

📧 meetmaru149@gmail.com

---

## ⭐ Support

If this project helped you, **give it a star** ⭐ — it helps others find it too!

---

> Made with ❤️ for Python beginners everywhere.
'''
