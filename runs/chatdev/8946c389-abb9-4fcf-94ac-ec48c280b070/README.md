# Run Summary

**Run ID**: 8946c389-abb9-4fcf-94ac-ec48c280b070
**Framework**: chatdev
**Started**: 2025-10-30T08:44:23.839754Z
**Completed**: 2025-10-30T09:06:42.038214Z
**Duration**: 1338.20s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 220.87 |
| 2 | 2 | completed | 0/0 | 0 | 220.65 |
| 3 | 3 | completed | 0/0 | 0 | 295.19 |
| 4 | 4 | completed | 0/0 | 0 | 600.02 |
| 5 | 5 | completed | 0/0 | 0 | 0.71 |
| 6 | 6 | completed | 0/0 | 0 | 0.75 |

## Directory Structure

```
8946c389-abb9-4fcf-94ac-ec48c280b070/
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
