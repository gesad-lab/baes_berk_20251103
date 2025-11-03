# Run Summary

**Run ID**: 9ce81574-8818-4f39-bf58-eaabe4bfe866
**Framework**: chatdev
**Started**: 2025-10-31T00:10:30.347903Z
**Completed**: 2025-10-31T00:28:41.960914Z
**Duration**: 1091.61s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 159.39 |
| 2 | 2 | completed | 0/0 | 0 | 168.26 |
| 3 | 3 | completed | 0/0 | 0 | 177.28 |
| 4 | 4 | completed | 0/0 | 0 | 170.83 |
| 5 | 5 | completed | 0/0 | 0 | 196.14 |
| 6 | 6 | completed | 0/0 | 0 | 219.70 |

## Directory Structure

```
9ce81574-8818-4f39-bf58-eaabe4bfe866/
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
