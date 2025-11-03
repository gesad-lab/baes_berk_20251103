# Run Summary

**Run ID**: 747d8a2c-4edc-49ca-a11d-40ca18eda963
**Framework**: chatdev
**Started**: 2025-10-31T21:17:23.754999Z
**Completed**: 2025-10-31T21:37:29.181021Z
**Duration**: 1205.43s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 259.81 |
| 2 | 2 | completed | 0/0 | 0 | 210.01 |
| 3 | 3 | completed | 0/0 | 0 | 219.38 |
| 4 | 4 | completed | 0/0 | 0 | 173.74 |
| 5 | 5 | completed | 0/0 | 0 | 175.81 |
| 6 | 6 | completed | 0/0 | 0 | 166.66 |

## Directory Structure

```
747d8a2c-4edc-49ca-a11d-40ca18eda963/
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
