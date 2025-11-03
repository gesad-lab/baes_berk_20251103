# Run Summary

**Run ID**: c5d2feca-f59a-4427-99d2-c32515ddacc6
**Framework**: baes
**Started**: 2025-10-30T00:04:14.347103Z
**Completed**: 2025-10-30T00:08:38.049707Z
**Duration**: 263.70s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 44.29 |
| 2 | 2 | completed | 0/0 | 0 | 40.40 |
| 3 | 3 | completed | 0/0 | 0 | 44.26 |
| 4 | 4 | completed | 0/0 | 0 | 38.63 |
| 5 | 5 | completed | 0/0 | 0 | 52.53 |
| 6 | 6 | completed | 0/0 | 0 | 43.59 |

## Directory Structure

```
c5d2feca-f59a-4427-99d2-c32515ddacc6/
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
