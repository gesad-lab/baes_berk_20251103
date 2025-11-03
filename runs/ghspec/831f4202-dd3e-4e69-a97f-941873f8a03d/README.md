# Run Summary

**Run ID**: 831f4202-dd3e-4e69-a97f-941873f8a03d
**Framework**: ghspec
**Started**: 2025-10-31T20:38:29.691637Z
**Completed**: 2025-10-31T20:58:07.310895Z
**Duration**: 1177.62s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 260.76 |
| 2 | 2 | completed | 0/0 | 0 | 124.69 |
| 3 | 3 | completed | 0/0 | 0 | 227.45 |
| 4 | 4 | completed | 0/0 | 0 | 180.36 |
| 5 | 5 | completed | 0/0 | 0 | 141.92 |
| 6 | 6 | completed | 0/0 | 0 | 242.43 |

## Directory Structure

```
831f4202-dd3e-4e69-a97f-941873f8a03d/
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
