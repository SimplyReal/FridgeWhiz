# FridgeWhiz AI - your secret sauce

![Demo]()

**Tired of staring at a full fridge with no meal ideas?** FridgeWhiz uses AI to generate recipes from your fridge photos in seconds! 

## ✨ Features
- 📸 **Smart Ingredient Detection** - Snap a pic, get ingredient list
- 🧠 **AI Recipe Generation** - Custom meals based on your food
- ⏱️ **Cooking Time & Calories** - Know what you're getting into
- 🌱 **Dietary Filters** - Vegan/GF/Quick meals with one click
- ♻️ **Reduce Food Waste** - Cook what you already have

## 🚀 Quick Start
```bash
# Clone & setup
git clone https://github.com/SimplyReal/FridgeWhiz.git
cd FridgeWhiz
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| **Frontend** |  |
| **Backend** | Python |
| **AI Model** | Qwen2-VL-72B (via Nebius AI) |
| **Computer Vision** | OpenCV/Pillow |


## 🌍 Demo
[!([https://img.shields.io/badge/Try_Live-Demo-brightgreen](https://youtu.be/QSJNQczB4VA))](https://your-streamlit-url.streamlit.app)

## 📂 Project Structure

FridgeWhiz/
├── app.py                # Flask backend
├── recipe_model.py       # AI integration
├── static/               # CSS/images
│   └── style.css
├── templates/            # HTML pages
│   ├── index.html
│   └── process.html
├── requirements.txt      # Dependencies
└── README.md

## 🤝 Contribute
1. Fork the repo
2. Create your branch (`git checkout -b feature/awesome-feature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/awesome-feature`)
5. Open a PR

## 📜 License
MIT © 2024 [Neha Kumari]
