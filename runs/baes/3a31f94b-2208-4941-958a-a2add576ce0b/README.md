# Run Summary

**Run ID**: 3a31f94b-2208-4941-958a-a2add576ce0b
**Framework**: baes
**Started**: 2025-10-31T13:40:52.311007Z
**Completed**: 2025-10-31T13:44:47.278337Z
**Duration**: 234.97s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 37.83 |
| 2 | 2 | completed | 0/0 | 0 | 40.99 |
| 3 | 3 | completed | 0/0 | 0 | 36.41 |
| 4 | 4 | completed | 0/0 | 0 | 41.91 |
| 5 | 5 | completed | 0/0 | 0 | 35.79 |
| 6 | 6 | completed | 0/0 | 0 | 42.03 |

## Directory Structure

```
3a31f94b-2208-4941-958a-a2add576ce0b/
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
