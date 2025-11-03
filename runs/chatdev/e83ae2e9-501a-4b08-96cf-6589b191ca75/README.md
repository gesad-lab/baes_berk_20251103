# Run Summary

**Run ID**: e83ae2e9-501a-4b08-96cf-6589b191ca75
**Framework**: chatdev
**Started**: 2025-10-30T02:33:54.395750Z
**Completed**: 2025-10-30T03:01:35.853307Z
**Duration**: 1661.46s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 283.10 |
| 2 | 2 | completed | 0/0 | 0 | 230.34 |
| 3 | 3 | completed | 0/0 | 0 | 218.86 |
| 4 | 4 | completed | 0/0 | 0 | 254.36 |
| 5 | 5 | completed | 0/0 | 0 | 381.48 |
| 6 | 6 | completed | 0/0 | 0 | 293.31 |

## Directory Structure

```
e83ae2e9-501a-4b08-96cf-6589b191ca75/
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
