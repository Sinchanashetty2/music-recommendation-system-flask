# 🎵 EchoTune

> **Music Recommendation System using Flask and Machine Learning**

EchoTune is a web-based music recommendation system that suggests songs similar to a user's favorite track by analyzing audio features using the **Cosine Similarity** algorithm. The application provides a clean, responsive interface built with **Flask, HTML, CSS, JavaScript, and Machine Learning**.

---

# 📖 Overview

EchoTune helps users discover new music by comparing the characteristics of songs from a Spotify dataset. When a user searches for a song, the application finds the closest matching track and recommends similar songs based on their audio features.

This project was initially developed during my internship and later improved into a clean, portfolio-ready web application with a modern user interface.

---

# ✨ Features

* 🎵 Music recommendation using Cosine Similarity
* 🔍 Song search with autocomplete
* 📊 Machine Learning-based recommendation engine
* 🌙 Modern responsive dark-themed UI
* ⚡ Loading animation
* ❌ Error handling for unavailable songs
* 📱 Mobile-friendly design
* 🧩 Clean and modular project structure

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Pandas
* Scikit-learn
* Cosine Similarity

### Dataset

* Spotify Songs Dataset

---

# 📷 Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

---

## 🔍 Autocomplete Search

![Autocomplete](screenshots/autocomplete.png)

---

## 🎵 Recommendations

![Recommendations](screenshots/recommendations.png)

---

## ❌ Error Handling

![Error](screenshots/error.png)

---

# ⚙️ How It Works

1. User enters a song name.
2. The application searches the Spotify dataset.
3. The selected song is identified.
4. Audio features are compared using Cosine Similarity.
5. Similar songs are ranked.
6. Top recommendations are displayed to the user.

---

# 📂 Project Structure

```text
EchoTune/
│
├── app.py
├── recommendation.py
├── requirements.txt
├── README.md
├── Procfile
├── .gitignore
│
├── data/
│   └── clean_spotify.csv
│
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── layout.css
│   │   ├── components.css
│   │   ├── responsive.css
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       └── favicon.ico
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── home.png
│   ├── autocomplete.png
│   ├── recommendations.png
│   └── error.png
│
└── scripts/
    ├── clean_dataset.py
    ├── explore_dataset.py
    ├── test_dataset.py
    └── test_suggestions.py
```

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EchoTune.git
```

### 2. Navigate to the project directory

```bash
cd EchoTune
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open your browser

```text
http://127.0.0.1:5000
```

---

# 💡 Future Improvements

* Filter recommendations by genre
* Improve recommendation accuracy with additional audio features
* Use a larger music dataset
* Enhance recommendation visualization

---

# 👨‍💻 Author

**Sinchana Shetty S**

* GitHub: https://github.com/YOUR_USERNAME
* LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

* Flask Documentation
* Scikit-learn Documentation
* Pandas Documentation
* Spotify Songs Dataset
