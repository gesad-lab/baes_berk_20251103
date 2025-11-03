# Run Summary

**Run ID**: 3253c301-e6c4-4cb0-8d6f-e411e0857ee7
**Framework**: chatdev
**Started**: 2025-10-30T06:13:14.622314Z
**Completed**: 2025-10-30T06:31:30.381033Z
**Duration**: 1095.76s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 132.14 |
| 2 | 2 | completed | 0/0 | 0 | 149.13 |
| 3 | 3 | completed | 0/0 | 0 | 169.66 |
| 4 | 4 | completed | 0/0 | 0 | 187.32 |
| 5 | 5 | completed | 0/0 | 0 | 213.86 |
| 6 | 6 | completed | 0/0 | 0 | 243.64 |

## Directory Structure

```
3253c301-e6c4-4cb0-8d6f-e411e0857ee7/
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
