# Run Summary

**Run ID**: fa06fd9c-192c-4654-b02c-ffa73aed6b59
**Framework**: chatdev
**Started**: 2025-10-29T16:50:08.846730Z
**Completed**: 2025-10-29T17:15:41.251854Z
**Duration**: 1532.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 217.80 |
| 2 | 2 | completed | 0/0 | 0 | 278.75 |
| 3 | 3 | completed | 0/0 | 0 | 329.52 |
| 4 | 4 | completed | 0/0 | 0 | 275.43 |
| 5 | 5 | completed | 0/0 | 0 | 208.88 |
| 6 | 6 | completed | 0/0 | 0 | 222.02 |

## Directory Structure

```
fa06fd9c-192c-4654-b02c-ffa73aed6b59/
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
