from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHECKPOINT_DIR = ROOT / "checkpoints"
THIRD_PARTY_DIR = ROOT / "third_party"

INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"

# Weights
DISNEY_CHECKPOINT = CHECKPOINT_DIR / "disney_stylegan_nada.pt"
E4E_CHECKPOINT = CHECKPOINT_DIR / "e4e_ffhq_encode.pt"

# Third-party repositories
STYLEGAN2_DIR = THIRD_PARTY_DIR / "stylegan2-pytorch"
E4E_DIR = THIRD_PARTY_DIR / "encoder4editing"