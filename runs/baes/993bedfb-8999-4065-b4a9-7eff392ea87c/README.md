# Run Summary

**Run ID**: 993bedfb-8999-4065-b4a9-7eff392ea87c
**Framework**: baes
**Started**: 2025-10-28T19:56:03.174028Z
**Completed**: 2025-10-28T19:59:26.145299Z
**Duration**: 202.97s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.36 |
| 2 | 2 | completed | 0/0 | 0 | 32.00 |
| 3 | 3 | completed | 0/0 | 0 | 39.19 |
| 4 | 4 | completed | 0/0 | 0 | 25.69 |
| 5 | 5 | completed | 0/0 | 0 | 34.55 |
| 6 | 6 | completed | 0/0 | 0 | 39.17 |

## Directory Structure

```
993bedfb-8999-4065-b4a9-7eff392ea87c/
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
