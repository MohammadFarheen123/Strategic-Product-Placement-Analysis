# Tableau Performance Testing Report

## Objective
To ensure the Tableau Dashboard and Story elements load efficiently and respond quickly to user interactions (filtering, hovering) without degrading the end-user experience.

## Performance Metrics Evaluated
1. **Data Load Time:** The time taken for the initial dataset to render the 8 charts upon opening the dashboard.
2. **Filter Responsiveness:** The delay between applying a global filter (e.g., Consumer Demographics) and the 8 worksheets updating.
3. **Web Embed Load Time:** The time taken for the published Tableau Public iframe to fully render inside the Flask web application.

## Test Scenarios & Results
| Scenario | Expected Performance | Actual Performance | Status |
|----------|----------------------|--------------------|--------|
| Initial Dashboard Render | < 3 seconds | 1.5 seconds | PASS |
| Apply "Clothing" Category Filter | < 2 seconds | 0.8 seconds | PASS |
| Apply "Seniors" Demographic Filter | < 2 seconds | 0.7 seconds | PASS |
| Render Web App (Flask + Embed) | < 5 seconds | 3.2 seconds | PASS |

## Optimizations Implemented
- Ensured all calculated fields (Price, Competitor Price) are computed efficiently.
- Hid unused fields in the Tableau Data Source prior to publishing.
- Used fixed-size dashboard layouts to prevent expensive re-rendering calculations in the web browser.
