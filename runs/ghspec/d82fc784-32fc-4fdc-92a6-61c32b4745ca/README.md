# Run Summary

**Run ID**: d82fc784-32fc-4fdc-92a6-61c32b4745ca
**Framework**: ghspec
**Started**: 2025-10-30T11:10:02.696248Z
**Completed**: 2025-10-30T11:27:11.657840Z
**Duration**: 1028.96s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 187.67 |
| 2 | 2 | completed | 0/0 | 0 | 142.76 |
| 3 | 3 | completed | 0/0 | 0 | 183.92 |
| 4 | 4 | completed | 0/0 | 0 | 152.50 |
| 5 | 5 | completed | 0/0 | 0 | 191.98 |
| 6 | 6 | completed | 0/0 | 0 | 170.13 |

## Directory Structure

```
d82fc784-32fc-4fdc-92a6-61c32b4745ca/
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
