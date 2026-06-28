import streamlit as st

st.set_page_config(
    page_title="String Theory",
    layout="wide"
)

# ======================================
# SESSION
# ======================================

if "score" not in st.session_state:
    st.session_state.score = 30

# ======================================
# STYLE
# ======================================

st.markdown("""
<style>

.stApp{
background:#101010;
}

#MainMenu,footer,header{
visibility:hidden;
}

.card{

background:#1a1a1a;

padding:20px;

border-radius:12px;

border:2px solid #333;

margin-bottom:20px;

color:white;

}

.score{

font-size:32px;

color:#00ff66;

font-weight:bold;

text-shadow:0 0 10px #00ff66;

}

.paper{

background:#ead7af;

padding:25px;

border-radius:10px;

font-family:Georgia;

box-shadow:0px 0px 15px black;

}

.paper h2{

color:black;

}

.paper p{

color:black;

font-size:18px;

line-height:1.7;

}

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER
# ======================================

st.markdown(
f"""
<div class='card'>

<h2>
OPERATION: BORDER LOCK
</h2>

OBJECTIVITY INDEX

<div class='score'>
{st.session_state.score}%
</div>

</div>
""",
unsafe_allow_html=True
)

# ======================================
# MAIN SCREEN
# ======================================

left,right=st.columns([2,1])

with left:

    st.markdown(
    """
    <div class='card'>

    <h3>
    INVESTIGATION BOARD
    </h3>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.image(
        "board.png",
        use_container_width=True
    )


with right:

    st.markdown(
    """
<div class='paper'>

<h2>
SECRET INFORMATION
</h2>

<hr>

<p>

🏛 Minister promises safety

</p>

<hr>

<p>

🎖 Troops approach border

</p>

<hr>

<p>

🏦 Foreign banks freeze assets

</p>

</div>
""",
unsafe_allow_html=True
)

# ======================================
# CHOICE
# ======================================

choice=st.radio(

"Select thread",

[
"🟢 FACT",
"🟡 LOGIC",
"🔴 INCOMPATIBILITY"
]

)

if st.button(
"TIGHTEN THE KNOT OF TRUTH",
use_container_width=True
):

    if "🔴" in choice:

        st.session_state.score=100

        st.balloons()

        st.success(
        "MISSION ACCOMPLISHED"
        )

    elif "🟡" in choice:

        st.session_state.score=55

        st.warning(
        "Only hypothesis"
        )

    else:

        st.session_state.score=20

        st.error(
        "Wrong conclusion"
        )
