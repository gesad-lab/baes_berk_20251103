# Run Summary

**Run ID**: 9b55e96d-3541-485f-a3df-0ac145895258
**Framework**: ghspec
**Started**: 2025-10-30T22:25:52.026989Z
**Completed**: 2025-10-30T22:42:08.748251Z
**Duration**: 976.72s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 185.24 |
| 2 | 2 | completed | 0/0 | 0 | 165.03 |
| 3 | 3 | completed | 0/0 | 0 | 136.03 |
| 4 | 4 | completed | 0/0 | 0 | 184.12 |
| 5 | 5 | completed | 0/0 | 0 | 140.21 |
| 6 | 6 | completed | 0/0 | 0 | 166.09 |

## Directory Structure

```
9b55e96d-3541-485f-a3df-0ac145895258/
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
