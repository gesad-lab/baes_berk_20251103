# Run Summary

**Run ID**: c00a794f-e29d-4e15-b209-55e492f12960
**Framework**: ghspec
**Started**: 2025-10-29T06:07:11.889693Z
**Completed**: 2025-10-29T06:24:32.432679Z
**Duration**: 1040.54s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 175.73 |
| 2 | 2 | completed | 0/0 | 0 | 157.40 |
| 3 | 3 | completed | 0/0 | 0 | 233.81 |
| 4 | 4 | completed | 0/0 | 0 | 169.90 |
| 5 | 5 | completed | 0/0 | 0 | 149.44 |
| 6 | 6 | completed | 0/0 | 0 | 154.24 |

## Directory Structure

```
c00a794f-e29d-4e15-b209-55e492f12960/
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
