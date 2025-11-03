# Run Summary

**Run ID**: 7b4cf8e2-4c8d-440f-a8b0-41ac41fb249a
**Framework**: ghspec
**Started**: 2025-10-30T15:39:50.261860Z
**Completed**: 2025-10-30T16:01:45.378586Z
**Duration**: 1315.12s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 234.94 |
| 2 | 2 | completed | 0/0 | 0 | 234.63 |
| 3 | 3 | completed | 0/0 | 0 | 125.10 |
| 4 | 4 | completed | 0/0 | 0 | 196.86 |
| 5 | 5 | completed | 0/0 | 0 | 138.51 |
| 6 | 6 | completed | 0/0 | 0 | 385.09 |

## Directory Structure

```
7b4cf8e2-4c8d-440f-a8b0-41ac41fb249a/
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
