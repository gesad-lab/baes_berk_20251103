# Run Summary

**Run ID**: cb792b53-a7aa-4224-9dfc-37fb7aba7b8c
**Framework**: baes
**Started**: 2025-10-30T11:27:13.155425Z
**Completed**: 2025-10-30T11:31:21.944335Z
**Duration**: 248.79s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 36.38 |
| 2 | 2 | completed | 0/0 | 0 | 37.47 |
| 3 | 3 | completed | 0/0 | 0 | 41.38 |
| 4 | 4 | completed | 0/0 | 0 | 41.55 |
| 5 | 5 | completed | 0/0 | 0 | 34.86 |
| 6 | 6 | completed | 0/0 | 0 | 57.14 |

## Directory Structure

```
cb792b53-a7aa-4224-9dfc-37fb7aba7b8c/
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
