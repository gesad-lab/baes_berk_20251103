# Run Summary

**Run ID**: ec10db37-b75a-4860-bc62-31d74af00a7a
**Framework**: baes
**Started**: 2025-10-29T04:55:59.633365Z
**Completed**: 2025-10-29T04:59:10.823964Z
**Duration**: 191.19s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 30.71 |
| 2 | 2 | completed | 0/0 | 0 | 35.62 |
| 3 | 3 | completed | 0/0 | 0 | 30.26 |
| 4 | 4 | completed | 0/0 | 0 | 32.64 |
| 5 | 5 | completed | 0/0 | 0 | 28.43 |
| 6 | 6 | completed | 0/0 | 0 | 33.53 |

## Directory Structure

```
ec10db37-b75a-4860-bc62-31d74af00a7a/
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
