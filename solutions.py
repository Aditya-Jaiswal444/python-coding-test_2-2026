'''
❗ Q1: Workforce Stability Index

A company tracks employees across multiple projects over time. Each project assigns a performance score, but employees may appear multiple times in different projects and months.

You must compute a stability index for each employee based on their performance consistency and return a ranked list of employees.

 Q2: Fraud Pattern Detection Engine

A banking system records transaction logs for multiple users over time.

Each user may perform multiple transactions in a day. Some patterns indicate suspicious behavior based on frequency and repetition trends.

Your task is to analyze the dataset and classify users into normal or suspicious categories.
 Q3: Smart Inventory Drift Analyzer

A warehouse system logs continuous stock movements including additions, removals, and corrections.

Due to system delays, logs may not be in chronological order.

Your task is to determine the final correct inventory state and detect inconsistencies in movement patterns.

 Q4: Customer Engagement Ranking System

A digital platform tracks different types of user interactions such as clicks, views, purchases, and shares.

Each interaction contributes differently to engagement, and weights may vary over time.

Your task is to compute a dynamic engagement score and generate a sorted ranking of users.

 Q5: Multi-Zone Delivery Feasibility Engine

A logistics company assigns delivery tasks across multiple zones with constraints like time windows, capacity limits, and priority levels.

Not all requests can be fulfilled due to overlapping constraints.

Your task is to determine which deliveries can be successfully completed and which must be rejected.
'''

# Q1: Workforce Stability IndexGoal:
# Calculate how consistent an employee's performance is across different projects and months, then rank them. 
# Less variation means higher stability.Step-by-Step AlgorithmGather the Data:
# Create a list of all raw records. Each record should contain: Employee ID, Project ID, Month, and Performance Score
# Group by Employee: Create an empty dictionary (map).
# Loop through the records and group all Performance Scores under their respective Employee ID.
# Filter Active Employees: Loop through each employee.
# Check if they have enough data points (e.g., at least 3 scores). 
# If they do not, skip them or mark them as "Insufficient Data".
# Calculate Average Score: For each valid employee, sum all of their performance scores and divide by the total number of scores to get their Average Score.
# Calculate Variance (Consistency):For each score belonging to an employee, subtract the Average Score and square the result: (Score - Average)².Sum all of these squared values together.
# Divide this sum by the total number of scores. This result is the Variance.Compute Stability Index:A high variance means low stability. 
# To reverse this, use a formula like:Stability Index = 1 / (1 + Variance).
# Rank the Workforce: Collect all pairs of [Employee ID, Stability Index]. 
# Sort this list in descending order (highest stability index first).
# Output: Return the sorted ranking list.


# Q2: Fraud Pattern Detection EngineGoal:
#  Flag bank users as "Suspicious" if they execute too many rapid transactions or repeat identical actions in a short window.
# Step-by-Step AlgorithmGroup by User and Day:
#  Create a dictionary. 
# Filter the transaction logs so you group all transaction records by User ID and specific Date.
# Sort Chronologically: For every user on a specific day, sort their transactions by their exact Timestamp from earliest to latest.
# Initialize Fraud Flags: Set a default status for each user as "Normal".
# Define Threshold Limits: Set hard limits for rules (e.g., Max Transactions Per Minute = 5, Max Identical Amounts within 10 mins = 3).
# Analyze Frequency (Velocity Rule):Use a sliding time window. For every transaction, count how many other transactions occur within the next 60 seconds.
# If this count exceeds your threshold, change the user's status to "Suspicious".Analyze Repetition (Duplicate Rule):Look at consecutive transactions.
#  If a user repeats the exact same Transaction Amount multiple times within a short window, increase a suspicion counter.
# If the counter hits the threshold, change the status to "Suspicious".
# Output: Return a final list mapping every User ID to either "Normal" or "Suspicious".




# Q3: Smart Inventory Drift AnalyzerGoal:
#  Figure out the actual final stock of warehouse items when logs arrive out of chronological order, and flag negative stock errors.
# Step-by-Step AlgorithmSort the Logs: Take the chaotic list of inventory logs. 
# Sort the entire dataset globally by the actual Log Timestamp, not the time the system received them.
# Initialize Tracking Objects: Create two blank dictionaries:Current Stock: 
# Maps an Item ID to its running balance (starts at 0).
# Inconsistencies: Maps an Item ID to a list of error messages.
# Process Movements Step-by-Step: Loop through the sorted, chronological logs one by one:Identify the Item ID, Movement Type (Addition, Removal, Correction), and Quantity.
# If Addition: Add the quantity to Current Stock[Item ID].
# If Removal: Subtract the quantity from Current Stock[Item ID].
# If Correction: Overwrite Current Stock[Item ID] with this new physical count quantity.
# Detect Drift/Inconsistencies: Immediately after any subtraction or correction step, check if Current Stock[Item ID] drops below zero.
# If it goes negative, log an error in Inconsistencies (e.g., "Item X dropped to -5 on Timestamp Y").
# Output: Return the final Current Stock values along with the Inconsistencies log for auditing




# Q4: Customer Engagement Ranking SystemGoal:
#  Score and rank users based on their interactions (clicks, shares, purchases), accounting for the fact that weights change over time.
# Step-by-Step AlgorithmDefine Weight Maps: Create a configuration table that holds weights for each action type per time period (e.g., January: Click = 1, Purchase = 10; February: Click = 1, Purchase = 15).
# Initialize Scores: Create an empty dictionary called User Scores where every User ID starts with a balance of 0.
# Calculate Weighted Points: Loop through every interaction in the database:Look up the User ID, Interaction Type, and the Date.
# Find the matching weight from your configuration table based on that specific Date and Interaction Type.
# Add that weight value directly to the user's running total in User Scores.Apply Decay (Optional): 
# If older interactions should matter less than recent ones, multiply past scores by a decay factor (like 0.95) for every week that passes.
# Sort the Rankings: Convert your User Scores dictionary into a list of pairs: [User ID, Total Score]. Sort this list in descending order based on the Total Score.
# Output: Output the sorted list as the master user engagement leaderboard.



# Q5: Multi-Zone Delivery Feasibility EngineGoal:
#  Maximize delivery fulfillment across multiple areas while filtering out tasks that violate delivery time windows, capacity limits, or priorities.
# Step-by-Step AlgorithmStructure the Rules:
#  Organize your data into two sets:
# Zones: Each zone has a Driver Capacity (max orders it can take) and available Operating Hours.
# Delivery Tasks: Each task has a Zone ID, Time Window (e.g., 2 PM - 4 PM), Package Volume, and Priority Level (High/Medium/Low).
# Prioritize the Workload:
#  Sort all incoming delivery tasks using two sorting levels:
# Primary sort: Priority Level (High priority comes first).
# Secondary sort: Time Window End (Earliest deadline comes first).Initialize Trackers: For each delivery zone, initialize a Used Capacity = 0 counter and a Driver Schedule timeline.
# Evaluate Feasibility (Loop through sorted tasks):For each task, check its designated delivery zone.Constraint Check 1 (Capacity): Does adding this task's Package Volume exceed the zone's Driver Capacity? 
# If yes, reject the task as Infeasible.Constraint Check 2 (Time Window): Can a driver reach this address during its requested Time Window without overlapping or violating previous accepted schedules? 
# If no, reject the task.Allocate Valid Tasks: If the task passes both constraint checks:Add the task to the zone's accepted list.Increase the zone's Used Capacity by the task's volume.Lock in the time slot on the zone's Driver Schedule.
# Output: Return a list of "Accepted Deliveries" grouped by zone, alongside a list of "Rejected Deliveries" detailing which constraint caused the failure.
































