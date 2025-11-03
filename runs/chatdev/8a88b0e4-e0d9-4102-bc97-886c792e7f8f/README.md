# Run Summary

**Run ID**: 8a88b0e4-e0d9-4102-bc97-886c792e7f8f
**Framework**: chatdev
**Started**: 2025-10-29T00:06:19.913784Z
**Completed**: 2025-10-29T00:18:57.001636Z
**Duration**: 757.09s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 177.72 |
| 2 | 2 | completed | 0/0 | 0 | 140.58 |
| 3 | 3 | completed | 0/0 | 0 | 100.94 |
| 4 | 4 | completed | 0/0 | 0 | 100.61 |
| 5 | 5 | completed | 0/0 | 0 | 120.35 |
| 6 | 6 | completed | 0/0 | 0 | 116.89 |

## Directory Structure

```
8a88b0e4-e0d9-4102-bc97-886c792e7f8f/
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
