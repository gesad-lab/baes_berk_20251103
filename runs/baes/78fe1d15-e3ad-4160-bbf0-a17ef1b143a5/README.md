# Run Summary

**Run ID**: 78fe1d15-e3ad-4160-bbf0-a17ef1b143a5
**Framework**: baes
**Started**: 2025-10-31T02:10:59.185134Z
**Completed**: 2025-10-31T02:14:29.512381Z
**Duration**: 210.33s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 31.62 |
| 2 | 2 | completed | 0/0 | 0 | 34.12 |
| 3 | 3 | completed | 0/0 | 0 | 31.43 |
| 4 | 4 | completed | 0/0 | 0 | 37.08 |
| 5 | 5 | completed | 0/0 | 0 | 39.10 |
| 6 | 6 | completed | 0/0 | 0 | 36.97 |

## Directory Structure

```
78fe1d15-e3ad-4160-bbf0-a17ef1b143a5/
├── sprint_001/          # First sprint artifacts
│   ├── generated_artifacts/
│   ├── logs/
│   ├── metadata.json
│   └── validation.json
├── sprint_002/          # Second sprint artifacts
│   └── ...
├── final/               # Symlink to last successful sprint
└── metrics.json         # Run-level metrics (single source of truth)
```

## Accessing Results

### View final artifacts
```bash
cd final/generated_artifacts/managed_system/
```

### Compare sprints
```bash
diff -r sprint_001/generated_artifacts sprint_002/generated_artifacts
```

### View metrics (single source of truth)
```bash
cat metrics.json | jq
```

### Check specific sprint
```bash
cat sprint_001/metadata.json
```
