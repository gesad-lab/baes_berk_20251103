# Run Summary

**Run ID**: 5f3cf14e-5bc9-43c9-b4eb-b4a1089c12dd
**Framework**: baes
**Started**: 2025-10-29T03:30:21.874755Z
**Completed**: 2025-10-29T03:32:30.430399Z
**Duration**: 128.56s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 18.21 |
| 2 | 2 | completed | 0/0 | 0 | 21.80 |
| 3 | 3 | completed | 0/0 | 0 | 22.30 |
| 4 | 4 | completed | 0/0 | 0 | 22.42 |
| 5 | 5 | completed | 0/0 | 0 | 19.89 |
| 6 | 6 | completed | 0/0 | 0 | 23.92 |

## Directory Structure

```
5f3cf14e-5bc9-43c9-b4eb-b4a1089c12dd/
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
