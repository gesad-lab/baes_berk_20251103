# Run Summary

**Run ID**: 1272cf36-810b-44a2-a485-1d3b87477cde
**Framework**: chatdev
**Started**: 2025-10-28T12:58:12.378427Z
**Completed**: 2025-10-28T13:29:48.419247Z
**Duration**: 1896.04s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 258.79 |
| 2 | 2 | completed | 0/0 | 0 | 244.83 |
| 3 | 3 | completed | 0/0 | 0 | 303.17 |
| 4 | 4 | completed | 0/0 | 0 | 353.99 |
| 5 | 5 | completed | 0/0 | 0 | 383.57 |
| 6 | 6 | completed | 0/0 | 0 | 351.68 |

## Directory Structure

```
1272cf36-810b-44a2-a485-1d3b87477cde/
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
