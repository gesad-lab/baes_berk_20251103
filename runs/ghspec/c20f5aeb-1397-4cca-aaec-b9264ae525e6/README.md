# Run Summary

**Run ID**: c20f5aeb-1397-4cca-aaec-b9264ae525e6
**Framework**: ghspec
**Started**: 2025-10-29T00:49:46.430623Z
**Completed**: 2025-10-29T01:03:54.573321Z
**Duration**: 848.14s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 160.67 |
| 2 | 2 | completed | 0/0 | 0 | 96.73 |
| 3 | 3 | completed | 0/0 | 0 | 139.72 |
| 4 | 4 | completed | 0/0 | 0 | 124.13 |
| 5 | 5 | completed | 0/0 | 0 | 110.26 |
| 6 | 6 | completed | 0/0 | 0 | 216.63 |

## Directory Structure

```
c20f5aeb-1397-4cca-aaec-b9264ae525e6/
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
