# Run Summary

**Run ID**: 451e137c-6f56-4ba1-a853-e0e8ee14473e
**Framework**: chatdev
**Started**: 2025-10-28T23:30:38.721792Z
**Completed**: 2025-10-28T23:51:52.812462Z
**Duration**: 1274.09s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 156.96 |
| 2 | 2 | completed | 0/0 | 0 | 205.00 |
| 3 | 3 | completed | 0/0 | 0 | 190.98 |
| 4 | 4 | completed | 0/0 | 0 | 198.00 |
| 5 | 5 | completed | 0/0 | 0 | 244.46 |
| 6 | 6 | completed | 0/0 | 0 | 278.69 |

## Directory Structure

```
451e137c-6f56-4ba1-a853-e0e8ee14473e/
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
