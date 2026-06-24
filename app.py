import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="RaceIQ",
    layout="wide"
)

st.title("🏎️ RaceIQ")
st.subheader("AI-Powered F1 Strategy & Analytics Platform")

st.write(
    "Welcome to RaceIQ. Analyze Formula 1 data, explore driver performance, and generate AI-powered race strategies."
)
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///raceiq.db")

races = pd.read_sql("SELECT * FROM races", engine)

st.set_page_config(
    page_title="RaceIQ",
    layout="wide"
)

st.title("🏎️ RaceIQ")
st.subheader("AI-Powered F1 Strategy & Analytics Platform")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Seasons",
        races["season"].nunique()
    )

with col2:
    st.metric(
        "Races",
        len(races)
    )

with col3:
    st.metric(
        "Circuits",
        races["circuit_name"].nunique()
    )

with col4:
    st.metric(
        "Countries",
        races["country"].nunique()
    )
    import plotly.express as px

season_races = (
    races.groupby("season")
    .size()
    .reset_index(name="race_count")
)

fig = px.line(
    season_races,
    x="season",
    y="race_count",
    title="Races Per Season"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Driver Analytics",
        "Constructor Analytics",
        "AI Strategy"
    ]
)
drivers = pd.read_sql(
    "SELECT * FROM driver_standings",
    engine
)
if page == "Driver Analytics":

    st.header("🏎 Driver Analytics")

    top_drivers = drivers.sort_values(
        "points",
        ascending=False
    )

    st.dataframe(
        top_drivers.head(20)
    )

    driver_chart = px.bar(
        top_drivers.head(10),
        x="driver_name",
        y="points",
        title="Top Drivers by Points"
    )

    st.plotly_chart(
        driver_chart,
        use_container_width=True
    )

    drivers["performance_score"] = (
        drivers["points"] +
        drivers["wins"] * 5
    )

    performance_chart = px.bar(
        drivers.sort_values(
            "performance_score",
            ascending=False
        ).head(10),
        x="driver_name",
        y="performance_score",
        title="Driver Performance Score"
    )

    st.plotly_chart(
        performance_chart,
        use_container_width=True
    )
    page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Driver Analytics",
        "Constructor Analytics",
        "AI Strategy"
    ]
)
    constructors = pd.read_sql(
    "SELECT * FROM constructor_standings",
    engine
)
if page == "Constructor Analytics":

    st.header("🏆 Constructor Analytics")

    constructors["dominance_score"] = (
        constructors["points"] +
        constructors["wins"] * 5
    )

    st.dataframe(
        constructors.sort_values(
            "dominance_score",
            ascending=False
        )
    )

    constructor_chart = px.bar(
        constructors.sort_values(
            "dominance_score",
            ascending=False
        ).head(10),
        x="constructor",
        y="dominance_score",
        title="Constructor Dominance Score"
    )

    st.plotly_chart(
        constructor_chart,
        use_container_width=True
    )
if page == "AI Strategy":

    st.header("🤖 AI Strategy Generator")
    weather = st.selectbox(
    "Weather",
    ["Sunny", "Cloudy", "Rain"]
)

position = st.number_input(
    "Current Position",
    min_value=1,
    max_value=20
)

tire_wear = st.slider(
    "Tire Wear (%)",
    0,
    100
)

laps_remaining = st.slider(
    "Remaining Laps",
    1,
    70
)
if st.button("Generate Strategy"):

    if tire_wear > 75:
        strategy = "Pit Stop Recommended"

    elif weather == "Rain":
        strategy = "Switch to Intermediate Tires"

    else:
        strategy = "Stay Out"

    st.success(strategy)