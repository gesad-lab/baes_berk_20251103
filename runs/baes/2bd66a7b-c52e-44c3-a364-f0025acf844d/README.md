# Run Summary

**Run ID**: 2bd66a7b-c52e-44c3-a364-f0025acf844d
**Framework**: baes
**Started**: 2025-10-30T22:42:12.501541Z
**Completed**: 2025-10-30T22:45:52.838924Z
**Duration**: 220.34s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.15 |
| 2 | 2 | completed | 0/0 | 0 | 34.83 |
| 3 | 3 | completed | 0/0 | 0 | 35.08 |
| 4 | 4 | completed | 0/0 | 0 | 39.72 |
| 5 | 5 | completed | 0/0 | 0 | 39.50 |
| 6 | 6 | completed | 0/0 | 0 | 38.05 |

## Directory Structure

```
2bd66a7b-c52e-44c3-a364-f0025acf844d/
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
