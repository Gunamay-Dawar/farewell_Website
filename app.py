import streamlit as st
import base64
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Rajsi & Gunu's Memory Lane",
    page_icon="🎓",
    layout="centered"
)

# --- BACKGROUND MUSIC FUNCTION ---

music_path = "assets/song.mp3"  # Change 'music.mp3' if your file is named 'song.mp3'

# 2. Pass the variable to both functions
def add_bg_music(music_path) : 
    try:
        st.audio(music_path, format="audio/mp3")
    except Exception:
        pass
# --- HEADER SECTION ---
st.title(" Rajsi & Gunu's Memory Lane ❤️")
st.write("A trip down memory lane before we head off to our next adventures! Scroll down to relive the best moments.")

# --- BACKGROUND MUSIC ---
music_path = "assets/song.MP3"

music_path = "assets/song.MP3"

if os.path.exists(music_path):
    st.audio(music_path, format="audio/mp3", loop=True)
else:
    st.error(f"Audio file not found at '{music_path}'!")

# --- MEMORIES GALLERY ---
# Add your photos, taglines, and descriptions here!
memories = [
    {
        "image": "assets/20 nov 2021.jpeg", 
        "tagline": "20th November 2021, Gunamay's 14th birthday",
        "description": "This marks exactly one year since we meat. I rememeber after this our group litr fought w neel😂😂 "
    },
    {
        "image": "assets/WhatsApp Image 2026-08-08 at 8.16.11 PM.jpeg", 
        "tagline": "27th December 2021, Rajsi's 13th Birthday",
        "description": "Mc dondalds forever fav place for us fatties! Btw i still cant believe i was 14 and u were 12 for 2 months. Ur such a kid yaar"
    },
    {
        "image": "assets/gunuuu.jpeg", 
        "tagline": "21st August 2022, Shraddha's 15th birthday",
        "description": "We had gone to the terrace and I still remmeber how amazing the sky looked!! Forever one of my fav purva memories w u. "
    },
    {
        "image": "assets/9999.jpeg",
        "tagline": "2nd May 2026",
        "description": "We played cricket infront of M block. Hahah such old memories type shi!!"
    },
    {
        "image": "assets/hnnn.jpeg", 
        "tagline": "27th December 2025! Rajsi's 17th Birthday at Glens",
        "description": "We had surprised u at glens Bakehouse."
    },
    {
        "image": "assets/fgfgg.jpeg",
        "tagline": "1st January 2026.",
        "description": "Favourite New years!"
    },
    {
        "image": "assets/gunu rajsi last day pic nikita took.jpeg", 
        "tagline": "30th July 2025! ",
        "description": "Gunamay's Last photo with rajsi as offical purvaites. This was taken by Nikita "
    },
    {
        "image": "assets/gunu yaps pfp.jpeg",
        "tagline": "21st June, 2026",
        "description": "Gunamay had come back from ashoka! This was taken from Ashmita's digi camera at the badminton court."
    },
     {
        "image": "assets/matching tshirt day trio pic.jpeg",
        "tagline": "9th May 2026",
        "description": "This was taken at Pizza Bakery HSR Layout. Ayaan's last board exam and Gunamays last day before leaving to ashoka."
    },
    {
        "image": "assets/ggyg.jpeg",
        "tagline": "20th november 2021",
        "description": "Gunamay 14th bday"
    },
     {
        "image": "assets/cvv.jpeg",
        "tagline": "9th May 2026",
        "description": "Pizza bakery dinner!"
    },
    {
        "image": "assets/css.jpeg",
        "tagline": "3rd August, 2026",
        "description": "Morning brunch, few days before the great seperation 💔"
    },
    {
        "image": "assets/----.jpeg",
        "tagline": "5th October, 2022",
        "description": "Garba 2022 in BDA Layout. Forever HSR Layout ka awara duo"
    },
    {
        "image": "assets/000.jpeg",
        "tagline": "13th November 2022",
        "description": "Rohan's Birthday dinner at his house."
    },
    {
        "image": "assets/ddd.jpeg",
        "tagline": "17th November, 2025",
        "description": "Gunamay's surprise bday rajsi had arranged! Forever grateful (not greatful) to you. Cannot express how happy and shocked I was:) "
    },
    {
        "image": "assets/ddddd.jpeg",
        "tagline": "20th October, 2025",
        "description": "Diwali 2025. Forever fav festival of rajsi n gunu"
    },
       {
        "image": "assets/ffffg.jpeg",
        "tagline": "29th July, 2026",
        "description": "Gunamay's Last day in Purva. We wore matching tshirts #alwaystwinning #twins #purvaOGduo"
    },
    {
        "image": "assets/rajsi gunu 2025 garba.jpeg",
        "tagline": "19th October, 2024",
        "description": "2024 Garba!"
    },
      {
        "image": "assets/rajsi gunu ayaan apr day.jpeg",
        "tagline": "22nd June, 2026",
        "description": "Rajsi and Gunu in APR"
    },
    {
        "image": "assets/rajsi gunu mirror selfi at jersey store.jpeg",
        "tagline": "7th August, 2026",
        "description": "Gunamay and Rajsi at jersey store"
    },
     {
        "image": "assets/rajsi gunu grad.jpeg",
        "tagline": "9th January, 2026",
        "description": "Gunamays Grad"
    },
    {
        "image": "assets/rajsi solo w flowers bday.jpeg",
        "tagline": "27th December, 2025",
        "description": "Rajsi's 17th Birthday"
    },
    {
        "image": "assets/rajsi gunu world cup day.jpeg",
        "tagline": "19th July, 2026",
        "description": "Morning of FIFA 2026 world cup"
    },
    {
        "image": "assets/rajsi gunu terrace pci.jpeg",
        "tagline": "19th Julyl, 2026",
        "description": "Evening of FIFA 2026 world cup at terrace"
    },{
        "image": "assets/rasji mirror video call braces.jpeg",
        "tagline": "2nd August, 2026",
        "description": "The day Rajsi got ger braces off after 2 years!!"
    },
    {
        "image": "assets/rajsi shrabs gunu coffee makers day.jpeg",
        "tagline": "23rd July, 2026",
        "description": "Rajsi Shraddha and Gunamay at Coffee makers"
    },
    {
        "image": "assets/rajsi gunu diwali 2025 lighter pic.jpeg",
        "tagline": "31st October, 2024",
        "description": "Diwali 2024! Forever lighter pic duo"
    },
    {
        "image": "assets/rajsi gunu bday christmas.jpeg",
        "tagline": "27th December, 2025",
        "description": "Rajsi's 17th Birthday eve!!"
    }
    ]

    # Copy and paste the block above to add more photos


# Loop through the list and display each memory
for memory in memories:
    img_path = memory["image"]
    if os.path.exists(img_path):
        try:
            st.image(img_path, use_container_width=True)
            st.subheader(memory.get("tagline", ""))
            st.write(memory.get("description", ""))
            st.markdown("---")
        except Exception:
            st.error(f"Error loading image file: '{img_path}'. File may be corrupt or 0 bytes.")
    else:
        st.warning(f"Image not found at '{img_path}'. Check filename in assets folder!")

# --- FOOTER ---
st.markdown("<h4 style='text-align: center;'>To many more memories in the future! ❤️</h4>", unsafe_allow_html=True)