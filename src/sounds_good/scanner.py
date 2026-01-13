"""Scanner for the "Sounds Good" metric.

Usage:
    from sounds_good.scanner import evaluate_all_runs
    evaluate_all_runs(Path('/path/to/baes_berk_20251214'))

This module inspects each run under the `runs` directory of the provided
base path, computes a boolean `sounds_good` according to a set of
conditions, and writes that boolean into the run's `metrics.json` file.
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess
from pathlib import Path
from typing import Dict, Optional, Tuple


def _read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def _find_db_file(run_path: Path) -> bool:
    # kept as a fallback; prefer running shell commands configured in commands.txt
    for p in run_path.rglob("*.db"):
        return True
    return False


def _count_py_files(search_root: Path) -> int:
    return sum(1 for _ in search_root.rglob("*.py"))


def _run_shell_command(cmd: str, cwd: Optional[Path] = None) -> Tuple[int, str, str]:
    try:
        # run with shell so complex grep/find pipelines are allowed
        p = subprocess.run(cmd, shell=True, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
        stdout = p.stdout.strip()
        stderr = p.stderr.strip()
        return p.returncode, stdout, stderr
    except Exception as e:
        return 1, "", str(e)


def _load_commands(cmd_file: Optional[Path] = None) -> Dict[str, str]:
    cmds: Dict[str, str] = {}
    if cmd_file is None:
        cmd_file = Path(__file__).resolve().parents[0] / "commands.txt"
    if not cmd_file.exists():
        return cmds
    for line in cmd_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            continue
        key, command = line.split("|", 1)
        cmds[key.strip()] = command.strip()
    return cmds


def _has_fastapi_import(search_root: Path) -> bool:
    pattern = re.compile(r"(^|\s)(from\s+fastapi\b|import\s+fastapi)", re.I | re.M)
    for py in search_root.rglob("*.py"):
        text = _read_text_safe(py)
        if pattern.search(text):
            return True
    return False


def _has_log_errors(search_root: Path) -> bool:
    """Return True if any `adapter.log` under `search_root` contains an ERROR level line.

    This is a Python fallback when the shell `HAS_CORRECT_LOGS` command is not configured.
    The shell command is expected to output a matching error line when an ERROR exists; the
    scanner interprets any non-empty output as indication of an error.
    """
    pattern = re.compile(r'"level"\s*:\s*"ERROR"')
    for log in search_root.rglob("**/adapter.log"):
        if not log.is_file():
            continue
        text = _read_text_safe(log)
        if pattern.search(text):
            return True
    return False


def _find_class_block(text: str, class_name: str) -> Optional[str]:
    # Rough extraction of class body using regex: from `class Name` to next `class` or end
    cls_re = re.compile(rf"^class\s+{re.escape(class_name)}\b[\s\S]*?(?=^class\s+|\Z)", re.M)
    m = cls_re.search(text)
    return m.group(0) if m else None


def _has_entity_with_field(search_root: Path, entity: str, field: str) -> bool:
    # Look for class definitions or model-like dicts that include the entity name and field
    class_pattern = re.compile(rf"class\s+{re.escape(entity)}\b", re.M)
    for py in search_root.rglob("*.py"):
        text = _read_text_safe(py)
        if class_pattern.search(text):
            block = _find_class_block(text, entity)
            if block and re.search(rf"\b{re.escape(field)}\b", block):
                return True
        # also allow simple definitions like Student = TypedDict(...) or pydantic BaseModel
        # fallback: file contains both entity and field tokens
        if entity in text and field in text:
            return True
    return False


def evaluate_run_path(run_path: Path) -> Dict[str, bool]:
    """Evaluate a single run directory and return a dict of condition booleans.

    Conditions checked:
    - has_db: any .db file present
    - has_fastapi: any .py imports fastapi
    - has_py_files: at least one .py file
    - has_student_with_email: `Student` entity that includes `email`
    - has_course: `Course` entity exists
    - has_teacher: `Teacher` entity exists
    - min_files_generated: at least 3 files present under managed_system or generated_artifacts
    - has_correct_logs: no `adapter.log` contains an ERROR-level line
    - sounds_good: logical AND of the above
    """
    ga = run_path / "generated_artifacts"
    search_root = ga if ga.exists() else run_path

    # load commands (shell-based checks) and run them where applicable
    cmds = _load_commands()
    # default fallbacks
    has_db = _find_db_file(run_path)
    py_count = _count_py_files(search_root)
    has_fastapi = _has_fastapi_import(search_root) if py_count > 0 else False
    files_generated = 0
    # internal: whether any ERROR-level lines were found in adapter.log
    log_errors_found = False

    # run shell commands where present
    if "HAS_DB" in cmds:
        cmd = cmds["HAS_DB"]
        rc, out, err = _run_shell_command(cmd, cwd=search_root)
        if out:
            has_db = bool(out)
        else:
            # fallback: python-based rglob that follows symlinks
            has_db = _find_db_file(search_root)
    if "PY_FILES_COUNT" in cmds:
        cmd = cmds["PY_FILES_COUNT"]
        rc, out, err = _run_shell_command(cmd, cwd=search_root)
        try:
            py_count = int(out.strip())
        except Exception:
            py_count = _count_py_files(search_root)
    has_py_files = py_count > 0
    if "HAS_FASTAPI" in cmds and has_py_files:
        cmd = cmds["HAS_FASTAPI"]
        rc, out, err = _run_shell_command(cmd, cwd=search_root)
        has_fastapi = bool(out)
    if "FILES_GENERATED_COUNT" in cmds:
        cmd = cmds["FILES_GENERATED_COUNT"]
        rc, out, err = _run_shell_command(cmd, cwd=search_root)
        try:
            files_generated = int(out.strip())
        except Exception:
            # fallback to python count
            managed = ga / "managed_system"
            if managed.exists():
                files_generated = sum(1 for _ in managed.rglob("*") if _.is_file())
            else:
                files_generated = sum(1 for _ in search_root.rglob("*") if _.is_file())

    # detect adapter.log ERROR lines: prefer shell command if provided, else fall back to Python search
    if "HAS_CORRECT_LOGS" in cmds:
        cmd = cmds["HAS_CORRECT_LOGS"]
        rc, out, err = _run_shell_command(cmd, cwd=search_root)
        # the shell command returns matching ERROR lines; non-empty output -> error present
        log_errors_found = bool(out and out.strip())
    else:
        log_errors_found = _has_log_errors(search_root)

    has_student_with_email = _has_entity_with_field(search_root, "Student", "email")
    has_course = _has_entity_with_field(search_root, "Course", "")
    has_teacher = _has_entity_with_field(search_root, "Teacher", "")

    min_files_generated = files_generated >= 3

    has_correct_logs = not log_errors_found

    sounds_good = all([
        has_db,
        has_fastapi,
        has_py_files,
        has_student_with_email,
        has_course,
        has_teacher,
        min_files_generated,
        has_correct_logs,
    ])

    return {
        "has_db": has_db,
        "has_fastapi": has_fastapi,
        "has_py_files": has_py_files,
        "has_student_with_email": has_student_with_email,
        "has_course": has_course,
        "has_teacher": has_teacher,
        "min_files_generated": min_files_generated,
        "has_correct_logs": has_correct_logs,
        "sounds_good": sounds_good,
        "files_generated_count": files_generated,
        "py_files_count": py_count,
    }


def _safe_write_json(path: Path, data: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def evaluate_all_runs(base_path: Path, repo_root: Optional[Path] = None, reload: bool = False) -> None:
    """Walk `base_path/runs/*/*` and update `metrics.json` in each run.

    Args:
        base_path: top-level path containing `runs` (e.g., /path/to/baes_berk_20251214)
        repo_root: optional repository root to check `config_sets/default/prompts`
    """
    base = Path(base_path)
    runs_dir = base / "runs"
    if not runs_dir.exists():
        raise FileNotFoundError(f"runs directory not found at {runs_dir}")

    # optionally inspect prompts for alignment
    prompts_ok = None
    try:
        if repo_root:
            prompts_dir = Path(repo_root) / "config_sets" / "default" / "prompts"
        else:
            # try to find config_sets relative to this package
            candidate = Path(__file__).resolve().parents[2] / "config_sets" / "default" / "prompts"
            prompts_dir = candidate

        if prompts_dir.exists():
            combined = "\n".join(_read_text_safe(p) for p in prompts_dir.glob("**/*") if p.is_file())
            tokens = ["database", "fastapi", "Student", "email", "Course", "Teacher", "files"]
            prompts_ok = all(tok.lower() in combined.lower() for tok in tokens)
        else:
            prompts_ok = False
    except Exception:
        prompts_ok = False

    for framework_dir in sorted(runs_dir.iterdir()):
        if not framework_dir.is_dir():
            continue
        for run_dir in sorted(framework_dir.iterdir()):
            if not run_dir.is_dir():
                continue
            metrics_path = run_dir / "metrics.json"
            if not metrics_path.exists():
                continue
            try:
                metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
            except Exception:
                metrics = {}
            # If SOUNDS_GOOD already present and reload==False, skip this run to save time
            existing = None
            try:
                existing = metrics.get("aggregate_metrics", {}).get("SOUNDS_GOOD")
            except Exception:
                existing = None
            if existing is not None and not reload:
                continue

            result = evaluate_run_path(run_dir)
            # write boolean only under aggregate_metrics (do NOT write top-level key)
            if "aggregate_metrics" not in metrics or not isinstance(metrics.get("aggregate_metrics"), dict):
                metrics["aggregate_metrics"] = metrics.get("aggregate_metrics", {}) or {}
            metrics["aggregate_metrics"]["SOUNDS_GOOD"] = bool(result.get("sounds_good"))
            # attach diagnostic details in a dedicated key (not top-level metric flag)
            metrics["sounds_good_details"] = result

            # write back
            try:
                metrics_path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False))
            except Exception:
                # silently ignore write errors in non-interactive runs
                pass

    # print short summary about prompts alignment
    # no interactive prints; function is silent


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compute Sounds Good metric for all runs")
    parser.add_argument("base_path", help="Path to top-level experiment (contains `runs`)")
    parser.add_argument("--repo-root", help="Optional repo root to inspect prompts", default=None)
    parser.add_argument("--reload", action="store_true", help="Recompute SOUNDS_GOOD even if already present in metrics.json")
    args = parser.parse_args()
    evaluate_all_runs(Path(args.base_path), repo_root=Path(args.repo_root) if args.repo_root else None, reload=bool(args.reload))
