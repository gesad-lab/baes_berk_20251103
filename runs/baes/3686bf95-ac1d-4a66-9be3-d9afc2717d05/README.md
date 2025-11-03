# Run Summary

**Run ID**: 3686bf95-ac1d-4a66-9be3-d9afc2717d05
**Framework**: baes
**Started**: 2025-10-30T15:08:04.213553Z
**Completed**: 2025-10-30T15:11:51.651951Z
**Duration**: 227.44s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 31.70 |
| 2 | 2 | completed | 0/0 | 0 | 56.67 |
| 3 | 3 | completed | 0/0 | 0 | 35.25 |
| 4 | 4 | completed | 0/0 | 0 | 36.63 |
| 5 | 5 | completed | 0/0 | 0 | 29.32 |
| 6 | 6 | completed | 0/0 | 0 | 37.87 |

## Directory Structure

```
3686bf95-ac1d-4a66-9be3-d9afc2717d05/
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
