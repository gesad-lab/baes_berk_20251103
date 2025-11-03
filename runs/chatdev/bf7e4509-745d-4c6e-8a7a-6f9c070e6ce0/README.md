# Run Summary

**Run ID**: bf7e4509-745d-4c6e-8a7a-6f9c070e6ce0
**Framework**: chatdev
**Started**: 2025-10-29T14:37:44.826646Z
**Completed**: 2025-10-29T14:58:59.383174Z
**Duration**: 1274.56s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 227.12 |
| 2 | 2 | completed | 0/0 | 0 | 220.43 |
| 3 | 3 | completed | 0/0 | 0 | 215.25 |
| 4 | 4 | completed | 0/0 | 0 | 185.68 |
| 5 | 5 | completed | 0/0 | 0 | 207.88 |
| 6 | 6 | completed | 0/0 | 0 | 218.19 |

## Directory Structure

```
bf7e4509-745d-4c6e-8a7a-6f9c070e6ce0/
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
