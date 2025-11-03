# Run Summary

**Run ID**: f47d09ee-aef5-43a2-b991-1c7d6b9ff7a2
**Framework**: baes
**Started**: 2025-10-30T09:23:59.704572Z
**Completed**: 2025-10-30T09:27:41.049131Z
**Duration**: 221.34s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 37.28 |
| 2 | 2 | completed | 0/0 | 0 | 42.28 |
| 3 | 3 | completed | 0/0 | 0 | 34.68 |
| 4 | 4 | completed | 0/0 | 0 | 36.01 |
| 5 | 5 | completed | 0/0 | 0 | 34.23 |
| 6 | 6 | completed | 0/0 | 0 | 36.86 |

## Directory Structure

```
f47d09ee-aef5-43a2-b991-1c7d6b9ff7a2/
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
