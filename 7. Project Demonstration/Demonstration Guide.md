# Project Demonstration & Publishing Guide

This guide provides instructions on how to publish the dashboard to Tableau Public and demonstrate it via the Flask web integration.

## 1. How to Save and Publish the Dashboard to Tableau Public
Follow these exact steps within Tableau Desktop to generate your embed codes:

1. **Publish to Public:** Click on **"File"** in the top-left corner of the Tableau window.
2. Select the **"Save to Tableau Public As..."** option. This will prompt a sign-in window.
3. **Sign In:** Enter your Tableau Public credentials (Email and Password) and click "Sign In".
4. **Enable Settings:** After signing in, the workbook will be published and displayed in your browser. Click on the **"Settings"** (gear icon) on the top right. Scroll down and ensure **"Show workbook sheets as tabs"** is enabled so all your dashboard and story sheets are visible.
5. **Generate Embed Code:** Click the **"Share"** icon (typically in the top right or bottom right of the viz). A window titled "Embed Code" will appear.
6. **Copy Code:** Click **"Copy Embed Code"** (the `<script>` snippet).
7. **Paste to Web App:** Open `5. Project Development Phase/templates/index.html` in a code editor and paste the copied embed code into the designated `[Paste Tableau Public Dashboard Embed Code Here]` placeholder.
8. Repeat steps 5-7 for each of the Story Scenes.

## 2. Setup the Web Environment
1. Open a terminal and navigate to the `5. Project Development Phase` folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 3. Run the Flask App
1. Run the application:
   ```bash
   python app.py
   ```
2. The server will start on `http://127.0.0.1:5000`.

## 4. Viewing the Dashboard
1. Open a web browser.
2. Navigate to `http://127.0.0.1:5000`.
3. The page will display the "SALES" Bootstrap template. Scroll down to see the embedded Tableau Public Dashboard and Stories.

## 5. Demonstration Talking Points
- **Scene 1:** Point out the "Avg Sales Volume vs Product Category" chart. Emphasize that *Clothing has the highest Average sales volume*.
- **Scene 2:** Show the "Foot Traffic vs Product Position" chart. Highlight that *Product position at the Front of store has high sales volume and high foot traffic*.
- **Scene 3:** Conclude that *The Product Category clothing at the front of the store has the highest avg sales volume*. 
- **Filters:** Demonstrate the interactive filters, showing how the entire dashboard recalculates live.
