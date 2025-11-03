# Run Summary

**Run ID**: 950a01fa-93e7-4cb1-9f51-cd1c1f5e0563
**Framework**: ghspec
**Started**: 2025-10-30T14:45:13.609580Z
**Completed**: 2025-10-30T15:08:03.033255Z
**Duration**: 1369.42s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 239.68 |
| 2 | 2 | completed | 0/0 | 0 | 130.89 |
| 3 | 3 | completed | 0/0 | 0 | 189.67 |
| 4 | 4 | completed | 0/0 | 0 | 366.63 |
| 5 | 5 | completed | 0/0 | 0 | 190.32 |
| 6 | 6 | completed | 0/0 | 0 | 252.21 |

## Directory Structure

```
950a01fa-93e7-4cb1-9f51-cd1c1f5e0563/
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
