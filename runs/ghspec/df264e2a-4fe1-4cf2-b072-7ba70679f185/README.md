# Run Summary

**Run ID**: df264e2a-4fe1-4cf2-b072-7ba70679f185
**Framework**: ghspec
**Started**: 2025-10-30T09:06:44.218909Z
**Completed**: 2025-10-30T09:23:59.462341Z
**Duration**: 1035.24s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 169.63 |
| 2 | 2 | completed | 0/0 | 0 | 166.06 |
| 3 | 3 | completed | 0/0 | 0 | 194.51 |
| 4 | 4 | completed | 0/0 | 0 | 186.61 |
| 5 | 5 | completed | 0/0 | 0 | 144.92 |
| 6 | 6 | completed | 0/0 | 0 | 173.51 |

## Directory Structure

```
df264e2a-4fe1-4cf2-b072-7ba70679f185/
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
