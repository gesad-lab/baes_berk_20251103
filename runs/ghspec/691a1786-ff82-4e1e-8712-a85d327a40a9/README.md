# Run Summary

**Run ID**: 691a1786-ff82-4e1e-8712-a85d327a40a9
**Framework**: ghspec
**Started**: 2025-10-30T07:38:56.596673Z
**Completed**: 2025-10-30T07:58:59.380453Z
**Duration**: 1202.78s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 196.28 |
| 2 | 2 | completed | 0/0 | 0 | 197.97 |
| 3 | 3 | completed | 0/0 | 0 | 112.10 |
| 4 | 4 | completed | 0/0 | 0 | 377.97 |
| 5 | 5 | completed | 0/0 | 0 | 155.80 |
| 6 | 6 | completed | 0/0 | 0 | 162.66 |

## Directory Structure

```
691a1786-ff82-4e1e-8712-a85d327a40a9/
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
