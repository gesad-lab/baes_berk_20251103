# Run Summary

**Run ID**: 741a3bb6-fbf9-4ede-b6fa-bba428f23daf
**Framework**: chatdev
**Started**: 2025-10-30T05:36:13.485281Z
**Completed**: 2025-10-30T05:53:34.175512Z
**Duration**: 1040.69s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 213.59 |
| 2 | 2 | completed | 0/0 | 0 | 125.69 |
| 3 | 3 | completed | 0/0 | 0 | 129.68 |
| 4 | 4 | completed | 0/0 | 0 | 214.15 |
| 5 | 5 | completed | 0/0 | 0 | 174.60 |
| 6 | 6 | completed | 0/0 | 0 | 182.96 |

## Directory Structure

```
741a3bb6-fbf9-4ede-b6fa-bba428f23daf/
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
