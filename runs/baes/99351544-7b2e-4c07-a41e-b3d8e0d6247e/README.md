# Run Summary

**Run ID**: 99351544-7b2e-4c07-a41e-b3d8e0d6247e
**Framework**: baes
**Started**: 2025-10-29T00:04:04.796123Z
**Completed**: 2025-10-29T00:06:19.100080Z
**Duration**: 134.30s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.72 |
| 2 | 2 | completed | 0/0 | 0 | 19.69 |
| 3 | 3 | completed | 0/0 | 0 | 25.66 |
| 4 | 4 | completed | 0/0 | 0 | 19.28 |
| 5 | 5 | completed | 0/0 | 0 | 25.29 |
| 6 | 6 | completed | 0/0 | 0 | 24.67 |

## Directory Structure

```
99351544-7b2e-4c07-a41e-b3d8e0d6247e/
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
