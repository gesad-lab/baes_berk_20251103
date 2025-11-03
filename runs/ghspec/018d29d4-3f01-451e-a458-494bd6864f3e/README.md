# Run Summary

**Run ID**: 018d29d4-3f01-451e-a458-494bd6864f3e
**Framework**: ghspec
**Started**: 2025-10-29T14:14:14.288356Z
**Completed**: 2025-10-29T14:34:09.140367Z
**Duration**: 1194.85s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 221.20 |
| 2 | 2 | completed | 0/0 | 0 | 212.95 |
| 3 | 3 | completed | 0/0 | 0 | 150.04 |
| 4 | 4 | completed | 0/0 | 0 | 256.31 |
| 5 | 5 | completed | 0/0 | 0 | 171.38 |
| 6 | 6 | completed | 0/0 | 0 | 182.96 |

## Directory Structure

```
018d29d4-3f01-451e-a458-494bd6864f3e/
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
