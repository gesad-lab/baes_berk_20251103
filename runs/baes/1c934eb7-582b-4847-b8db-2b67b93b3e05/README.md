# Run Summary

**Run ID**: 1c934eb7-582b-4847-b8db-2b67b93b3e05
**Framework**: baes
**Started**: 2025-10-28T23:28:13.578680Z
**Completed**: 2025-10-28T23:30:35.021567Z
**Duration**: 141.44s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 18.01 |
| 2 | 2 | completed | 0/0 | 0 | 20.94 |
| 3 | 3 | completed | 0/0 | 0 | 25.78 |
| 4 | 4 | completed | 0/0 | 0 | 21.65 |
| 5 | 5 | completed | 0/0 | 0 | 26.60 |
| 6 | 6 | completed | 0/0 | 0 | 28.45 |

## Directory Structure

```
1c934eb7-582b-4847-b8db-2b67b93b3e05/
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
