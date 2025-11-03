# Run Summary

**Run ID**: e76816dc-9b25-4698-906f-91810326b9b4
**Framework**: baes
**Started**: 2025-10-31T04:47:13.947768Z
**Completed**: 2025-10-31T04:53:30.462561Z
**Duration**: 376.51s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 62.78 |
| 2 | 2 | completed | 0/0 | 0 | 62.83 |
| 3 | 3 | completed | 0/0 | 0 | 63.30 |
| 4 | 4 | completed | 0/0 | 0 | 61.78 |
| 5 | 5 | completed | 0/0 | 0 | 62.98 |
| 6 | 6 | completed | 0/0 | 0 | 62.82 |

## Directory Structure

```
e76816dc-9b25-4698-906f-91810326b9b4/
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
