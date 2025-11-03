# Run Summary

**Run ID**: 29e9089c-bdbb-431c-9964-d2991fc50893
**Framework**: chatdev
**Started**: 2025-10-29T08:44:27.687923Z
**Completed**: 2025-10-29T09:06:47.330224Z
**Duration**: 1339.64s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 186.10 |
| 2 | 2 | completed | 0/0 | 0 | 190.97 |
| 3 | 3 | completed | 0/0 | 0 | 198.37 |
| 4 | 4 | completed | 0/0 | 0 | 218.63 |
| 5 | 5 | completed | 0/0 | 0 | 268.04 |
| 6 | 6 | completed | 0/0 | 0 | 277.52 |

## Directory Structure

```
29e9089c-bdbb-431c-9964-d2991fc50893/
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
