# Run Summary

**Run ID**: e9a39e57-ef11-4e6d-9d95-a9c600cb6aca
**Framework**: ghspec
**Started**: 2025-10-30T13:12:25.820667Z
**Completed**: 2025-10-30T13:37:26.498869Z
**Duration**: 1500.68s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 340.81 |
| 2 | 2 | completed | 0/0 | 0 | 168.35 |
| 3 | 3 | completed | 0/0 | 0 | 235.72 |
| 4 | 4 | completed | 0/0 | 0 | 273.81 |
| 5 | 5 | completed | 0/0 | 0 | 165.04 |
| 6 | 6 | completed | 0/0 | 0 | 316.94 |

## Directory Structure

```
e9a39e57-ef11-4e6d-9d95-a9c600cb6aca/
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
