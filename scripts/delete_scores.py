import os
import glob


def delete_csv_files(scores_folder):
    # Get all subdirectories inside the scores folder
    for subdir in os.listdir(scores_folder):
        subdir_path = os.path.join(scores_folder, subdir)

        # Check if it's a directory
        if os.path.isdir(subdir_path):
            # Find all CSV files in the subdirectory
            csv_files = glob.glob(os.path.join(subdir_path, "*.csv"))

            # Delete each CSV file
            for file in csv_files:
                try:
                    os.remove(file)
                    print(f"Deleted: {file}")
                except Exception as e:
                    print(f"Error deleting {file}: {e}")


if __name__ == "__main__":
    scores_folder = "../scores"  # Change this if needed
    delete_csv_files(scores_folder)