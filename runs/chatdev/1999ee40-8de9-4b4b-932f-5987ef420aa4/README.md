# Run Summary

**Run ID**: 1999ee40-8de9-4b4b-932f-5987ef420aa4
**Framework**: chatdev
**Started**: 2025-10-30T11:31:23.329389Z
**Completed**: 2025-10-30T11:48:43.851918Z
**Duration**: 1040.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 166.99 |
| 2 | 2 | completed | 0/0 | 0 | 233.30 |
| 3 | 3 | completed | 0/0 | 0 | 144.86 |
| 4 | 4 | completed | 0/0 | 0 | 142.70 |
| 5 | 5 | completed | 0/0 | 0 | 176.95 |
| 6 | 6 | completed | 0/0 | 0 | 175.72 |

## Directory Structure

```
1999ee40-8de9-4b4b-932f-5987ef420aa4/
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
