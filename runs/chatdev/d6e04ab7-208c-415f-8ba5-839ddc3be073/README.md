# Run Summary

**Run ID**: d6e04ab7-208c-415f-8ba5-839ddc3be073
**Framework**: chatdev
**Started**: 2025-10-28T15:37:49.941811Z
**Completed**: 2025-10-28T16:00:52.349494Z
**Duration**: 1382.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 241.00 |
| 2 | 2 | completed | 0/0 | 0 | 180.39 |
| 3 | 3 | completed | 0/0 | 0 | 231.79 |
| 4 | 4 | completed | 0/0 | 0 | 225.54 |
| 5 | 5 | completed | 0/0 | 0 | 239.89 |
| 6 | 6 | completed | 0/0 | 0 | 263.78 |

## Directory Structure

```
d6e04ab7-208c-415f-8ba5-839ddc3be073/
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
