# Run Summary

**Run ID**: 4eacdbba-14af-44bb-ade2-b79c46dba34c
**Framework**: chatdev
**Started**: 2025-10-30T22:45:57.666559Z
**Completed**: 2025-10-30T23:06:08.081482Z
**Duration**: 1210.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 283.62 |
| 2 | 2 | completed | 0/0 | 0 | 169.11 |
| 3 | 3 | completed | 0/0 | 0 | 159.96 |
| 4 | 4 | completed | 0/0 | 0 | 150.85 |
| 5 | 5 | completed | 0/0 | 0 | 223.09 |
| 6 | 6 | completed | 0/0 | 0 | 223.78 |

## Directory Structure

```
4eacdbba-14af-44bb-ade2-b79c46dba34c/
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
