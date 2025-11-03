# Run Summary

**Run ID**: 7a6ead32-3f04-42d2-84c8-cac27d27cb3c
**Framework**: ghspec
**Started**: 2025-10-29T02:19:04.482228Z
**Completed**: 2025-10-29T02:33:55.567197Z
**Duration**: 891.08s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 180.99 |
| 2 | 2 | completed | 0/0 | 0 | 139.69 |
| 3 | 3 | completed | 0/0 | 0 | 122.09 |
| 4 | 4 | completed | 0/0 | 0 | 164.66 |
| 5 | 5 | completed | 0/0 | 0 | 165.36 |
| 6 | 6 | completed | 0/0 | 0 | 118.29 |

## Directory Structure

```
7a6ead32-3f04-42d2-84c8-cac27d27cb3c/
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
