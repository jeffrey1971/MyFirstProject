# MyFirstProject

## Quick Start

1. **Read CLAUDE.md first** - Contains essential rules for Claude Code
2. Follow the pre-task compliance checklist before starting any work
3. Use proper module structure under `src/`
4. Commit after every completed task

## Project Overview

Simple Python project for AI hackathon development. Built with Claude Code template for rapid prototyping and clean architecture.

**Description**: It's for intenteal AI hackthon

## Project Structure

```
MyFirstProject/
├── CLAUDE.md              # Essential rules for Claude Code
├── README.md              # This file
├── .gitignore             # Git ignore patterns
├── src/                   # Source code (NEVER put files in root)
│   ├── main.py            # Main script/entry point
│   └── utils.py           # Utility functions
├── tests/                 # Test files
│   └── test_main.py       # Basic tests
├── docs/                  # Documentation
└── output/                # Generated output files
```

## Getting Started

### Run the project
```bash
python src/main.py
```

### Run tests
```bash
python tests/test_main.py
```

### Interactive development
```bash
python -c "import sys; sys.path.append('src'); import main, utils"
```

## Development Guidelines

- **Always search first** before creating new files
- **Extend existing** functionality rather than duplicating  
- **Use Task agents** for operations >30 seconds
- **Single source of truth** for all functionality
- **Language-agnostic structure** - works with Python, JS, Java, etc.
- **Scalable** - start simple, grow as needed

## Template Credits

🎯 Template by Chang Ho Chien | HC AI 說人話channel | v1.0.0  
📺 Tutorial: https://youtu.be/8Q1bRZaHH24