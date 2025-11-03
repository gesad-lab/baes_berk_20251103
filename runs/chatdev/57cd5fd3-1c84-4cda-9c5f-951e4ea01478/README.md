# Run Summary

**Run ID**: 57cd5fd3-1c84-4cda-9c5f-951e4ea01478
**Framework**: chatdev
**Started**: 2025-10-30T19:15:46.204943Z
**Completed**: 2025-10-30T19:35:47.339009Z
**Duration**: 1201.13s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 235.52 |
| 2 | 2 | completed | 0/0 | 0 | 182.00 |
| 3 | 3 | completed | 0/0 | 0 | 145.14 |
| 4 | 4 | completed | 0/0 | 0 | 177.45 |
| 5 | 5 | completed | 0/0 | 0 | 230.39 |
| 6 | 6 | completed | 0/0 | 0 | 230.63 |

## Directory Structure

```
57cd5fd3-1c84-4cda-9c5f-951e4ea01478/
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
