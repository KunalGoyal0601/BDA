import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "creadit_risk_fds" / "credit_risk_dataset.csv"
NOTEBOOKS = [
    ROOT / "creadit_risk_fds" / "creadit_risk_final.ipynb",
    ROOT / "creadit_risk_fds" / "creadit_risk_final_1.0.ipynb",
]

class DatasetSafetyTests(unittest.TestCase):
    def test_credit_risk_csv_is_not_bundled(self):
        self.assertFalse(DATA.exists())

    def test_credit_risk_notebooks_are_valid_and_use_local_data(self):
        for path in NOTEBOOKS:
            with self.subTest(notebook=path.name):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                source = "\n".join(
                    "".join(cell.get("source", []))
                    for cell in notebook["cells"] if cell.get("cell_type") == "code"
                )
                self.assertIn("DATA_PATH", source)
                self.assertIn("FileNotFoundError", source)
                self.assertIn("verify its license/terms", source)
                for cell in notebook["cells"]:
                    if cell.get("cell_type") == "code":
                        self.assertIsNone(cell.get("execution_count"))
                        self.assertFalse(cell.get("outputs"))

if __name__ == "__main__":
    unittest.main()
