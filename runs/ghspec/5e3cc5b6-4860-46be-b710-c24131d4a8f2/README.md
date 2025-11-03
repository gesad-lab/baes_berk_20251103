# Run Summary

**Run ID**: 5e3cc5b6-4860-46be-b710-c24131d4a8f2
**Framework**: ghspec
**Started**: 2025-10-30T05:17:22.925941Z
**Completed**: 2025-10-30T05:33:03.045254Z
**Duration**: 940.12s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 159.39 |
| 2 | 2 | completed | 0/0 | 0 | 90.06 |
| 3 | 3 | completed | 0/0 | 0 | 229.70 |
| 4 | 4 | completed | 0/0 | 0 | 157.65 |
| 5 | 5 | completed | 0/0 | 0 | 132.00 |
| 6 | 6 | completed | 0/0 | 0 | 171.30 |

## Directory Structure

```
5e3cc5b6-4860-46be-b710-c24131d4a8f2/
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
