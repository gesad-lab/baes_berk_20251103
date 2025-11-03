# Run Summary

**Run ID**: 3e7d5734-4952-46dc-a9bc-6e3045a647e6
**Framework**: baes
**Started**: 2025-10-30T03:18:05.673118Z
**Completed**: 2025-10-30T03:21:22.694152Z
**Duration**: 197.02s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.26 |
| 2 | 2 | completed | 0/0 | 0 | 18.36 |
| 3 | 3 | completed | 0/0 | 0 | 53.25 |
| 4 | 4 | completed | 0/0 | 0 | 20.64 |
| 5 | 5 | completed | 0/0 | 0 | 37.03 |
| 6 | 6 | completed | 0/0 | 0 | 35.47 |

## Directory Structure

```
3e7d5734-4952-46dc-a9bc-6e3045a647e6/
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
