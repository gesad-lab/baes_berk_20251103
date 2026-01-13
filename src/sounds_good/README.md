# sounds_good

Scanner for the "Sounds Good" metric.

Purpose
- Inspect each run under an experiment `runs/` tree and compute a boolean metric `SOUNDS_GOOD`.
- Write the boolean into each run's `metrics.json` under `aggregate_metrics.SOUNDS_GOOD` and store diagnostics under `sounds_good_details`.

Quick run (recommended)
- From the repository root run with `PYTHONPATH=src` so the package is importable.

Example (using environment variables):

```bash
export EXP_PATH=/home/vitor/Desktop/Dev/baes_berk_20251214
export REPO_ROOT=/home/vitor/Desktop/Dev/genai-devbench
PYTHONPATH=src python -m sounds_good.scanner "$EXP_PATH" --repo-root "$REPO_ROOT"
```

One-line (temporary):

```bash
EXP_PATH=/home/vitor/Desktop/Dev/baes_berk_20251214 REPO_ROOT=/home/vitor/Desktop/Dev/genai-devbench PYTHONPATH=src python -m sounds_good.scanner "$EXP_PATH" --repo-root "$REPO_ROOT"
```

Run a single run for inspection (prints JSON):

```bash
export RUN_PATH=/home/vitor/Desktop/Dev/baes_berk_20251214/runs/baes/<id>/sprint_002
PYTHONPATH=src python -c "from sounds_good.scanner import evaluate_run_path; from pathlib import Path, import json; print(json.dumps(evaluate_run_path(Path('$RUN_PATH')), indent=2))"
```

Notes about the `commands.txt` file
- `src/sounds_good/commands.txt` contains shell checks used by the scanner.
- Commands are executed with the run's `search_root` as the working directory, so commands should use `.` (dot) paths. Example:
  - `HAS_DB|(find . -type f -iname '*.db' -print -quit; grep -R -I -l '\.db' . 2>/dev/null) | head -n1`
  - This checks for both files with `.db` extension and files containing the ".db" string in their content
  - The content check is needed for cases where the database file is created only after the first execution (e.g., code that references "students.db" or configures a database path)
    - New: `HAS_CORRECT_LOGS|(grep -R '"level": "ERROR"' . --include="adapter.log" 2>/dev/null | head -n1)` can be added to detect ERROR-level lines in `adapter.log` files. The scanner exposes a single diagnostic boolean `has_correct_logs` in `sounds_good_details` — `True` means no ERROR lines were found, `False` means ERROR lines were detected. When present the scanner prefers this shell check; otherwise it falls back to a Python search.

  Commands (`commands.txt`)
  - `src/sounds_good/commands.txt` contains optional shell checks. Each line is `KEY|COMMAND` and commands run with the run's `search_root` as working directory.
  - Keys supported (examples):
    - `HAS_DB` — detect `.db` file presence (filesystem/content checks).
    - `PY_FILES_COUNT` — number of `.py` files under the run.
    - `HAS_FASTAPI` — grep check for `from fastapi` / `import fastapi`.
    - `FILES_GENERATED_COUNT` — count of generated files.
    - `HAS_CORRECT_LOGS` — grep for `"level": "ERROR"` in `adapter.log`. The command prints matching lines when an ERROR exists; the scanner treats any non-empty output as an ERROR indicator.

  Detection precedence
  - If a key exists in `commands.txt`, the scanner runs the shell command and prefers its output; otherwise a Python fallback (rglob + regex) is used.

  What the scanner checks (details)
  - `has_db`: True when a `.db` file is detected.
  - `has_fastapi`: True when FastAPI imports are found in `.py` files under the run. This explicitly documents the FastAPI check.
  - `has_py_files`: True when at least one `.py` file exists.
  - `has_student_with_email`: Best-effort detection of `Student` entity with `email`.
  - `has_course`, `has_teacher`: Best-effort detection for `Course` and `Teacher`.
  - `has_correct_logs`: True when no `adapter.log` contains `"level": "ERROR"` (shell command or Python fallback).
  - `min_files_generated`: True when at least 3 files were generated.

  Outputs written to `metrics.json`
  - `aggregate_metrics.SOUNDS_GOOD` (boolean) — primary aggregated flag.
  - `sounds_good_details` (object) — diagnostic dict containing checks above, e.g. `has_db`, `has_fastapi`, `has_py_files`, `has_student_with_email`, `has_course`, `has_teacher`, `min_files_generated`, `has_correct_logs`, `files_generated_count`, `py_files_count`.

Why you sometimes saw the RuntimeWarning when running the module
- Warning text: `'<module>' found in sys.modules after import of package 'sounds_good', but prior to execution of 'sounds_good.scanner'`.
- Cause: the package `sounds_good` previously imported the `scanner` submodule at package import time (in `__init__.py`). When Python runs `python -m sounds_good.scanner`, the package import step left an entry in `sys.modules` for `sounds_good.scanner` before runpy executed the module, causing the runtime warning.

How we fixed it
- `src/sounds_good/__init__.py` was changed to be a minimal package marker and no longer imports `scanner` on import. This prevents the double-import situation and removes the warning.

If you still see the warning
- It can appear if your interactive session already imported `sounds_good.scanner` before you run `python -m ...` (for example, in an active REPL). Restarting the shell/session or running the command in a fresh process avoids it.

Silencing logs / batch runs
- The scanner was made quiet for batch use (no per-run prints). If you need verbose debugging, temporarily run `evaluate_run_path()` for the specific run in Python and inspect returned diagnostics.

Default behavior when `metrics.json` already contains the metric
- By default the scanner will NOT re-compute or overwrite `aggregate_metrics.SOUNDS_GOOD` if that key already exists in the run's `metrics.json` — it skips that run to save time. This speeds up repeated runs when you only add new runs to the dataset.
- To force recomputation (re-run and overwrite existing values), pass the `--reload` flag:

```bash
PYTHONPATH=src python -m sounds_good.scanner "$EXP_PATH" --repo-root "$REPO_ROOT" --reload
```

Notes:
- Skipping is conservative: if you previously computed the metric and later change the scanner logic, use `--reload` to refresh all runs.
- The scanner writes `sounds_good_details` alongside `aggregate_metrics.SOUNDS_GOOD` when it computes a run.


