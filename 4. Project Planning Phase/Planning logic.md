# Planning Logic

## Methodology
- **Agile/Iterative:** Given the visual nature of the project, an iterative approach is best. We build the data foundation, create individual charts, assemble them into a dashboard, and then refine based on visual clarity and stakeholder feedback.

## Workflow
1. **Data Acquisition:** Download the finalized dataset from Kaggle.
2. **Data Ingestion & Review:** Connect the CSV to Tableau, review column headers, and validate data types.
3. **Data Preparation:** Rename fields and create necessary calculated fields (e.g., Price Difference).
4. **Visualization Generation:** Build the 8 specific charts (Avg Sales Volume vs Category, Consumer Demographics Donut, etc.) on individual worksheets.
5. **Dashboard Assembly:** Combine the 8 worksheets onto a single fixed-size dashboard. Implement the 3 interactive filters.
6. **Storyboarding:** Curate the 3 key insights into a Tableau Story presentation.
7. **Review & Finalization:** Validate that all metrics match expected values and design is responsive.

## Dependencies
- Visualization (Step 4) cannot begin until Data Preparation (Step 3) is fully complete and validated.
- Dashboard Assembly (Step 5) requires all 8 individual worksheets to be finalized.
- Storyboarding (Step 6) depends on insights discovered during the Dashboard Assembly.
