# Run Summary

**Run ID**: 88d365df-f764-43ad-a172-890b70792fb7
**Framework**: baes
**Started**: 2025-10-29T04:05:48.077693Z
**Completed**: 2025-10-29T04:09:09.805789Z
**Duration**: 201.73s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.70 |
| 2 | 2 | completed | 0/0 | 0 | 39.86 |
| 3 | 3 | completed | 0/0 | 0 | 31.10 |
| 4 | 4 | completed | 0/0 | 0 | 28.49 |
| 5 | 5 | completed | 0/0 | 0 | 32.35 |
| 6 | 6 | completed | 0/0 | 0 | 37.22 |

## Directory Structure

```
88d365df-f764-43ad-a172-890b70792fb7/
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
