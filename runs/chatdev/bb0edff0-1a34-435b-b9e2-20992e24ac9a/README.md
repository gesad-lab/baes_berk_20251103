# Run Summary

**Run ID**: bb0edff0-1a34-435b-b9e2-20992e24ac9a
**Framework**: chatdev
**Started**: 2025-10-31T03:45:42.200548Z
**Completed**: 2025-10-31T04:07:02.039273Z
**Duration**: 1279.84s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 178.97 |
| 2 | 2 | completed | 0/0 | 0 | 218.66 |
| 3 | 3 | completed | 0/0 | 0 | 280.79 |
| 4 | 4 | completed | 0/0 | 0 | 600.02 |
| 5 | 5 | completed | 0/0 | 0 | 0.69 |
| 6 | 6 | completed | 0/0 | 0 | 0.70 |

## Directory Structure

```
bb0edff0-1a34-435b-b9e2-20992e24ac9a/
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
