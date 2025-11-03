# Run Summary

**Run ID**: 5504cc3e-cadd-498b-8b04-848d1aee7437
**Framework**: ghspec
**Started**: 2025-10-31T10:31:41.082264Z
**Completed**: 2025-10-31T10:50:16.130328Z
**Duration**: 1115.05s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 204.90 |
| 2 | 2 | completed | 0/0 | 0 | 234.22 |
| 3 | 3 | completed | 0/0 | 0 | 142.52 |
| 4 | 4 | completed | 0/0 | 0 | 203.69 |
| 5 | 5 | completed | 0/0 | 0 | 183.57 |
| 6 | 6 | completed | 0/0 | 0 | 146.13 |

## Directory Structure

```
5504cc3e-cadd-498b-8b04-848d1aee7437/
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
