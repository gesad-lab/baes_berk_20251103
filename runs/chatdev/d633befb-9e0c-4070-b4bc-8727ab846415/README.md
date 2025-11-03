# Run Summary

**Run ID**: d633befb-9e0c-4070-b4bc-8727ab846415
**Framework**: chatdev
**Started**: 2025-10-30T12:15:44.795918Z
**Completed**: 2025-10-30T12:33:58.406622Z
**Duration**: 1093.61s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 156.73 |
| 2 | 2 | completed | 0/0 | 0 | 155.77 |
| 3 | 3 | completed | 0/0 | 0 | 187.58 |
| 4 | 4 | completed | 0/0 | 0 | 187.77 |
| 5 | 5 | completed | 0/0 | 0 | 189.06 |
| 6 | 6 | completed | 0/0 | 0 | 216.69 |

## Directory Structure

```
d633befb-9e0c-4070-b4bc-8727ab846415/
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
