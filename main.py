import streamlit as st

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Our Love Playlist", page_icon="🎵", layout="centered")

# --- TITLE ---
st.title("🎶 Our Love Playlist 🎶")
st.markdown("Every song here is a scene in our drama. 💖")


# --- PLAYLIST DATA (local file paths) ---
playlist = {
    "Die with a Smile – Lady Gaga & Bruno Mars": r"d.mp3",
    "Those Eyes – New West": r"t.mp3",
    "Lover – Taylor Swift": r"l.mp3",
    "Marry you": r"m.mp3",
    "Love Story – Taylor Swift": r"love.mp3",
    "Bihibbek W Bghaar – Assi El Hallani": r"b.mp3",
    "Min awal diea": r"es.mp3"
}

# --- SCENE NOTES ---
messages = {
    "Die with a Smile – Lady Gaga & Bruno Mars": "If I had to end it all, I’d want to ‘die with a smile’—because you’re my reason to smile forever.",
    "Those Eyes – New West": "Those eyes… they see straight into my soul.",
    "Lover – Taylor Swift": "Can I go where you go? Can we always be this close forever and ever?",
    "Marry you": "In a hundred lifetimes, I’d still find you and marry you every time.",
    "Love Story – Taylor Swift": "This is our love story, and I’ll fight for it every single day.",
    "Bihibbek W Bghaar – Assi El Hallani": "I love you, and yes… I get jealous too.",
    "Min awal diea" : "From the very first moment, my heart knew you were the one — like the opening scene of a love story that never ends."
}

# --- SELECT SONG ---
song_choice = st.selectbox("Choose a scene from our drama:", list(playlist.keys()))

# --- LOAD & PLAY SONG ---
file_path = playlist[song_choice]
with open(file_path, "rb") as audio_file:
    audio_bytes = audio_file.read()
st.markdown(f"**Now Playing:** {song_choice}")
st.audio(audio_bytes, format="audio/mp3")

# --- ROMANTIC MESSAGE ---
st.markdown(f"💌 **Scene Note:** {messages[song_choice]}")

# --- ADD A VIDEO ---
with open(r"ds.mp4", "rb") as video_file:
    video_bytes = video_file.read()

st.video(video_bytes)


