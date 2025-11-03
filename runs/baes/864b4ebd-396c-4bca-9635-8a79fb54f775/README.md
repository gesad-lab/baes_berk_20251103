# Run Summary

**Run ID**: 864b4ebd-396c-4bca-9635-8a79fb54f775
**Framework**: baes
**Started**: 2025-10-29T03:05:26.009768Z
**Completed**: 2025-10-29T03:07:40.747147Z
**Duration**: 134.74s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 24.55 |
| 2 | 2 | completed | 0/0 | 0 | 20.17 |
| 3 | 3 | completed | 0/0 | 0 | 20.80 |
| 4 | 4 | completed | 0/0 | 0 | 22.46 |
| 5 | 5 | completed | 0/0 | 0 | 24.05 |
| 6 | 6 | completed | 0/0 | 0 | 22.70 |

## Directory Structure

```
864b4ebd-396c-4bca-9635-8a79fb54f775/
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
