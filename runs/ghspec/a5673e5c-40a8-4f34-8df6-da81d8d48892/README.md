# Run Summary

**Run ID**: a5673e5c-40a8-4f34-8df6-da81d8d48892
**Framework**: ghspec
**Started**: 2025-10-29T08:21:37.015628Z
**Completed**: 2025-10-29T08:40:40.511783Z
**Duration**: 1143.50s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 158.70 |
| 2 | 2 | completed | 0/0 | 0 | 296.91 |
| 3 | 3 | completed | 0/0 | 0 | 188.65 |
| 4 | 4 | completed | 0/0 | 0 | 183.56 |
| 5 | 5 | completed | 0/0 | 0 | 153.70 |
| 6 | 6 | completed | 0/0 | 0 | 161.97 |

## Directory Structure

```
a5673e5c-40a8-4f34-8df6-da81d8d48892/
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
