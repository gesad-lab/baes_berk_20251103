# Run Summary

**Run ID**: 2d4d489d-a943-4682-aac6-8c2034f1949a
**Framework**: baes
**Started**: 2025-10-30T16:01:45.828447Z
**Completed**: 2025-10-30T16:05:57.748967Z
**Duration**: 251.92s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 44.85 |
| 2 | 2 | completed | 0/0 | 0 | 37.72 |
| 3 | 3 | completed | 0/0 | 0 | 42.55 |
| 4 | 4 | completed | 0/0 | 0 | 40.78 |
| 5 | 5 | completed | 0/0 | 0 | 51.70 |
| 6 | 6 | completed | 0/0 | 0 | 34.30 |

## Directory Structure

```
2d4d489d-a943-4682-aac6-8c2034f1949a/
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
