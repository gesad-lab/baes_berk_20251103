# Run Summary

**Run ID**: bd8144a4-1401-47c5-a14e-268562a5a6a4
**Framework**: baes
**Started**: 2025-10-28T23:03:18.253959Z
**Completed**: 2025-10-28T23:05:35.531537Z
**Duration**: 137.28s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.89 |
| 2 | 2 | completed | 0/0 | 0 | 19.76 |
| 3 | 3 | completed | 0/0 | 0 | 27.40 |
| 4 | 4 | completed | 0/0 | 0 | 20.82 |
| 5 | 5 | completed | 0/0 | 0 | 23.17 |
| 6 | 6 | completed | 0/0 | 0 | 26.23 |

## Directory Structure

```
bd8144a4-1401-47c5-a14e-268562a5a6a4/
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
