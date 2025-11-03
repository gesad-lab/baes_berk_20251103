# Run Summary

**Run ID**: 279229b1-431c-4201-9106-7cc2b7f184c3
**Framework**: ghspec
**Started**: 2025-10-28T16:47:33.755971Z
**Completed**: 2025-10-28T17:16:40.073667Z
**Duration**: 1746.32s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 483.04 |
| 2 | 2 | completed | 0/0 | 0 | 252.83 |
| 3 | 3 | completed | 0/0 | 0 | 218.03 |
| 4 | 4 | completed | 0/0 | 0 | 220.55 |
| 5 | 5 | completed | 0/0 | 0 | 178.18 |
| 6 | 6 | completed | 0/0 | 0 | 393.68 |

## Directory Structure

```
279229b1-431c-4201-9106-7cc2b7f184c3/
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
