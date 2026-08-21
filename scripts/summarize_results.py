from __future__ import annotations

import csv
from pathlib import Path


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    rows = load_rows(Path("results/experiments_summary.csv"))
    decoding = [row for row in rows if row["experiment"].startswith("decoding_")]
    best = max(decoding, key=lambda row: float(row["BLEU_4"]))
    no_cases = next(row for row in rows if row["experiment"] == "ablation_no_sk")
    print(f"best_decoding={best['experiment']}")
    print(f"samples={int(float(best['total_samples']))}")
    print(f"bleu4={float(best['BLEU_4']):.4f}")
    print(f"rouge_l={float(best['ROUGE_L']):.4f}")
    print(f"cider={float(best['CIDEr']):.4f}")
    print(f"chexbert_5_micro_f1={float(best['chexbert_5_micro_f1']):.4f}")
    print(f"no_similar_cases_bleu4={float(no_cases['BLEU_4']):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
