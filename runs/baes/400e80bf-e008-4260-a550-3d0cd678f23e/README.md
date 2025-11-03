# Run Summary

**Run ID**: 400e80bf-e008-4260-a550-3d0cd678f23e
**Framework**: baes
**Started**: 2025-10-29T18:26:04.627385Z
**Completed**: 2025-10-29T18:29:35.195425Z
**Duration**: 210.57s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 41.55 |
| 2 | 2 | completed | 0/0 | 0 | 32.11 |
| 3 | 3 | completed | 0/0 | 0 | 51.39 |
| 4 | 4 | completed | 0/0 | 0 | 24.63 |
| 5 | 5 | completed | 0/0 | 0 | 29.91 |
| 6 | 6 | completed | 0/0 | 0 | 30.98 |

## Directory Structure

```
400e80bf-e008-4260-a550-3d0cd678f23e/
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
