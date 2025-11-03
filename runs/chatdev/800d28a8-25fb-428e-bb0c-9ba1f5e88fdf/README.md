# Run Summary

**Run ID**: 800d28a8-25fb-428e-bb0c-9ba1f5e88fdf
**Framework**: chatdev
**Started**: 2025-10-29T02:36:30.036624Z
**Completed**: 2025-10-29T02:52:34.195928Z
**Duration**: 964.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 166.07 |
| 2 | 2 | completed | 0/0 | 0 | 158.36 |
| 3 | 3 | completed | 0/0 | 0 | 149.30 |
| 4 | 4 | completed | 0/0 | 0 | 153.80 |
| 5 | 5 | completed | 0/0 | 0 | 154.23 |
| 6 | 6 | completed | 0/0 | 0 | 182.39 |

## Directory Structure

```
800d28a8-25fb-428e-bb0c-9ba1f5e88fdf/
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
