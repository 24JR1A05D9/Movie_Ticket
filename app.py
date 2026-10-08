import streamlit as st

# Page settings
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# Movie-themed styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F9E5E7;
    }

    .block-container {
        max-width: 750px;
        padding-top: 2rem;
    }

    .movie-title {
        text-align: center;
        color: #741C2A;
        font-size: 42px;
        font-weight: bold;
    }

    .movie-subtitle {
        text-align: center;
        color: #8F3948;
        font-size: 18px;
        margin-bottom: 20px;
    }

    .movie-decoration {
        text-align: center;
        font-size: 28px;
        letter-spacing: 18px;
        opacity: 0.75;
        margin: 12px 0;
    }

    .section-title {
        color: #741C2A;
        font-size: 22px;
        font-weight: bold;
        margin-top: 15px;
    }

    .stButton > button {
        background-color: #8F2D3D;
        color: white;
        border-radius: 12px;
        border: none;
        font-size: 17px;
        font-weight: bold;
        padding: 12px;
    }

    .stButton > button:hover {
        background-color: #741C2A;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Decorative movie emojis
st.markdown(
    '<div class="movie-decoration">🎬 🍿 🎟️ 🎞️ 🎥</div>',
    unsafe_allow_html=True
)

# Title
st.markdown(
    '<div class="movie-title">🎬 MOVIE NIGHT 🎬</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="movie-subtitle">🍿 Book your movie experience in a few clicks! 🎟️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="movie-decoration">🎫 ⭐ 🍿 🎥 🎬</div>',
    unsafe_allow_html=True
)

st.divider()

# Movie data
movies = {
    "Pushpa 2": 180,
    "Kalki 2898 AD": 200,
    "RRR": 150,
    "Salaar": 180,
    "Devara": 170
}

# Movie selection
st.markdown(
    '<div class="section-title">🎞️ Choose Your Movie</div>',
    unsafe_allow_html=True
)

movie = st.selectbox(
    "🎬 Select Movie",
    list(movies.keys())
)

st.info(f"🎟️ Ticket Price: ₹{movies[movie]} per ticket")

# Show details
st.markdown(
    '<div class="section-title">🕐 Show Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    show_date = st.date_input("📅 Select Date")

with col2:
    show_time = st.selectbox(
        "🕐 Select Show",
        [
            "10:00 AM",
            "1:00 PM",
            "4:00 PM",
            "7:00 PM",
            "10:00 PM"
        ]
    )

# Tickets
st.markdown(
    '<div class="section-title">🎟️ Tickets</div>',
    unsafe_allow_html=True
)

tickets = st.number_input(
    "🎫 Number of Tickets",
    min_value=1,
    max_value=10,
    value=1
)

# Seats
st.markdown(
    '<div class="section-title">💺 Select Your Seats</div>',
    unsafe_allow_html=True
)

seats = st.multiselect(
    "Choose seats",
    [
        "A1", "A2", "A3", "A4",
        "B1", "B2", "B3", "B4",
        "C1", "C2", "C3", "C4",
        "D1", "D2", "D3", "D4"
    ],
    max_selections=tickets
)

# Calculate price
ticket_price = movies[movie]
total = ticket_price * tickets

st.divider()

# Booking summary
st.markdown(
    '<div class="section-title">🧾 Booking Summary</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.write("🎬 **Movie**")
    st.write("📅 **Date**")
    st.write("🕐 **Show**")
    st.write("🎟️ **Tickets**")
    st.write("💺 **Seats**")

with col2:
    st.write(movie)
    st.write(show_date)
    st.write(show_time)
    st.write(tickets)

    if seats:
        st.write(", ".join(seats))
    else:
        st.write("Not selected")

st.metric(
    "💰 Total Amount",
    f"₹{total}"
)

st.divider()

# Confirm booking
if st.button(
    "🎟️ CONFIRM BOOKING",
    use_container_width=True
):

    if len(seats) != tickets:

        st.error(
            f"💺 Please select exactly {tickets} seat(s) before booking."
        )

    else:

        st.success(
            "🎉 Your movie tickets are booked successfully!"
        )

        st.balloons()

        st.markdown("### 🎫 Your Movie Ticket")

        st.write(f"🎬 **Movie:** {movie}")
        st.write(f"📅 **Date:** {show_date}")
        st.write(f"🕐 **Show:** {show_time}")
        st.write(f"🎟️ **Tickets:** {tickets}")
        st.write(f"💺 **Seats:** {', '.join(seats)}")
        st.write(f"💰 **Total Paid:** ₹{total}")

        st.success("🍿 Enjoy your movie! 🎬❤️")

st.markdown(
    '<div class="movie-decoration">🍿 🎬 🎟️ 🎞️ 🍿</div>',
    unsafe_allow_html=True
)