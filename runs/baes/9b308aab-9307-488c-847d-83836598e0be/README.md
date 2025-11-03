# Run Summary

**Run ID**: 9b308aab-9307-488c-847d-83836598e0be
**Framework**: baes
**Started**: 2025-10-29T01:03:56.829148Z
**Completed**: 2025-10-29T01:06:33.769465Z
**Duration**: 156.94s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 23.24 |
| 2 | 2 | completed | 0/0 | 0 | 27.73 |
| 3 | 3 | completed | 0/0 | 0 | 23.07 |
| 4 | 4 | completed | 0/0 | 0 | 26.24 |
| 5 | 5 | completed | 0/0 | 0 | 27.93 |
| 6 | 6 | completed | 0/0 | 0 | 28.72 |

## Directory Structure

```
9b308aab-9307-488c-847d-83836598e0be/
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
