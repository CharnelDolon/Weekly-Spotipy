# 🎶 Spotify Discover Weekly Saver

This Flask + Spotipy application allows you to **automatically save songs** from your weekly *Discover Weekly* playlist into a permanent *Saved Weekly* playlist.  
It ensures that you never lose track of songs after your Discover Weekly refreshes.

---

## 📋 Features
- **Login with Spotify** using OAuth2.
- Automatically creates a **Saved Weekly** playlist (if it doesn't exist).
- Copies all tracks from your **Discover Weekly** playlist into **Saved Weekly**.

---

## ⚙️ Prerequisites
- Python 3.8 or higher
- A [Spotify Developer](https://developer.spotify.com/dashboard/) account
- Flask & Spotipy Python packages

---

## 🛠 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/spotify-discover-weekly-saver.git
   cd spotify-discover-weekly-saver
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask spotipy
   ```

4. **Set up your Spotify app**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and note down:
     - **Client ID**
     - **Client Secret**
   - Set a **Redirect URI** to:
     ```
     http://localhost:5000/redirect
     ```

---

## ⚡ Configuration

Create a `.env` file in the project root or set environment variables:

```env
SECRET_KEY=your_flask_secret
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

Then update the code in `create_spotify_oauth()` to load these from the environment,  
or replace `"YOUR_CLIENT_ID"` and `"YOUR_CLIENT_SECRET"` directly in the script.

---

## ▶️ Usage

1. **Run the Flask app**
   ```bash
   python app.py
   ```
   The app will start on [http://localhost:5000](http://localhost:5000)

2. **Login with Spotify**
   - Navigate to the root URL.
   - You’ll be redirected to Spotify’s login and authorization page.

3. **Save your Discover Weekly**
   - After authorization, the app creates a playlist called **Saved Weekly** (if it doesn’t already exist).
   - All tracks from your current Discover Weekly are added to Saved Weekly.

---

## 📂 Project Structure
```
.
├─ app.py                 # Main Flask application
├─ requirements.txt        # Dependencies (optional)
└─ README.md               # This file
```

---

## 🔑 Key Routes
| Route | Description |
|------|-------------|
| `/` | Redirects to Spotify login authorization |
| `/redirect` | Handles Spotify OAuth callback and token exchange |
| `/saveDiscoverWeekly` | Saves all Discover Weekly songs to Saved Weekly |

---

## 🧩 Code Overview

Below is a simplified explanation of important functions:

- **`login()`**  
  Generates an authorization URL and redirects the user to Spotify for login.

- **`redirect_path()`**  
  Handles Spotify’s callback, exchanges the code for an access/refresh token, and stores it in a Flask session.

- **`save_discover_weekly()`**  
  Finds your Discover Weekly playlist and copies all its tracks into Saved Weekly.

- **`get_token()`**  
  Checks if the access token is expired and refreshes it if needed.

---

## 💡 Tips
- The Flask `SECRET_KEY` is required for session management.  
- Make sure the redirect URI in your Spotify app matches exactly what’s in the code.
- You can deploy this on services like **Heroku**, **Render**, or **AWS** with minor adjustments.
