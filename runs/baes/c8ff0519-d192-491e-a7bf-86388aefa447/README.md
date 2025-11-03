# Run Summary

**Run ID**: c8ff0519-d192-491e-a7bf-86388aefa447
**Framework**: baes
**Started**: 2025-10-31T17:13:02.485663Z
**Completed**: 2025-10-31T17:17:33.220948Z
**Duration**: 270.74s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 38.70 |
| 2 | 2 | completed | 0/0 | 0 | 36.21 |
| 3 | 3 | completed | 0/0 | 0 | 77.88 |
| 4 | 4 | completed | 0/0 | 0 | 48.58 |
| 5 | 5 | completed | 0/0 | 0 | 30.57 |
| 6 | 6 | completed | 0/0 | 0 | 38.78 |

## Directory Structure

```
c8ff0519-d192-491e-a7bf-86388aefa447/
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
