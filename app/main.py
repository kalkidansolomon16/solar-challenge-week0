import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from app.utils import existing_countries, load_countries, METRICS, top_regions, infer_region_column

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title("Solar Potential: Cross-Country Explorer")
st.caption("Load local cleaned CSVs from data/ and interactively explore GHI/DNI/DHI across countries.")

available = existing_countries()
selected = st.multiselect(
    "Select countries",
    options=sorted(available),
    default=sorted(available),
)

metric = st.selectbox("Metric", METRICS, index=0)

@st.cache_data(show_spinner=False)
def _load(selected_countries):
    return load_countries(selected_countries)

try:
    df = _load(selected)
except FileNotFoundError as e:
    st.warning(str(e))
    st.stop()

st.subheader("Distribution by Country")
col1, col2 = st.columns([2, 1])
with col1:
    if metric in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x="Country", y=metric, palette="Set2", ax=ax)
        ax.set_title(f"{metric} by Country")
        ax.set_xlabel("Country")
        ax.set_ylabel(metric)
        st.pyplot(fig, clear_figure=True)
    else:
        st.info(f"Metric {metric} not found in data.")

with col2:
    st.markdown("**Summary (mean/median/std)**")
    if metric in df.columns:
        tbl = (
            df.groupby("Country")[metric]
            .agg(["mean", "median", "std"])  # type: ignore[arg-type]
            .round(3)
        )
        st.dataframe(tbl)
    else:
        st.write("N/A")

st.divider()
st.subheader("Top Regions by Average Metric")

n_top = st.slider("How many regions?", min_value=5, max_value=25, value=10, step=1)
region_col = infer_region_column(df)
if not region_col:
    st.info("No region-like column found in the data; cannot display top regions table.")
else:
    try:
        top = top_regions(df, metric=metric, n=n_top)
        st.dataframe(top)
    except ValueError as e:
        st.info(str(e))

st.divider()
st.caption("Tip: To run locally, install streamlit, pandas, seaborn, matplotlib. Then: `streamlit run app/main.py`")
