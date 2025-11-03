# Run Summary

**Run ID**: 90d6d439-c186-4c47-8c5e-009d4166cd20
**Framework**: baes
**Started**: 2025-10-30T04:44:46.895017Z
**Completed**: 2025-10-30T04:47:59.417745Z
**Duration**: 192.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 21.65 |
| 2 | 2 | completed | 0/0 | 0 | 22.08 |
| 3 | 3 | completed | 0/0 | 0 | 34.04 |
| 4 | 4 | completed | 0/0 | 0 | 41.44 |
| 5 | 5 | completed | 0/0 | 0 | 31.70 |
| 6 | 6 | completed | 0/0 | 0 | 41.60 |

## Directory Structure

```
90d6d439-c186-4c47-8c5e-009d4166cd20/
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
