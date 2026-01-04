from .data_manager import DataManager
from .cleaner import TransactionCleaner
from .feature_builder import FeatureBuilder
from .risk_scorer import RiskScorer
from .transaction_flagger import TransactionFlagger
from .report_generator import ReportGenerator

class ConsoleApp:
    def __init__(self):
        self.data_manager = DataManager()
        self.cleaner = TransactionCleaner()
        self.feature_builder = FeatureBuilder()
        self.risk_scorer = RiskScorer()
        self.transaction_flagger = TransactionFlagger()
        self.report_generator = ReportGenerator()

        self.raw_df = None
        self.cleaned_df = None
        self.features_df = None
        self.scored_df = None
        self.flagged_df = None

        self.data_loaded = False
        self.cleaned = False
        self.features_built = False
        self.scored = False
        self.flagged = False

    def show_menu(self):
        print("\nBank Transaction Risk Analyzer")
        print("1. Load Data")
        print(f"2. Clean and validate data {'✔' if self.cleaned else ''}")
        print(f"3. Build features {'✔' if self.features_built else ''}")
        print(f"4. Score customers {'✔' if self.scored else ''}")
        print(f"5. Flag suspicious transactions {'✔' if self.flagged else ''}")
        print("6. Export reports")
        print("7. Display summary")
        print("0. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option: ")
            
            if choice == '1':
                path = input("Enter CSV path: ")
                self.raw_df = self.data_manager.load_csv(path)
                if self.raw_df is not None:
                    self.data_loaded = True
                    print("Data loaded successfully.")
            
            elif choice == '2':
                if not self.data_loaded:
                    print("Error: Please load data first (Option 1).")
                    continue
                self.cleaned_df = self.cleaner.clean(self.raw_df)
                self.cleaned = True
                print("Data cleaned successfully.")
                
            elif choice == '3':
                if not self.cleaned:
                    print("Error: Please clean data first (Option 2).")
                    continue
                self.features_df = self.feature_builder.build(self.cleaned_df)
                self.features_built = True
                print("Features built successfully.")

            elif choice == '4':
                if not self.features_built:
                    print("Error: Please build features first (Option 3).")
                    continue
                self.scored_df = self.risk_scorer.score(self.features_df)
                self.scored = True
                print("Customers scored successfully.")

            elif choice == '5':
                if not self.cleaned:
                    print("Error: Please clean data first (Option 2).")
                    continue
                self.flagged_df = self.transaction_flagger.flag(self.cleaned_df)
                self.flagged = True
                print("Suspicious transactions flagged successfully.")

            elif choice == '6':
                if not (self.flagged and self.scored):
                    print("Error: Please complete scoring and flagging (Options 4 & 5) first.")
                    continue
                self.report_generator.export(self.flagged_df, self.scored_df)
                print("Reports exported successfully.")

            elif choice == '7':
                if not self.scored:
                    print("Error: Nothing to summarize. Please score customers first.")
                    continue
                print("\n--- Summary ---")
                print(self.scored_df["risk_level"].value_counts())

            elif choice == '0':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")