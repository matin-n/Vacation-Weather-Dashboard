import streamlit as st
import pandas as pd
import plotly.express as px

# Access mapbox token from secrets.toml
mapbox_token = st.secrets["mapbox_token"]

# Import weather data into a DataFrame.
df = pd.read_csv("cities.csv")[
    [
        "City",
        "Country",
        "Lat",
        "Lng",
        "Max Temp",
        "Humidity",
        "Cloudiness",
        "Wind Speed",
    ]
]

# Streamlit page configuration.
st.set_page_config(
    page_title="Vacation Weather Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Vacation Weather Dashboard")

# Sidebar to customize the map.
with st.sidebar:
    st.title("Map Settings")

    # Get the user input for the heatmap data selection, map style, heatmap marker radius, and marker opacity.
    heatmap_selection = st.selectbox(
        "Heatmap Selection",
        [
            "Max Temp",
            "Humidity",
            "Wind Speed",
            "Cloudiness",
        ],
    )

    map_style = st.selectbox(
        "Select a mapbox style",
        [
            "basic",
            "streets",
            "outdoors",
            "light",
            "dark",
            "satellite",
            "satellite-streets",
        ],
    )

    heatmap_colorscale = st.selectbox("Color Scale", px.colors.named_colorscales())

    radius_level = st.slider("Set the radius of influence of each point", 1, 20, 10)

    opacity_level = st.slider("Marker opacity", 0.0, 1.0, 0.7)


with st.empty():
    # Create and display the map.
    st.header(f"{heatmap_selection} Heatmap")
    # https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox
    fig = px.density_mapbox(
        df,
        lat="Lat",
        lon="Lng",
        z=heatmap_selection,
        radius=radius_level,
        hover_data={
            "Lat": False,
            "Lng": False,
            "City": True,
            "Country": True,
            "Max Temp": False,
            "Humidity": False,
            "Cloudiness": False,
            "Wind Speed": False,
        },
        color_continuous_scale=heatmap_colorscale,
        center=dict(lat=0, lon=180),
        zoom=0,
        opacity=opacity_level,
    )

    # Default hovertemplate.
    # fig.data[0].hovertemplate

    # Modify the default hovertemplate.
    fig.update_traces(
        hovertemplate="%{customdata[2]}, %{customdata[3]}<br><extra>"
        + heatmap_selection
        + " %{z:.0f}</extra>"
    )

    # Update the mapbox style.
    fig.update_layout(
        mapbox_style=map_style,
        mapbox_accesstoken=mapbox_token,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    )

    # Disable the plotly modebar.
    config = {
        "displayModeBar": False,
    }

    # Display the map.
    st.plotly_chart(fig, use_container_width=True, config=config)


# Exploring correlations between the weather variables.
with st.expander("Explore the Data"):

    # Scatter plots for each weather variable.
    st.header("Scatter Plots")
    st.subheader("Max Temperature vs. Latitude")
    st.plotly_chart(
        px.scatter(
            df,
            x="Lat",
            y="Max Temp",
            trendline="ols",
        ),
        use_container_width=True,
    )

    st.subheader("Humidity vs. Latitude")
    st.plotly_chart(
        px.scatter(
            df,
            x="Lat",
            y="Humidity",
            trendline="ols",
        ),
        use_container_width=True,
    )

    st.subheader("Cloudiness vs. Latitude")
    st.plotly_chart(
        px.scatter(
            df,
            x="Lat",
            y="Cloudiness",
            trendline="ols",
        ),
        use_container_width=True,
    )

    st.subheader("Wind Speed vs. Latitude")
    st.plotly_chart(
        px.scatter(
            df,
            x="Lat",
            y="Wind Speed",
            trendline="ols",
        ),
        use_container_width=True,
    )

    # Cartesian plot with data visualized as colored rectangular tile.
    st.subheader("Correlation Heatmap")
    st.plotly_chart(
        px.imshow(
            df[["Lat", "Max Temp", "Humidity", "Cloudiness", "Wind Speed"]].corr(),
            color_continuous_scale="RdBu",
        ),
        use_container_width=True,
    )

    # Create a table of the data.
    st.header("Data Table")
    st.table(df)
