# Run Summary

**Run ID**: 5f481a77-b1ab-4e80-b13a-6cf75cdef632
**Framework**: ghspec
**Started**: 2025-10-29T21:37:25.068036Z
**Completed**: 2025-10-29T21:55:44.478993Z
**Duration**: 1099.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 276.28 |
| 2 | 2 | completed | 0/0 | 0 | 186.52 |
| 3 | 3 | completed | 0/0 | 0 | 251.00 |
| 4 | 4 | completed | 0/0 | 0 | 120.09 |
| 5 | 5 | completed | 0/0 | 0 | 139.45 |
| 6 | 6 | completed | 0/0 | 0 | 126.06 |

## Directory Structure

```
5f481a77-b1ab-4e80-b13a-6cf75cdef632/
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
