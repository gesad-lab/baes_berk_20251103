# Run Summary

**Run ID**: 3a3cb4d4-9fa6-4ec8-8a3c-17c30e103c10
**Framework**: chatdev
**Started**: 2025-10-29T13:11:42.737725Z
**Completed**: 2025-10-29T13:29:28.381908Z
**Duration**: 1065.64s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 215.76 |
| 2 | 2 | completed | 0/0 | 0 | 185.51 |
| 3 | 3 | completed | 0/0 | 0 | 147.57 |
| 4 | 4 | completed | 0/0 | 0 | 152.33 |
| 5 | 5 | completed | 0/0 | 0 | 170.45 |
| 6 | 6 | completed | 0/0 | 0 | 194.01 |

## Directory Structure

```
3a3cb4d4-9fa6-4ec8-8a3c-17c30e103c10/
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
