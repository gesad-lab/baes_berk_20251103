# Run Summary

**Run ID**: 2dd84426-ec8c-4a81-8164-9a0bea88fdae
**Framework**: ghspec
**Started**: 2025-10-28T19:39:47.702129Z
**Completed**: 2025-10-28T19:55:58.718936Z
**Duration**: 971.02s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 159.34 |
| 2 | 2 | completed | 0/0 | 0 | 179.35 |
| 3 | 3 | completed | 0/0 | 0 | 125.16 |
| 4 | 4 | completed | 0/0 | 0 | 190.94 |
| 5 | 5 | completed | 0/0 | 0 | 128.89 |
| 6 | 6 | completed | 0/0 | 0 | 187.33 |

## Directory Structure

```
2dd84426-ec8c-4a81-8164-9a0bea88fdae/
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
