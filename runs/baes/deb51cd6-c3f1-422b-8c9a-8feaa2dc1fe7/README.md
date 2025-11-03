# Run Summary

**Run ID**: deb51cd6-c3f1-422b-8c9a-8feaa2dc1fe7
**Framework**: baes
**Started**: 2025-10-28T15:34:09.796364Z
**Completed**: 2025-10-28T15:37:46.072162Z
**Duration**: 216.28s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.40 |
| 2 | 2 | completed | 0/0 | 0 | 21.79 |
| 3 | 3 | completed | 0/0 | 0 | 52.66 |
| 4 | 4 | completed | 0/0 | 0 | 37.44 |
| 5 | 5 | completed | 0/0 | 0 | 38.45 |
| 6 | 6 | completed | 0/0 | 0 | 45.53 |

## Directory Structure

```
deb51cd6-c3f1-422b-8c9a-8feaa2dc1fe7/
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
