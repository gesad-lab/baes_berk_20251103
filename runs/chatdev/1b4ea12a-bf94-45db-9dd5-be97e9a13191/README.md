# Run Summary

**Run ID**: 1b4ea12a-bf94-45db-9dd5-be97e9a13191
**Framework**: chatdev
**Started**: 2025-10-29T22:41:41.916794Z
**Completed**: 2025-10-29T22:57:25.846350Z
**Duration**: 943.93s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 207.53 |
| 2 | 2 | completed | 0/0 | 0 | 142.81 |
| 3 | 3 | completed | 0/0 | 0 | 128.38 |
| 4 | 4 | completed | 0/0 | 0 | 143.12 |
| 5 | 5 | completed | 0/0 | 0 | 176.36 |
| 6 | 6 | completed | 0/0 | 0 | 145.72 |

## Directory Structure

```
1b4ea12a-bf94-45db-9dd5-be97e9a13191/
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
