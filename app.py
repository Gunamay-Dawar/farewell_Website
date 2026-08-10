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
music_path = "assets/song.mp3"

music_path = "assets/song.mp3"

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
        "description": "This marks exactly one year since we met. I remember after this our group litr fought w neel😂😂. Hahahh we r so kaleshi! #rakhisawant "
    },
    {
        "image": "assets/dec 22 2022.jpeg", 
        "tagline": "27th December 2021, Rajsi's 13th Birthday",
        "description": "Mc donalds forever fav place for us fatties! Btw i still cant believe i was 14 and u were 12 for 2 months. Ur such a kid yaar"
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
        "description": "We had surprised u at Glens Bakehouse. Forever gonna msis the eating red velvet mini-cupcakes and chocolate croissant w my fav "
    },
    {
        "image": "assets/fgfgg.jpeg",
        "tagline": "1st January 2026.",
        "description": "Favourite New years! I remember dancing in the park with everyone!!"
    },
    {
        "image": "assets/gunu rajsi last day pic nikita took.jpeg", 
        "tagline": "30th July 2025! ",
        "description": "Gunamay's Last photo with rajsi as offical purvaites. This was taken by Nikita infront of Purva fairmont main gate. "
    },
    {
        "image": "assets/gunu yaps pfp.jpeg",
        "tagline": "21st June, 2026",
        "description": "Gunamay had come back from ashoka! This was taken from Ashmita's digi camera at the badminton court."
    },
     {
        "image": "assets/matching tshirt day trio pic.jpeg",
        "tagline": "29th June 2026",
        "description": "Rajsi, Adhit and gunu at S 203! Last pic in S 203"
    },
    {
        "image": "assets/ggyg.jpeg",
        "tagline": "20th november 2021",
        "description": "Gunamay 14th bday"
    },
    {
        "image": "assets/adhit3.jpeg",
        "tagline": "Exchanging gifts!!",
        "description": "I think it's so funny how you got me a proper nice T-shirt that I still wear and I got you some goofy stuff😂😂."
    },{
        "image": "assets/8th october 2023.jpg",
        "tagline": "8th October, 2023",
        "description": "Do you remember this pic? Bro this brough back so many old 10th grade memories! I remember this day so clearly, this picture is at mughal treat when we had gone to buy gauri ka final farwell gift. What a fun day i remember hwo much we roamed 27th main that dayy!!"
    }, 
     {
        "image": "assets/cvvv.jpeg",
        "tagline": "9th May 2026",
        "description": "Pizza bakery dinner!"
    },
    {
        "image": "assets/csss.jpeg",
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
    },{
        "image": "assets/adhit5.jpeg",
        "tagline": "Your Birthday!!",
        "description": "This was right before I threw a cupcake in your eye. Im sorry for that I was aiming at your forehead but I missed. Still I think it's hilarious how you had no idea 😂"
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
        "image": "assets/adhit2.jpeg",
        "tagline": "The first chapal pose!!",
        "description": "That day was hilarious Im sure u remember it. Even though it's making fun of me I love that it started a new tradition where we take this pic on every important occasion 😋"
    },
    {
        "image": "assets/sep 9 2023.jpg",
        "tagline": "9th September, 2023",
        "description": "I think this is one of my fondest memories with you! Ill never forget dancing on Hey! Ho! Shanaya Shanaya! I dont think ill ever be able to watch any movie of sid malothra without being reminded of you."
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
    },  {
        "image": "assets/aug 21 2022.jpg",
        "tagline": "21st August, 2022",
        "description": " Shraddha's 15th Birthday. I think this is our first pic together?"
    },
    {
        "image": "assets/aug 27 2022.jpg",
        "tagline": "27th August, 2022",
        "description": "We had gone out for Shrabs ka 15th birthday to polar bear! I remEmebr we were tryign to take embaressing pics of u LMFOAO."
    }, 
     {
        "image": "assets/aug 21 2021.jpg",
        "tagline": "21st August, 2021",
        "description": " Shraddha's 14th Birthday. We all had made a huge card together for her and gone to her house to cut the cake that My3 had made."
    },
    {
        "image": "assets/dec 27, 2021.jpg",
        "tagline": "27th December, 2021",
        "description": "Rajsi's 13th Birthday. Ill never be able to believe that when we actually met for the first tiem you were 11 and i was 13 and now we are 17 and 18???!! WHATTT how did time fly so fast? It seems like just yesterday we were kaleshing on stupid topics every thrusday?"
    },
     {
        "image": "assets/adhit1.jpeg",
        "tagline": "Yulu day😋😋",
        "description": " I lost the clip where you're taking me on yulu but I have to say I was impressed I didn't expect you to be able to balance me. This gives me little confidence in you to finally learn scooty and not crash I think you will be able to do it eventually ☝️"
    },
    {
        "image": "assets/oct 5 2022.jpg",
        "tagline": "5th October, 2022. Garba 2022",
        "description": "You me and Shraddha at Mc Donalds after attending garba in 2022 at HSR BDA"
    },
    
     {
        "image": "assets/june 5 2022.jpg",
        "tagline": "5th June 2022",
        "description": " Rajat's Birthday party at Taco Bell! Fav person rajat da LMFAOOA. "
    },
    {
        "image": "assets/24 october 2022.jpg",
        "tagline": "24th October, 2022. Garba 2022",
        "description": "This was Diwali of 2022. I believe this was my third Diwali at Purva with you all! And i remember this was our first year tryign to light a lanturn and it was such a fail cus it kept hitting the V block houses LMFAOAO."
    }, 
     {
        "image": "assets/july 14 202`.jpg",
        "tagline": "14th July, 2021",
        "description": "Bro ur snapchat phase is so funny. I think u should be grateful i didnt chose any bad picture cus I definately wanted to bro. But since I am a changed man, I've decided to be nice to you and use only nice pics.  "
    },
    {
        "image": "assets/25th mar 2024.jpg",
        "tagline": "25th March, 2024. Holi 2024",
        "description": "I dont think this pic deserves any description cus we both know this day very well😂😂😭"
    },
     {
        "image": "assets/2.jpeg",
        "tagline": "21st october, 2025",
        "description": "BRO this is another pic which does not require any explanation. I still think this is my fav pic of ours LMFOAOAO. But gen what a funny day to look back on bro. "
    },

    {
        "image": "assets/adhit4.jpeg",
        "tagline": "Cooking maggi at gunus✌️",
        "description": "Love ragebaiting you but to be fair all you did was stir only so it's fine I think my ragebait was valid"
    },
    {
        "image": "assets/1.jpeg",
        "tagline": "26th June, 2026",
        "description": "Bro this is such a cute pic! This is the day Sidhika was leaving to college. "
    },

    {
        "image": "assets/aug 28 2022.jpg",
        "tagline": "28th August, 2022",
        "description": "Shraddha's birthday at Polar bear. I remember this was the year we made shrabs ka card together while watching kabhi khushu kabhi gham! and i remember writign the - not sohan not mohan only rohan! like 10 times in the cardd!!"
    }, 
     {
        "image": "assets/rajsi gunu infront of diwali house.jpeg",
        "tagline": "Infront of Diwali House",
        "description": "I think im going to remember this house forever. 2 years in a row getting scolded by same uncle is forever such a fond memory with you!"
    },

    {
        "image": "assets/4.jpeg",
        "tagline": "22nd June, 2025",
        "description": "HAHHAHA im so sorry, now that i see this video i feel so bad for pulling ur hairrrr😭😭😭😭"
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