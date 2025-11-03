# Run Summary

**Run ID**: bf63f3ca-6583-428a-a76f-cf9996b8ab11
**Framework**: baes
**Started**: 2025-10-31T03:42:27.044721Z
**Completed**: 2025-10-31T03:45:41.619176Z
**Duration**: 194.57s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 27.39 |
| 2 | 2 | completed | 0/0 | 0 | 29.62 |
| 3 | 3 | completed | 0/0 | 0 | 38.76 |
| 4 | 4 | completed | 0/0 | 0 | 33.88 |
| 5 | 5 | completed | 0/0 | 0 | 34.28 |
| 6 | 6 | completed | 0/0 | 0 | 30.63 |

## Directory Structure

```
bf63f3ca-6583-428a-a76f-cf9996b8ab11/
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
