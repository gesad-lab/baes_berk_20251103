# Run Summary

**Run ID**: a864d4ef-414d-4224-b616-c590daf924de
**Framework**: baes
**Started**: 2025-10-30T17:23:02.564148Z
**Completed**: 2025-10-30T17:26:33.990153Z
**Duration**: 211.43s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.39 |
| 2 | 2 | completed | 0/0 | 0 | 30.10 |
| 3 | 3 | completed | 0/0 | 0 | 34.73 |
| 4 | 4 | completed | 0/0 | 0 | 34.39 |
| 5 | 5 | completed | 0/0 | 0 | 43.70 |
| 6 | 6 | completed | 0/0 | 0 | 35.11 |

## Directory Structure

```
a864d4ef-414d-4224-b616-c590daf924de/
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
