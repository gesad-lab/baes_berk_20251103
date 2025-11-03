# Run Summary

**Run ID**: 36f69385-0273-4980-a5b0-07a53a425486
**Framework**: baes
**Started**: 2025-10-30T03:55:50.482340Z
**Completed**: 2025-10-30T03:58:40.734778Z
**Duration**: 170.25s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.02 |
| 2 | 2 | completed | 0/0 | 0 | 26.96 |
| 3 | 3 | completed | 0/0 | 0 | 28.57 |
| 4 | 4 | completed | 0/0 | 0 | 22.64 |
| 5 | 5 | completed | 0/0 | 0 | 34.03 |
| 6 | 6 | completed | 0/0 | 0 | 38.02 |

## Directory Structure

```
36f69385-0273-4980-a5b0-07a53a425486/
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
