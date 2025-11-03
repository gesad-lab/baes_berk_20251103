# Run Summary

**Run ID**: 4ab70870-6786-47bc-87a2-6eba4b44700b
**Framework**: chatdev
**Started**: 2025-10-30T18:34:00.017118Z
**Completed**: 2025-10-30T18:52:47.604072Z
**Duration**: 1127.59s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 187.72 |
| 2 | 2 | completed | 0/0 | 0 | 146.98 |
| 3 | 3 | completed | 0/0 | 0 | 147.78 |
| 4 | 4 | completed | 0/0 | 0 | 194.26 |
| 5 | 5 | completed | 0/0 | 0 | 210.36 |
| 6 | 6 | completed | 0/0 | 0 | 240.48 |

## Directory Structure

```
4ab70870-6786-47bc-87a2-6eba4b44700b/
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
