# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

This is Python learning repository organized into numbered sections covering core Python concepts:

- **section/** - Contains all learning materials organized in chapters
  - (一)python基础知识/ - Basic Python I/O, data types
  - (二)内置数据类型/ - Built-in structures (list, dict, tuple, set)
  - (三)循环与判断/ - Control flow (if/else, loops)
  - (四)输入输出与文件操作/ - I/O operations and file handling
  - (五)函数 - Functions and parameter handling
  - (六)类/ - Object-oriented programming concepts
  - (七)模块与标准库/ - Modules and standard libraries
  - (八)异常处理/ - Exception handling
  - (九)数据类型与算法/ - Advanced data types and algorithms

## Development Setup

### Environment Setup
- **Python Version**: 3.10.7
- **Environment**: Uses venv for virtual environments

### Commands
```bash
# Activate virtual environment
source venv/bin/

# Install dependencies
pip install -r requirements.txt

# Run any section file directly
python section/（章节名称）/文件名.py
```

## Key Dependencies
- PyMySQL: MySQL database operations
- Redis: Redis database operations 
- TinyDB: Simple JSON-based database
- Requests: HTTP requests
- Numpy: Numerical operations
- Pynput: Keyboard/mouse control

## Usage Pattern
Each file in the `section/` directory is a standalone runnable Python example. Files numbered sequentially and can be executed directly:

```bash
python section/（九）数据类型与算法/59.使用关系型数据库.py
```

## Testing
This is a learning repository - no formal test suite. Each script is self-contained and be run to verify understanding.