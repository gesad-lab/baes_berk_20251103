# Run Summary

**Run ID**: 1d96d250-1a1f-45d6-83fe-321919e65026
**Framework**: chatdev
**Started**: 2025-10-28T17:20:59.604866Z
**Completed**: 2025-10-28T17:55:16.793994Z
**Duration**: 2057.19s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 264.59 |
| 2 | 2 | completed | 0/0 | 0 | 230.58 |
| 3 | 3 | completed | 0/0 | 0 | 321.94 |
| 4 | 4 | completed | 0/0 | 0 | 353.80 |
| 5 | 5 | completed | 0/0 | 0 | 436.93 |
| 6 | 6 | completed | 0/0 | 0 | 449.35 |

## Directory Structure

```
1d96d250-1a1f-45d6-83fe-321919e65026/
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
