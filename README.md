# Shodan MCP Toolkit

A Model Context Protocol (MCP) toolkit for integrating Shodan's powerful search and intelligence capabilities into your applications.

## Features
- Advanced Shodan search with filters and facets
- IP information lookup (open ports, services, location)
- DNS and reverse DNS lookups
- Domain info and subdomain enumeration
- On-demand scanning (requires upgraded Shodan API access)
- Network alert creation and management
- Vulnerability analysis with CVE tracking
- API usage and limits info
- Historical scan data (premium access required)

## Requirements
- Python 3.7+
- Shodan API key (set as the `SHODAN_API_KEY` environment variable)

## Installation
```bash
pip install .
```

## Configuration
Set your Shodan API key as an environment variable:
```bash
export SHODAN_API_KEY=your_shodan_api_key
```

Or use the console script (if installed):
```bash
shodan-mcp
```

## Usage
Run the MCP server:
```bash
python main.py
```

## License
MIT
