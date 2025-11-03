# Run Summary

**Run ID**: 3d5a06c9-adf5-4722-8b60-5668a198ab6d
**Framework**: ghspec
**Started**: 2025-10-31T09:14:38.163882Z
**Completed**: 2025-10-31T09:31:52.792397Z
**Duration**: 1034.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 235.70 |
| 2 | 2 | completed | 0/0 | 0 | 164.81 |
| 3 | 3 | completed | 0/0 | 0 | 135.33 |
| 4 | 4 | completed | 0/0 | 0 | 236.59 |
| 5 | 5 | completed | 0/0 | 0 | 113.09 |
| 6 | 6 | completed | 0/0 | 0 | 149.10 |

## Directory Structure

```
3d5a06c9-adf5-4722-8b60-5668a198ab6d/
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
