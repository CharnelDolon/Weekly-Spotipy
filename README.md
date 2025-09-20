🎵 Discover Weekly Saver

A Flask web application that automatically saves tracks from your Spotify Discover Weekly playlist into a custom playlist called Saved Weekly, ensuring you never lose your favorite weekly recommendations.

🚀 Features

Spotify Login: Secure OAuth 2.0 authentication using the Spotify API.

Discover Weekly Backup: Automatically copies all tracks from your Discover Weekly playlist to a persistent Saved Weekly playlist.

Auto Refresh Tokens: Access tokens are refreshed seamlessly to maintain authorization.

Playlist Creation: If the Saved Weekly playlist doesn’t exist, it will be created automatically.

🛠️ Tech Stack

Backend Framework: Flask

Spotify API Client: Spotipy

Authorization: Spotify OAuth

📂 Project Structure
.
├── app.py                # Main Flask application
└── README.md              # Project documentation

⚡ Setup Instructions
1️⃣ Prerequisites

Python 3.8+

A Spotify Developer Account

Your Spotify Client ID and Client Secret

2️⃣ Clone the Repository
git clone https://github.com/your-username/discover-weekly-saver.git
cd discover-weekly-saver

3️⃣ Install Dependencies
pip install flask spotipy

4️⃣ Configure Environment Variables

Create a .env file or edit the app.py directly with your credentials:

SPOTIPY_CLIENT_ID="YOUR_CLIENT_ID"
SPOTIPY_CLIENT_SECRET="YOUR_CLIENT_SECRET"
SECRET_KEY="YOUR_SECRET_KEY"


⚠️ Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with the values from your Spotify Dashboard
.
⚠️ Replace SECRET_KEY with a secure random string for Flask session handling.

5️⃣ Run the App
python app.py


The server will start at:

http://127.0.0.1:5000/

🌐 Usage

Go to http://127.0.0.1:5000/

Log in with your Spotify account.

The app will:

Retrieve your Discover Weekly playlist.

Create a Saved Weekly playlist if it doesn’t exist.

Add all current Discover Weekly songs to it.

⚠️ Important Notes

Redirect URI: Ensure your Spotify App Dashboard includes

http://127.0.0.1:5000/redirect


as a valid redirect URI.

Token Expiration: The app automatically refreshes expired tokens using the stored refresh token.

🧩 Example Code Snippet
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri=url_for('redirect_path', _external=True),
        scope="user-library-read playlist-modify-public playlist-modify-private"
    )

🔒 Security

Never commit your Client Secret or SECRET_KEY to a public repository.

Use environment variables (os.getenv) instead of hardcoding credentials in production.
