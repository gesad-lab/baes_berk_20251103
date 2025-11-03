# Run Summary

**Run ID**: d2db77ae-acfa-4551-b247-6216547fe8b0
**Framework**: chatdev
**Started**: 2025-10-29T09:38:14.262066Z
**Completed**: 2025-10-29T09:59:31.898006Z
**Duration**: 1277.64s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 247.41 |
| 2 | 2 | completed | 0/0 | 0 | 167.77 |
| 3 | 3 | completed | 0/0 | 0 | 195.41 |
| 4 | 4 | completed | 0/0 | 0 | 205.07 |
| 5 | 5 | completed | 0/0 | 0 | 224.13 |
| 6 | 6 | completed | 0/0 | 0 | 237.84 |

## Directory Structure

```
d2db77ae-acfa-4551-b247-6216547fe8b0/
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
