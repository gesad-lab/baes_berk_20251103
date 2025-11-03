# Run Summary

**Run ID**: b907e5c1-f0f6-4314-b5c9-d2bc35883874
**Framework**: ghspec
**Started**: 2025-10-28T22:08:01.597139Z
**Completed**: 2025-10-28T22:26:36.484851Z
**Duration**: 1114.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 263.92 |
| 2 | 2 | completed | 0/0 | 0 | 157.88 |
| 3 | 3 | completed | 0/0 | 0 | 291.57 |
| 4 | 4 | completed | 0/0 | 0 | 128.83 |
| 5 | 5 | completed | 0/0 | 0 | 147.60 |
| 6 | 6 | completed | 0/0 | 0 | 125.07 |

## Directory Structure

```
b907e5c1-f0f6-4314-b5c9-d2bc35883874/
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
