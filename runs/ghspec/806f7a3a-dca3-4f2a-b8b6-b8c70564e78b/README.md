# Run Summary

**Run ID**: 806f7a3a-dca3-4f2a-b8b6-b8c70564e78b
**Framework**: ghspec
**Started**: 2025-10-30T04:25:26.423887Z
**Completed**: 2025-10-30T04:44:45.587792Z
**Duration**: 1159.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 259.40 |
| 2 | 2 | completed | 0/0 | 0 | 141.16 |
| 3 | 3 | completed | 0/0 | 0 | 178.28 |
| 4 | 4 | completed | 0/0 | 0 | 212.55 |
| 5 | 5 | completed | 0/0 | 0 | 208.18 |
| 6 | 6 | completed | 0/0 | 0 | 159.60 |

## Directory Structure

```
806f7a3a-dca3-4f2a-b8b6-b8c70564e78b/
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
