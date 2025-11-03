# Run Summary

**Run ID**: 023347f6-966e-4b16-b14c-f19c59a9b98b
**Framework**: chatdev
**Started**: 2025-10-30T01:10:26.807002Z
**Completed**: 2025-10-30T01:30:24.522457Z
**Duration**: 1197.72s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 249.29 |
| 2 | 2 | completed | 0/0 | 0 | 178.63 |
| 3 | 3 | completed | 0/0 | 0 | 162.85 |
| 4 | 4 | completed | 0/0 | 0 | 257.27 |
| 5 | 5 | completed | 0/0 | 0 | 173.34 |
| 6 | 6 | completed | 0/0 | 0 | 176.33 |

## Directory Structure

```
023347f6-966e-4b16-b14c-f19c59a9b98b/
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
