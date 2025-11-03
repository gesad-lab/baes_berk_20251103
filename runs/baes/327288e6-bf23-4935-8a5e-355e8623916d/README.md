# Run Summary

**Run ID**: 327288e6-bf23-4935-8a5e-355e8623916d
**Framework**: baes
**Started**: 2025-10-31T04:34:18.544142Z
**Completed**: 2025-10-31T04:40:28.586043Z
**Duration**: 370.04s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 62.51 |
| 2 | 2 | completed | 0/0 | 0 | 63.37 |
| 3 | 3 | completed | 0/0 | 0 | 58.63 |
| 4 | 4 | completed | 0/0 | 0 | 61.94 |
| 5 | 5 | completed | 0/0 | 0 | 63.39 |
| 6 | 6 | completed | 0/0 | 0 | 60.19 |

## Directory Structure

```
327288e6-bf23-4935-8a5e-355e8623916d/
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
