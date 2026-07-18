# User Acceptance Testing - Functional Specification Document (FSD)

## 1. Introduction
This document outlines the testing criteria designed to ensure the "Strategic Product Placement Analysis" dashboard meets the functional requirements specified by the stakeholders (Retail Managers, Merchandisers).

## 2. Test Environment
- **Platform:** Tableau Public (Embedded)
- **Browser:** Google Chrome (Version 115+)
- **Web Server:** Python Flask App (Localhost:5000)

## 3. Test Cases

### TC01: Verify Global Filters
- **Action:** Select "Aisle" from the Product Position filter.
- **Expected Result:** All 8 visualizations dynamically update to exclude "End-cap" and "Front of Store" data.
- **Pass/Fail:** PASS

### TC02: Verify Calculation Fields
- **Action:** Inspect the "Competitor Price vs Price" chart tooltips.
- **Expected Result:** Tooltips display the accurate aggregated average prices for both our store and competitors.
- **Pass/Fail:** PASS

### TC03: Verify Storyboard Navigation
- **Action:** Click through the 3 scenes in the Tableau Story container.
- **Expected Result:** The narrative progresses smoothly, highlighting "Clothing" and "Front of store" insights in scenes 1 through 3.
- **Pass/Fail:** PASS

### TC04: Verify Web Integration Layout
- **Action:** Open `http://127.0.0.1:5000` in the browser.
- **Expected Result:** The Bootstrap dark-themed UI loads, displaying the "SALES" navbar and accurately rendering the Tableau iframe without clipping the visualizations.
- **Pass/Fail:** PASS
