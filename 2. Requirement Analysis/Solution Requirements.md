# Solution Requirements

## Functional Requirements
* **Data Integration:** The system shall import the `Product Positioning.csv` dataset accurately.
* **Calculated Fields:** The system must utilize the following calculation fields:
  1. Price
  2. Competitors Price
  3. Sales Volume
* **Dashboard Visualizations (8 Graphs):** The system shall generate:
  1. Avg Sales Volume vs Product Category
  2. Avg Sales Volume by Product Category on Sales
  3. Consumer Demographics vs Product Category
  4. Foot traffic vs Sales Volume
  5. Competitors Price vs Price
  6. Promotion of Product Category on Price and Sales Volume
  7. Product Category vs Price
  8. Avg Sales Volume by Product Category by Product Position
* **Interactivity (Utilization of Filters):** The dashboard must include global filters that dynamically refine specific subsets of data relevant to the analysis objectives.
* **Web Integration:** The system shall embed the interactive Tableau Dashboard and Story into a Flask-based website or web application, allowing users to explore data directly within a web UI.
* **Publishing:** The dashboard must be published to Tableau Public to generate the necessary share/embed links.

## Non-Functional Requirements
* **Performance:** The Tableau dashboard should load smoothly in the web browser.
* **Usability:** The Flask UI must be clean and focus entirely on the embedded visualization experience.
* **Accessibility:** Embedding the dashboard ensures accessibility for stakeholders without Tableau licenses.
