# Run Summary

**Run ID**: acef64c1-a233-4d88-8d86-5907ea7fda56
**Framework**: chatdev
**Started**: 2025-10-29T00:35:15.895192Z
**Completed**: 2025-10-29T00:49:42.432023Z
**Duration**: 866.54s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 98.36 |
| 2 | 2 | completed | 0/0 | 0 | 100.51 |
| 3 | 3 | completed | 0/0 | 0 | 207.27 |
| 4 | 4 | completed | 0/0 | 0 | 184.78 |
| 5 | 5 | completed | 0/0 | 0 | 129.84 |
| 6 | 6 | completed | 0/0 | 0 | 145.77 |

## Directory Structure

```
acef64c1-a233-4d88-8d86-5907ea7fda56/
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
