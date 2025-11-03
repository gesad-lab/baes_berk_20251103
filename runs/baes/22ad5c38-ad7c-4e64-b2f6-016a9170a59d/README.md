# Run Summary

**Run ID**: 22ad5c38-ad7c-4e64-b2f6-016a9170a59d
**Framework**: baes
**Started**: 2025-10-30T17:51:23.877087Z
**Completed**: 2025-10-30T17:55:17.630033Z
**Duration**: 233.75s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 35.65 |
| 2 | 2 | completed | 0/0 | 0 | 52.34 |
| 3 | 3 | completed | 0/0 | 0 | 39.21 |
| 4 | 4 | completed | 0/0 | 0 | 30.89 |
| 5 | 5 | completed | 0/0 | 0 | 33.04 |
| 6 | 6 | completed | 0/0 | 0 | 42.61 |

## Directory Structure

```
22ad5c38-ad7c-4e64-b2f6-016a9170a59d/
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
