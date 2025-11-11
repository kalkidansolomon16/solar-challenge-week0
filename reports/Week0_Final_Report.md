# Week 0 Final Report: Solar Potential Across Benin, Sierra Leone, and Togo

Author: <your name>
Date: <date>

1) Executive Summary
- Goal: Compare solar resource potential across Benin, Sierra Leone, and Togo to guide prioritization for solar deployment.
- Key outputs: Cross-country EDA notebook (compare_countries.ipynb), significance testing on GHI, and an interactive Streamlit dashboard.
- Highlights:
  - Boxplots and summary statistics reveal relative levels and variability of GHI, DNI, and DHI across countries.
  - One-way ANOVA and Kruskal–Wallis on GHI indicate whether differences are statistically significant (see Notebook output).
  - Dashboard enables quick filtering by country and inspection of top-performing regions.

2) Data and Methods
- Inputs: Cleaned CSVs located locally under data/: benin_clean.csv, sierra_leone_clean.csv, togo_clean.csv.
- Metrics: GHI (Global Horizontal Irradiance), DNI (Direct Normal Irradiance), DHI (Diffuse Horizontal Irradiance).
- Analysis steps (see compare_countries.ipynb):
  - Load cleaned CSVs and coerce metrics to numeric.
  - Visualize distributions via side-by-side boxplots per metric.
  - Summarize mean, median, and standard deviation by country.
  - Statistical testing on GHI with one-way ANOVA and Kruskal–Wallis.

3) Results Snapshot
- Visuals: Boxplots for GHI, DNI, DHI by country; bar chart ranking countries by average GHI.
- Summary table: Mean/Median/Std for each metric by country (see Notebook display output).
- Statistical tests on GHI: Report F/H statistics and p-values from Notebook. If p < 0.05, differences are significant.

4) Key Observations
- Observation 1: <e.g., Country X shows the highest median GHI with moderate variability>.
- Observation 2: <e.g., Country Y displays the widest spread, suggesting heterogeneous solar profiles>.
- Observation 3: <e.g., ANOVA/Kruskal p-values indicate significant cross-country differences in GHI>.

5) Interactive Dashboard
- Location: app/main.py (Streamlit).
- Features:
  - Country multi-select, metric selector (GHI/DNI/DHI), side-by-side boxplot, and summary table.
  - Top regions table (auto-detects region column) ranked by average metric.
- How to run:
  - pip install streamlit pandas seaborn matplotlib
  - streamlit run app/main.py
- Screenshots: Save snapshots to dashboard_screenshots/ (e.g., dashboard_overview.png, boxplot_metric.png, top_regions.png).

6) Reproducibility
- Prerequisites: Python 3.x with pandas, seaborn, matplotlib, scipy, streamlit.
- Place cleaned CSVs under data/ with the exact names above (data/ is gitignored).
- Open and run compare_countries.ipynb; then launch the Streamlit app for interactive views.

7) Limitations and Next Steps
- Missing files will cause the notebook/app to skip a country. Ensure consistent schemas across CSVs.
- Future work: Add time/seasonality breakdowns, integrate geospatial layers, and deploy Streamlit to Community Cloud.

8) Repository Map
- compare_countries.ipynb – Cross-country analysis with plots, summary, and significance tests.
- app/ – Streamlit app (main.py, utils.py).
- dashboard_screenshots/ – Place PNGs used for submission.
- scripts/ – Helper scripts if needed.

Appendix: Statistical Testing Notes
- ANOVA assumptions: normality and homoscedasticity; Kruskal–Wallis is a non-parametric alternative.
- Interpret p-values in context and confirm with effect sizes.
