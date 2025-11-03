# Run Summary

**Run ID**: 72735833-d2af-48ed-b4c8-90c31e2c0bee
**Framework**: chatdev
**Started**: 2025-10-31T04:40:28.709581Z
**Completed**: 2025-10-31T04:45:55.490492Z
**Duration**: 326.78s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 323.30 |
| 2 | 2 | completed | 0/0 | 0 | 0.69 |
| 3 | 3 | completed | 0/0 | 0 | 0.69 |
| 4 | 4 | completed | 0/0 | 0 | 0.70 |
| 5 | 5 | completed | 0/0 | 0 | 0.70 |
| 6 | 6 | completed | 0/0 | 0 | 0.70 |

## Directory Structure

```
72735833-d2af-48ed-b4c8-90c31e2c0bee/
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
