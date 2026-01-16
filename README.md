# Demo MCP Server

A simple Model Context Protocol (MCP) server built with FastMCP that provides utility tools for dice rolling and number addition.

## Prerequisites

- Python >= 3.11
- [UV](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Installation

1. Clone this repository or navigate to the project directory.

2. Install dependencies using UV:
```bash
uv sync
```

## Running the Server

### Development Mode (Testing)

To test the server with the MCP inspector in your browser, run:

```bash
uv run fastmcp dev main.py
```
OR 
```bash
fastmcp dev main.py
```

This will start the server in development mode and automatically open the MCP inspector in your browser, allowing you to test the available tools interactively.

### Production Mode

To run the server for production use:

```bash
uv run fastmcp run main.py
```
OR

```bash
fastmcp run main.py
```
This will start the server and make it available for MCP clients to connect.

## Installing to Claude Desktop

To add this local MCP server to Claude Desktop, run:

```bash
uv run fastmcp install claude-desktop main.py
```
OR
```bash
fastmcp install claude-desktop main.py
```

This will configure Claude Desktop to use this MCP server. 

**Note:** If `uv` is not in your system PATH, you may need to manually edit the Claude Desktop MCP configuration file and use the absolute path to `uv.exe` in the command. To find your UV installation path, use:

```bash
Get-Command uv | Select-Object -ExpandProperty Source
```

Then update the MCP server configuration in Claude Desktop's settings to use the absolute path (e.g., `C:\Users\Khushil\AppData\Local\Microsoft\WinGet\Links\uv.exe run fastmcp run main.py`).

After installation, restart Claude Desktop to start using the server.

## Available Tools

### 1. `roll_dice`
Roll one or more 6-sided dice.

**Parameters:**
- `n_dice` (int, default: 1): Number of dice to roll

**Returns:**
- List of integers representing the dice roll results

**Example:**
- Roll a single die: `roll_dice(1)` → `[4]`
- Roll multiple dice: `roll_dice(3)` → `[2, 5, 1]`

### 2. `add_numbers`
Add two numbers together.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:**
- Sum of the two numbers as a float

**Example:**
- `add_numbers(5, 3)` → `8.0`
- `add_numbers(10.5, 2.3)` → `12.8`

## Usage

This MCP server can be used with any MCP-compatible client. Once the server is running, clients can call the available tools (`roll_dice` and `add_numbers`) through the MCP protocol.

## Development

The server is built using [FastMCP](https://github.com/jlowin/fastmcp), which provides a simple and fast way to create MCP servers in Python.
