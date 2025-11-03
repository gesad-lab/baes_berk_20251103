# Run Summary

**Run ID**: 31ff19d0-d800-4a24-9108-50d4232f8e1e
**Framework**: ghspec
**Started**: 2025-10-31T08:29:19.973744Z
**Completed**: 2025-10-31T08:48:22.384785Z
**Duration**: 1142.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 256.33 |
| 2 | 2 | completed | 0/0 | 0 | 213.99 |
| 3 | 3 | completed | 0/0 | 0 | 182.80 |
| 4 | 4 | completed | 0/0 | 0 | 182.54 |
| 5 | 5 | completed | 0/0 | 0 | 145.69 |
| 6 | 6 | completed | 0/0 | 0 | 161.04 |

## Directory Structure

```
31ff19d0-d800-4a24-9108-50d4232f8e1e/
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
