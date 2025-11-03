# Run Summary

**Run ID**: 46651451-9b35-4648-ab27-f60cdf9d3b90
**Framework**: chatdev
**Started**: 2025-10-30T23:31:54.132545Z
**Completed**: 2025-10-30T23:46:51.925190Z
**Duration**: 897.79s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 136.14 |
| 2 | 2 | completed | 0/0 | 0 | 122.46 |
| 3 | 3 | completed | 0/0 | 0 | 160.27 |
| 4 | 4 | completed | 0/0 | 0 | 152.49 |
| 5 | 5 | completed | 0/0 | 0 | 169.01 |
| 6 | 6 | completed | 0/0 | 0 | 157.42 |

## Directory Structure

```
46651451-9b35-4648-ab27-f60cdf9d3b90/
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
