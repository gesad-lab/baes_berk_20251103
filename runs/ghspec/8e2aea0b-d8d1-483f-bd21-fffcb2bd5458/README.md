# Run Summary

**Run ID**: 8e2aea0b-d8d1-483f-bd21-fffcb2bd5458
**Framework**: ghspec
**Started**: 2025-10-29T22:20:36.303075Z
**Completed**: 2025-10-29T22:38:32.340245Z
**Duration**: 1076.04s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 271.75 |
| 2 | 2 | completed | 0/0 | 0 | 169.45 |
| 3 | 3 | completed | 0/0 | 0 | 162.89 |
| 4 | 4 | completed | 0/0 | 0 | 181.89 |
| 5 | 5 | completed | 0/0 | 0 | 135.95 |
| 6 | 6 | completed | 0/0 | 0 | 154.11 |

## Directory Structure

```
8e2aea0b-d8d1-483f-bd21-fffcb2bd5458/
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
