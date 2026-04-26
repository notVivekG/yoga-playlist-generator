# 🧘‍♀️ AI Yoga Playlist Generator

An intelligent, AI-powered web application that generates personalized yoga video recommendations based on your physical or emotional concerns (e.g., stress, anxiety, neck tension). 

The app maps natural language input to curated yoga categories and dynamically serves the best matching YouTube yoga routines for your specific needs.

---

## 🚀 Tech Stack

- **Frontend:** Vanilla HTML + **Tailwind CSS v4**
- **Backend:** **Flask** (Python API)
- **Data:** Pre-calculated NLP mappings stored in CSV (`backend/*.csv`)
- **Hosting / Deployment:** Configured for a modern split-architecture on **Render** (Static Frontend + Python Web Service)

---

## 📂 Project Structure

- `src/index.html` – Client-side UI and fetch logic
- `src/input.css` – Tailwind input stylesheet
- `backend/app.py` – Flask server and recommendation API (`/recommend`)
- `backend/requirements.txt` – Lean, production-ready Python dependencies
- `dist/` – Compiled, minified production frontend (generated via npm)

---

## 💻 Local Development Setup

### 1. Frontend Setup
Make sure you have Node.js installed.
```bash
# Install frontend dependencies (Tailwind & Concurrently)
npm install
```

### 2. Backend Setup
Avoid creating multiple virtual environments. You only need one at the root map!
```bash
# Create a single clean virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Install the minimal backend requirements
pip install -r backend/requirements.txt
```

### 3. Run the App Locally
While your virtual environment is active, run the dev script. This concurrently spins up your Flask server AND the Tailwind CSS watcher!
```bash
npm run dev
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## ☁️ Production Deployment (Render)

This project has been heavily optimized for cloud deployment on **Render.com**. It uses a split architecture for maximum performance.

### Step 1: Deploy the Backend (Python Web Service)
1. Create a new **Web Service** on Render.
2. Link your GitHub repository.
3. Configure the settings:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r backend/requirements.txt`
   - **Start Command:** `cd backend && gunicorn app:app --bind 0.0.0.0:$PORT`
4. Deploy and copy the resulting `.onrender.com` URL.

### Step 2: Connect the Frontend
1. Open `src/index.html` in your code editor.
2. Locate the `BACKEND_URL` variable (around line 81) and paste your newly created backend Render URL.
3. Build the production `dist` folder locally:
   ```bash
   npm run build:prod
   copy src\index.html dist\index.html
   ```

### Step 3: Deploy the Frontend (Static Site)
1. Create a new **Static Site** on Render.
2. Link the identical GitHub repository.
3. Configure the settings:
   - **Build Command:** `npm install && npm run build:prod && mkdir -p dist && cp src/index.html dist/index.html`
   - **Publish Directory:** `dist`
4. Deploy! Your highly optimized frontend will now securely communicate with your Flask backend.

---

## 🔌 API Reference

### `POST /recommend`
Evaluates user text and returns video objects.
- **Request Body:** `{ "user_text": "I have a lot of neck tension today" }`
- **Response:** Array of matched yoga videos containing the `yoga_type` and `yt_link`.
