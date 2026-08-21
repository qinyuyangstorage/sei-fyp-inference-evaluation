from pathlib import Path

from scripts.summarize_results import load_rows


def test_aggregate_results_have_expected_baseline() -> None:
    rows = load_rows(Path("results/experiments_summary.csv"))
    beam3 = next(row for row in rows if row["experiment"] == "decoding_beam3")
    assert int(float(beam3["total_samples"])) == 3851
    assert round(float(beam3["BLEU_4"]), 4) == 0.1261
    assert round(float(beam3["chexbert_5_micro_f1"]), 3) == 0.527
