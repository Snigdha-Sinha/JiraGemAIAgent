
import json
from pathlib import Path

class CodeUpdater:
    """
    """

    def __init__(self, answer) -> None:
        """
        """

        self.solutions = json.loads(answer)

    # File update
    def file_updater(self, file_location, file_data):
        """
        """
        if file_location.exists():
            with open(file_location, "w") as fw:
                fw.write(file_data)

    def file_creater(self, file_location, file_data):
        """
        """
        if not file_location.parent.exists():
            file_location.parent.mkdir(parents=True)
        with open(file_location, "w") as fw:
            fw.write(file_data)

    def file_deleter(self, file_location):
        """
        """
        if file_location.exists():
            # If the file exists, delete it
            file_location.unlink()
        
        are_files_exists = [item.is_file() for item in file_location.parent.iterdir()]

        if not any(are_files_exists):
            file_location.parent.rmdir()
	
    def update(self):
        """
        """

        for solution in self.solutions:
            if solution["to_update"]:
                self.file_updater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_create"]:
                self.file_creater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_delete"]:
                self.file_deleter(
                    file_location=Path(solution["file_location"])
                )
