from database.runtime import DataBase
from models.runtime import PredictedLoadModel

def main():
    # Initialize database
    db = DataBase()

    try:
        # Connect to the database
        db.connect()

        # Ensure collections are clean before starting
        db.delete_collection("Wooster")
        db.models.delete_collection()

        # Create collection for Wooster node and import CSV data
        db.create_collection("Wooster", "Wooster_Data")

        # Initialize and train prediction model
        model = PredictedLoadModel(db, "Wooster")
        model.train()

        # Test predictions with sample dates
        test_dates = [
            (2022, 11, 7, 0, "November 7, 2022"),
            (2022, 7, 14, 20, "July 14, 2022"),
        ]

        for year, month, day, hour, label in test_dates:
            print(label)
            print(model.predict_weekly_loads(year, month, day, hour))

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up database
        db.delete_collection("Wooster")
        db.models.delete_collection()
        print("Database cleaned up successfully.")

if __name__ == "__main__":
    main()
