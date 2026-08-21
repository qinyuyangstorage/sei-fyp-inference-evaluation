# SEI Chest X-Ray Report Generation: Inference Evaluation

Privacy-safe portfolio record of a Final Year Project evaluating the pretrained SEI model for chest X-ray report generation on an authorized MIMIC-CXR test split.

## Exact scope

This was an **inference-only reproduction using pretrained checkpoints**. It did not reproduce SEI training, pretraining, or the original data-preprocessing pipeline.

Completed work:

- configured the published SEI implementation and pretrained checkpoint;
- ran inference on approximately 3,850 authorized test samples;
- compared beam-search and temperature settings;
- evaluated BLEU, METEOR, ROUGE-L, CIDEr, and CheXbert;
- tested removal of similar historical cases;
- explored entity contributions and a simplified Grad-CAM-style visualization.

## Verified evaluation snapshot

The strongest recorded decoding configuration was `beam_size=3`, `temperature=1.0`:

| Metric | Recorded value |
|---|---:|
| Test samples | 3,851 |
| BLEU-4 | 0.1261 |
| METEOR | 0.1527 |
| ROUGE-L | 0.2895 |
| CIDEr | 0.1926 |
| CheXbert 5-label micro F1 | 0.5270 |

Removing similar historical cases reduced BLEU-4 to `0.0783`, CIDEr to `0.0861`, and CheXbert 5-label micro F1 to `0.3752` in the recorded run.

Run the aggregate result check:

```bash
python scripts/summarize_results.py
python scripts/validate_public_release.py
python -m pytest -q
```

## Interpretation limits

- RadGraph F1 was not reproduced because of library compatibility; historical zero values are not model-performance measurements.
- The Grad-CAM work was a simplified sequence-generation visualization, not a clinically validated explanation method.
- The recorded `sk_topk=1/3/5` rows are identical and are not presented as a validated ablation without a new parameter-propagation and cache-isolation run.
- Results come from one test split and are not evidence of clinical readiness.

## Why this repository contains aggregate results only

MIMIC-CXR images, reports, per-sample predictions, image identifiers, checkpoints, and embedded example reports are excluded. The complete historical working repository remains private because its Git history previously contained restricted per-sample outputs.

This public portfolio repository contains only aggregate metrics, a small results-analysis script, automated tests, and a release-safety check.

## Original model

K. Liu et al., “Structural Entities Extraction and Patient Indications Incorporation for Chest X-Ray Report Generation,” MICCAI 2024, DOI: `10.1007/978-3-031-72384-1_41`.

Academic evaluation only. This repository is not a medical device and must not be used for clinical diagnosis or patient care.
