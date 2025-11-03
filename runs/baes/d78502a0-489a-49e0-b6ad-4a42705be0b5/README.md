# Run Summary

**Run ID**: d78502a0-489a-49e0-b6ad-4a42705be0b5
**Framework**: baes
**Started**: 2025-10-30T06:50:20.513841Z
**Completed**: 2025-10-30T06:54:19.641977Z
**Duration**: 239.13s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.85 |
| 2 | 2 | completed | 0/0 | 0 | 34.16 |
| 3 | 3 | completed | 0/0 | 0 | 33.45 |
| 4 | 4 | completed | 0/0 | 0 | 33.29 |
| 5 | 5 | completed | 0/0 | 0 | 65.51 |
| 6 | 6 | completed | 0/0 | 0 | 39.86 |

## Directory Structure

```
d78502a0-489a-49e0-b6ad-4a42705be0b5/
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
