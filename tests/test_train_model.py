
from pathlib import Path
import sys

# Make the project root importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from notebooks.train_model import main


def test_model_training():
    accuracy = main()

    assert 0.0 <= accuracy <= 1.0
    assert accuracy >= 0.80
