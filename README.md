# Marketing-Analytics

## Problem Statement

Marketing Analytics Dashboard was developed using BigQuery, REST API, Python and Power BI to analyze campaign performance, customer engagement and sentiments.
The client, experienced declining customer engagement and conversion rates despite increased marketing budgets. The marketing and customer experience teams sought insights to:
1.	Identify gaps in customer behavior and journeys.
2.	Evaluate campaign performance.
3.	Analyze customer sentiment from reviews and feedback to improve satisfaction.

### Steps followed 

- Step 1: Data Preparation
•	Optimized Customer, Products, Engagement, and Journey tables in BigQuery using SQL views to enhance query performance and scalability.

- Step 2: Sentiment Analysis with Python
•	Extracted Customer Reviews data from SuiteCRM via REST API.
•	Performed Sentiment Analysis using VADER (NLTK) in Python and categorized reviews into positive, negative, mixed, and neutral sentiments.
•	Loaded the results back into BigQuery for further processing.

- Step 3: Dashboard Development in Power BI
•	Imported all datasets and performed data modeling in Power BI, including relationships and calculated measures using DAX formulas.
•	Designed 4 tabs addressing:
1.	Executive Summary—Displayed KPIs such as top products, regions, and customer satisfaction ratings.
2.	Campaign Performance—Tracked CTR, impressions, and conversions over time.
3.	Customer Segmentation—Categorized customers by engagement scores.
4.	Sentiment Analysis—Showcased customer sentiment trends and common issues.

- Step 4: Optimization and Testing
•	Optimized load times by pre-aggregating data in BigQuery and using DirectQuery mode in Power BI.
•	Conducted rigorous testing to ensure data accuracy, refresh schedules, and visual consistency.

### Marketing Analytics Dashboard:
![Image](https://github.com/user-attachments/assets/dc896b04-f91c-4a8a-908c-7148ccb5b2bf)
![Image](https://github.com/user-attachments/assets/45f9c341-391b-4edb-b26b-faed25909703)
![Image](https://github.com/user-attachments/assets/b69b13b1-b950-44e2-af09-aa52ef0e4eb8)
![Image](https://github.com/user-attachments/assets/4a015103-3f46-4a23-a206-c2466301874f)

### Analysis:
![Image](https://github.com/user-attachments/assets/64746718-1e8c-4ce1-b940-84ebdd9b0a80)
![Image](https://github.com/user-attachments/assets/26e8b1f7-8672-4fe8-a702-03432e3f3d15)
![Image](https://github.com/user-attachments/assets/8880911d-4c0d-4797-9cc8-1a446a74c0ee)
![Image](https://github.com/user-attachments/assets/86f4aed7-8cbf-4c04-9a6a-a2a586dddc70)
![Image](https://github.com/user-attachments/assets/9813fa90-d779-4142-92b4-d12c12ff8301)

### Result:
•	500 more targeted customer interactions, leading to improved marketing ROI and better personalization strategies.

•	Reduced manual reporting efforts by 80% with automated workflows and real-time updates.

•	Stakeholders gained actionable insights into campaigns, enabling faster decision-making and higher engagement rates.


