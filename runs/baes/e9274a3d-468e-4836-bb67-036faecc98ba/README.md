# Run Summary

**Run ID**: e9274a3d-468e-4836-bb67-036faecc98ba
**Framework**: baes
**Started**: 2025-10-28T21:40:45.814560Z
**Completed**: 2025-10-28T21:43:53.241813Z
**Duration**: 187.43s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.73 |
| 2 | 2 | completed | 0/0 | 0 | 47.26 |
| 3 | 3 | completed | 0/0 | 0 | 30.81 |
| 4 | 4 | completed | 0/0 | 0 | 21.78 |
| 5 | 5 | completed | 0/0 | 0 | 31.87 |
| 6 | 6 | completed | 0/0 | 0 | 34.98 |

## Directory Structure

```
e9274a3d-468e-4836-bb67-036faecc98ba/
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
