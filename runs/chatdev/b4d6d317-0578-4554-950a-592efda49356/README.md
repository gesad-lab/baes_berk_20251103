# Run Summary

**Run ID**: b4d6d317-0578-4554-950a-592efda49356
**Framework**: chatdev
**Started**: 2025-10-29T23:20:48.089870Z
**Completed**: 2025-10-29T23:47:42.005709Z
**Duration**: 1613.92s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 212.01 |
| 2 | 2 | completed | 0/0 | 0 | 251.46 |
| 3 | 3 | completed | 0/0 | 0 | 351.40 |
| 4 | 4 | completed | 0/0 | 0 | 242.38 |
| 5 | 5 | completed | 0/0 | 0 | 265.19 |
| 6 | 6 | completed | 0/0 | 0 | 291.46 |

## Directory Structure

```
b4d6d317-0578-4554-950a-592efda49356/
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
