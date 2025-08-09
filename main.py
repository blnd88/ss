import streamlit as st

st.set_page_config(page_title="Our Love Playlist", page_icon="🎵", layout="centered")

st.title("🎶 Our Love Playlist 🎶")
st.markdown("Every song here is a scene in our drama. 💖")

playlist = {
    "Die with a Smile – Lady Gaga & Bruno Mars": "https://raw.githubusercontent.com/yourusername/yourrepo/main/d.mp3",
    "Those Eyes – New West": "https://raw.githubusercontent.com/yourusername/yourrepo/main/t.mp3",
    "Lover – Taylor Swift": "https://raw.githubusercontent.com/yourusername/yourrepo/main/l.mp3",
    "Marry you": "https://raw.githubusercontent.com/yourusername/yourrepo/main/m.mp3",
    "Love Story – Taylor Swift": "https://raw.githubusercontent.com/yourusername/yourrepo/main/love.mp3",
    "Bihibbek W Bghaar – Assi El Hallani": "https://raw.githubusercontent.com/yourusername/yourrepo/main/b.mp3",
    "Min awal diea": "https://raw.githubusercontent.com/yourusername/yourrepo/main/es.mp3"
}

messages = {
    "Die with a Smile – Lady Gaga & Bruno Mars": "If I had to end it all, I’d want to ‘die with a smile’—because you’re my reason to smile forever.",
    "Those Eyes – New West": "Those eyes… they see straight into my soul.",
    "Lover – Taylor Swift": "Can I go where you go? Can we always be this close forever and ever?",
    "Marry you": "In a hundred lifetimes, I’d still find you and marry you every time.",
    "Love Story – Taylor Swift": "This is our love story, and I’ll fight for it every single day.",
    "Bihibbek W Bghaar – Assi El Hallani": "I love you, and yes… I get jealous too.",
    "Min awal diea": "From the very first moment, my heart knew you were the one — like the opening scene of a love story that never ends."
}

song_choice = st.selectbox("Choose a scene from our drama:", list(playlist.keys()))

audio_url = playlist[song_choice]
st.markdown(f"**Now Playing:** {song_choice}")
st.audio(audio_url, format="audio/mp3")

st.markdown(f"💌 **Scene Note:** {messages[song_choice]}")

video_url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/ds.mp4"
st.video(video_url)
