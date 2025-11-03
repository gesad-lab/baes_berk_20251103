# Run Summary

**Run ID**: d228a1e2-fe4e-4148-a507-1ec4ea29962c
**Framework**: ghspec
**Started**: 2025-10-29T09:06:48.398160Z
**Completed**: 2025-10-29T09:34:16.002363Z
**Duration**: 1647.60s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 314.99 |
| 2 | 2 | completed | 0/0 | 0 | 169.21 |
| 3 | 3 | completed | 0/0 | 0 | 307.35 |
| 4 | 4 | completed | 0/0 | 0 | 258.95 |
| 5 | 5 | completed | 0/0 | 0 | 377.33 |
| 6 | 6 | completed | 0/0 | 0 | 219.77 |

## Directory Structure

```
d228a1e2-fe4e-4148-a507-1ec4ea29962c/
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
