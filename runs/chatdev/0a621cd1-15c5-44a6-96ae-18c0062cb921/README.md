# Run Summary

**Run ID**: 0a621cd1-15c5-44a6-96ae-18c0062cb921
**Framework**: chatdev
**Started**: 2025-10-30T03:21:25.818638Z
**Completed**: 2025-10-30T03:52:58.527120Z
**Duration**: 1892.71s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 307.15 |
| 2 | 2 | completed | 0/0 | 0 | 195.50 |
| 3 | 3 | completed | 0/0 | 0 | 283.77 |
| 4 | 4 | completed | 0/0 | 0 | 287.00 |
| 5 | 5 | completed | 0/0 | 0 | 485.55 |
| 6 | 6 | completed | 0/0 | 0 | 333.73 |

## Directory Structure

```
0a621cd1-15c5-44a6-96ae-18c0062cb921/
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
