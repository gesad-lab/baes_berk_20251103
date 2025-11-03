# Run Summary

**Run ID**: 712cb2a7-90fd-43c8-a2bb-2334457c081f
**Framework**: baes
**Started**: 2025-10-31T02:59:25.643260Z
**Completed**: 2025-10-31T03:03:15.630835Z
**Duration**: 229.99s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 28.32 |
| 2 | 2 | completed | 0/0 | 0 | 46.94 |
| 3 | 3 | completed | 0/0 | 0 | 35.16 |
| 4 | 4 | completed | 0/0 | 0 | 42.82 |
| 5 | 5 | completed | 0/0 | 0 | 39.24 |
| 6 | 6 | completed | 0/0 | 0 | 37.49 |

## Directory Structure

```
712cb2a7-90fd-43c8-a2bb-2334457c081f/
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
