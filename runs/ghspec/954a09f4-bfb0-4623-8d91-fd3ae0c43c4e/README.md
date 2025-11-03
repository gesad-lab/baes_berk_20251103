# Run Summary

**Run ID**: 954a09f4-bfb0-4623-8d91-fd3ae0c43c4e
**Framework**: ghspec
**Started**: 2025-10-29T19:33:46.417646Z
**Completed**: 2025-10-29T19:53:26.098973Z
**Duration**: 1179.68s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 180.99 |
| 2 | 2 | completed | 0/0 | 0 | 134.26 |
| 3 | 3 | completed | 0/0 | 0 | 209.40 |
| 4 | 4 | completed | 0/0 | 0 | 217.94 |
| 5 | 5 | completed | 0/0 | 0 | 167.86 |
| 6 | 6 | completed | 0/0 | 0 | 269.22 |

## Directory Structure

```
954a09f4-bfb0-4623-8d91-fd3ae0c43c4e/
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
