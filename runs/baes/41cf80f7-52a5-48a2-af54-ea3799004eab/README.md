# Run Summary

**Run ID**: 41cf80f7-52a5-48a2-af54-ea3799004eab
**Framework**: baes
**Started**: 2025-10-30T05:33:03.335124Z
**Completed**: 2025-10-30T05:36:10.355705Z
**Duration**: 187.02s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.55 |
| 2 | 2 | completed | 0/0 | 0 | 36.46 |
| 3 | 3 | completed | 0/0 | 0 | 35.07 |
| 4 | 4 | completed | 0/0 | 0 | 23.21 |
| 5 | 5 | completed | 0/0 | 0 | 40.21 |
| 6 | 6 | completed | 0/0 | 0 | 32.51 |

## Directory Structure

```
41cf80f7-52a5-48a2-af54-ea3799004eab/
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
