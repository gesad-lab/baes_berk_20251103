# Run Summary

**Run ID**: 715a30d1-24d7-4e4b-9c18-2183293dbeee
**Framework**: ghspec
**Started**: 2025-10-28T20:27:14.169142Z
**Completed**: 2025-10-28T20:46:34.173006Z
**Duration**: 1160.00s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 156.48 |
| 2 | 2 | completed | 0/0 | 0 | 160.03 |
| 3 | 3 | completed | 0/0 | 0 | 174.43 |
| 4 | 4 | completed | 0/0 | 0 | 270.51 |
| 5 | 5 | completed | 0/0 | 0 | 184.63 |
| 6 | 6 | completed | 0/0 | 0 | 213.92 |

## Directory Structure

```
715a30d1-24d7-4e4b-9c18-2183293dbeee/
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
