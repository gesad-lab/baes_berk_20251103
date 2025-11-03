# Run Summary

**Run ID**: 0396f6bc-0251-4ce8-aa2e-40b81a0aee0e
**Framework**: ghspec
**Started**: 2025-10-31T03:21:11.451259Z
**Completed**: 2025-10-31T03:42:23.584491Z
**Duration**: 1272.13s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 243.91 |
| 2 | 2 | completed | 0/0 | 0 | 168.57 |
| 3 | 3 | completed | 0/0 | 0 | 207.32 |
| 4 | 4 | completed | 0/0 | 0 | 246.23 |
| 5 | 5 | completed | 0/0 | 0 | 258.11 |
| 6 | 6 | completed | 0/0 | 0 | 147.99 |

## Directory Structure

```
0396f6bc-0251-4ce8-aa2e-40b81a0aee0e/
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
