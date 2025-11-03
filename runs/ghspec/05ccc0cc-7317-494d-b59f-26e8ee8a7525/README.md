# Run Summary

**Run ID**: 05ccc0cc-7317-494d-b59f-26e8ee8a7525
**Framework**: ghspec
**Started**: 2025-10-28T22:48:02.810037Z
**Completed**: 2025-10-28T23:03:14.675896Z
**Duration**: 911.87s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 173.74 |
| 2 | 2 | completed | 0/0 | 0 | 175.26 |
| 3 | 3 | completed | 0/0 | 0 | 223.86 |
| 4 | 4 | completed | 0/0 | 0 | 111.74 |
| 5 | 5 | completed | 0/0 | 0 | 104.98 |
| 6 | 6 | completed | 0/0 | 0 | 122.28 |

## Directory Structure

```
05ccc0cc-7317-494d-b59f-26e8ee8a7525/
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
