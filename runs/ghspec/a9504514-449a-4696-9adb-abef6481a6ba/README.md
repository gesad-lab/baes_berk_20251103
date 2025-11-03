# Run Summary

**Run ID**: a9504514-449a-4696-9adb-abef6481a6ba
**Framework**: ghspec
**Started**: 2025-10-30T06:31:35.147434Z
**Completed**: 2025-10-30T06:50:19.098523Z
**Duration**: 1123.95s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 171.23 |
| 2 | 2 | completed | 0/0 | 0 | 122.14 |
| 3 | 3 | completed | 0/0 | 0 | 161.44 |
| 4 | 4 | completed | 0/0 | 0 | 314.58 |
| 5 | 5 | completed | 0/0 | 0 | 171.48 |
| 6 | 6 | completed | 0/0 | 0 | 183.07 |

## Directory Structure

```
a9504514-449a-4696-9adb-abef6481a6ba/
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
