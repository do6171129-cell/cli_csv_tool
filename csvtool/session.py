from csvtool.loader import load_csv
from csvtool.filtering import apply_filter
from csvtool.sorter import apply_sort
from csvtool.export import export_csv

class CSVSession:
    def __init__(self):
        self.original_rows = None
        self.current_rows = None
        self.columns = None
        self.current_path = None

    def is_loaded(self):
        return self.original_rows is not None

    def load(self, path):
        rows, cols = load_csv(path)

        self.original_rows = rows
        self.current_rows = rows.copy()
        self.columns = cols
        self.current_path = path

    def count(self):
        if self.current_rows is None:
            raise RuntimeError("CSV not loaded")
        return len(self.current_rows)

    def filter(self, cond: dict) -> None:
        if not self.is_loaded():
            raise RuntimeError("CSV not loaded")
        self.current_rows = apply_filter(self.current_rows, cond)

    def sort(self, spec: dict) -> None:
        if not self.is_loaded():
            raise RuntimeError("CSV not loaded")
        self.current_rows = apply_sort(self.current_rows, spec)

    def reset(self):
        if not self.is_loaded():
            raise RuntimeError("CSV not loaded")
        self.current_rows = self.original_rows.copy()

    def export(self, path):
        if not self.is_loaded():
            raise RuntimeError("CSV not loaded")
        export_csv(self.current_rows, path, self.columns)


