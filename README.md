Banking Risk & Fraud Analyzer
A simple tool to find "weird" or "risky" customers in banking data using math and statistics.

What this project does
This app takes a list of thousands of bank transactions and:

1-Cleans the data to remove mistakes.

2-Groups transactions by customer so we can see their behavior.

3-Scores every customer to find who is spending an unusual amount of money.

4-Flags specific suspicious transactions (like very large transfers).

5-Saves the results into reports you can open in Excel.

How the code is organized
The project is built like a modular factory. Each piece does one job:

data_manager.py: Reads the CSV file.

cleaner.py: Fixes errors and removes duplicates.

feature_builder.py: Calculates totals for each customer.

risk_scorer.py: Uses math (Z-Scores) to decide who is risky.

transaction_flagger.py: Spots single suspicious transactions.

report_generator.py: Creates the final files.

console_app.py: Shows the menu and controls the flow.

The Math (Simply Explained)
We use a statistical method called the Z-Score.

Instead of guessing what a "large" amount is, the app calculates the average spending. If a customer is 3 steps (standard deviations) away from the average, they are flagged as Critical Risk because their behavior is mathematically rare.

How to use it
Start the app: Run python main.py.

Follow the steps (1 to 7):

Step 1: Give it the location of your data file.

Step 2-5: Press the numbers in order to process the data. (The app won't let you skip steps!)

Step 6: Save your reports to the reports/ folder.

Step 7: See a quick summary of the risk levels in your console.

Final Reports
After you finish, you will find 3 files in the reports folder:

customer_risk_summary.csv: A list of every customer and their risk level (Low, Medium, High, or Critical).

flagged_transactions.csv: A list of only the "red flag" transactions.

report.txt: A short summary of the whole analysis.