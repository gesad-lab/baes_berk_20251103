# Run Summary

**Run ID**: 26888623-50dc-4bde-8d8e-504deeffa654
**Framework**: chatdev
**Started**: 2025-10-29T21:58:30.657682Z
**Completed**: 2025-10-29T22:20:35.683012Z
**Duration**: 1325.03s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 457.24 |
| 2 | 2 | completed | 0/0 | 0 | 190.18 |
| 3 | 3 | completed | 0/0 | 0 | 196.71 |
| 4 | 4 | completed | 0/0 | 0 | 142.78 |
| 5 | 5 | completed | 0/0 | 0 | 170.60 |
| 6 | 6 | completed | 0/0 | 0 | 167.51 |

## Directory Structure

```
26888623-50dc-4bde-8d8e-504deeffa654/
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
