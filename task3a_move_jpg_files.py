# Task Automation: Move all .jpg and .jpeg images into another folder.
# Change SOURCE_FOLDER to the folder containing your images.

from pathlib import Path
import shutil

SOURCE_FOLDER = Path("images_to_sort")
DESTINATION_FOLDER = Path("sorted_images")

if not SOURCE_FOLDER.exists():
    print(f"Folder '{SOURCE_FOLDER}' was not found.")
    print("Create this folder and place some .jpg or .jpeg images inside it.")
else:
    DESTINATION_FOLDER.mkdir(parents=True, exist_ok=True)
    moved_count = 0

    for file_path in SOURCE_FOLDER.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".jpg", ".jpeg"]:
            destination = DESTINATION_FOLDER / file_path.name

            # Avoid overwriting a file with the same name.
            if destination.exists():
                print(f"Skipped '{file_path.name}' because it already exists in destination.")
                continue

            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name}")
            moved_count += 1

    print(f"\nDone! {moved_count} image file(s) moved.")
