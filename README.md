# WaConv
WhatsApp to JSON converter

WaConv converts exported WhatsApp chat text files into JSON for easier analysis and processing.

Features
- Parse exported WhatsApp chat `.txt` files
- Produce structured JSON with message timestamp, sender, and content

Getting started

1. Requirements

- Python 3.8+ (or your system Python)

2. Install

No external dependencies required for the simple converter. Run directly with Python:

```powershell
python waconv.py <path-to-exported-chat.txt> > output.json
```

Usage

- Replace `<path-to-exported-chat.txt>` with the path to your WhatsApp chat export.
- The script writes JSON to stdout so you can redirect it to a file (as shown above).

License

This project is licensed under the MIT License - see the `LICENSE` file for details.
