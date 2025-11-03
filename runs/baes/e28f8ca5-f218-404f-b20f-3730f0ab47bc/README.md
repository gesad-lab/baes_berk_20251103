# Run Summary

**Run ID**: e28f8ca5-f218-404f-b20f-3730f0ab47bc
**Framework**: baes
**Started**: 2025-10-31T00:06:30.166069Z
**Completed**: 2025-10-31T00:10:27.794249Z
**Duration**: 237.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 31.42 |
| 2 | 2 | completed | 0/0 | 0 | 44.28 |
| 3 | 3 | completed | 0/0 | 0 | 36.36 |
| 4 | 4 | completed | 0/0 | 0 | 47.64 |
| 5 | 5 | completed | 0/0 | 0 | 36.55 |
| 6 | 6 | completed | 0/0 | 0 | 41.37 |

## Directory Structure

```
e28f8ca5-f218-404f-b20f-3730f0ab47bc/
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
