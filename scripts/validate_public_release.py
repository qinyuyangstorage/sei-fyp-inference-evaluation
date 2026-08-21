from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {"test_prediction.csv", "case.json", "test_small_50.json"}
FORBIDDEN_SUFFIXES = {".dcm", ".dicom", ".pth", ".pt", ".ckpt"}


def main() -> int:
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            violations.append(str(path.relative_to(ROOT)))
        if path.stat().st_size > 20 * 1024 * 1024:
            violations.append(f"{path.relative_to(ROOT)} (larger than 20 MB)")
    if violations:
        for violation in sorted(set(violations)):
            print(f"FORBIDDEN: {violation}")
        return 1
    print("Public-release validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
