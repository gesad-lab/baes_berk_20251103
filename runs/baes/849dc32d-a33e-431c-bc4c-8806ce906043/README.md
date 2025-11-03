# Run Summary

**Run ID**: 849dc32d-a33e-431c-bc4c-8806ce906043
**Framework**: baes
**Started**: 2025-10-29T23:18:07.951397Z
**Completed**: 2025-10-29T23:20:46.933342Z
**Duration**: 158.98s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 27.54 |
| 2 | 2 | completed | 0/0 | 0 | 18.90 |
| 3 | 3 | completed | 0/0 | 0 | 29.13 |
| 4 | 4 | completed | 0/0 | 0 | 22.60 |
| 5 | 5 | completed | 0/0 | 0 | 29.60 |
| 6 | 6 | completed | 0/0 | 0 | 31.20 |

## Directory Structure

```
849dc32d-a33e-431c-bc4c-8806ce906043/
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
