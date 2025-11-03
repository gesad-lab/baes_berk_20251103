# Run Summary

**Run ID**: bc525074-2f77-4dc7-b730-2c65345b4401
**Framework**: baes
**Started**: 2025-10-29T05:36:45.860028Z
**Completed**: 2025-10-29T05:40:32.774905Z
**Duration**: 226.91s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.27 |
| 2 | 2 | completed | 0/0 | 0 | 39.59 |
| 3 | 3 | completed | 0/0 | 0 | 48.75 |
| 4 | 4 | completed | 0/0 | 0 | 36.40 |
| 5 | 5 | completed | 0/0 | 0 | 34.77 |
| 6 | 6 | completed | 0/0 | 0 | 35.13 |

## Directory Structure

```
bc525074-2f77-4dc7-b730-2c65345b4401/
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
