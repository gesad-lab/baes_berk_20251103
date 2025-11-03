# Run Summary

**Run ID**: 46216546-7a7a-4d3d-8192-5f5590130a51
**Framework**: baes
**Started**: 2025-10-29T07:56:31.170324Z
**Completed**: 2025-10-29T08:00:01.135189Z
**Duration**: 209.96s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.91 |
| 2 | 2 | completed | 0/0 | 0 | 36.13 |
| 3 | 3 | completed | 0/0 | 0 | 39.14 |
| 4 | 4 | completed | 0/0 | 0 | 33.80 |
| 5 | 5 | completed | 0/0 | 0 | 34.21 |
| 6 | 6 | completed | 0/0 | 0 | 32.76 |

## Directory Structure

```
46216546-7a7a-4d3d-8192-5f5590130a51/
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
