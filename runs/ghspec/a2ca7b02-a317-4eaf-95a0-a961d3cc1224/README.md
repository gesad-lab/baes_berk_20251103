# Run Summary

**Run ID**: a2ca7b02-a317-4eaf-95a0-a961d3cc1224
**Framework**: ghspec
**Started**: 2025-10-28T10:56:14.609206Z
**Completed**: 2025-10-28T11:17:45.501759Z
**Duration**: 1290.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 202.48 |
| 2 | 2 | completed | 0/0 | 0 | 148.75 |
| 3 | 3 | completed | 0/0 | 0 | 306.34 |
| 4 | 4 | completed | 0/0 | 0 | 373.38 |
| 5 | 5 | completed | 0/0 | 0 | 88.31 |
| 6 | 6 | completed | 0/0 | 0 | 171.63 |

## Directory Structure

```
a2ca7b02-a317-4eaf-95a0-a961d3cc1224/
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
