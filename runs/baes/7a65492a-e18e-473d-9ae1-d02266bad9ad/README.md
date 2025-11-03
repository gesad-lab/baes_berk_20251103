# Run Summary

**Run ID**: 7a65492a-e18e-473d-9ae1-d02266bad9ad
**Framework**: baes
**Started**: 2025-10-31T18:01:23.487410Z
**Completed**: 2025-10-31T18:04:31.002583Z
**Duration**: 187.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.88 |
| 2 | 2 | completed | 0/0 | 0 | 29.99 |
| 3 | 3 | completed | 0/0 | 0 | 30.57 |
| 4 | 4 | completed | 0/0 | 0 | 34.62 |
| 5 | 5 | completed | 0/0 | 0 | 28.40 |
| 6 | 6 | completed | 0/0 | 0 | 29.04 |

## Directory Structure

```
7a65492a-e18e-473d-9ae1-d02266bad9ad/
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
