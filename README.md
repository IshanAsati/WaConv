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
python waconv.py <path-to-exported-chat.txt> <output.json>
```

Usage

- Replace `<path-to-exported-chat.txt>` with the path to your WhatsApp chat export.
- Replace `<output.json>` with your desired output filename.

Sample Output

The generated JSON will look like this:

```json
[
    {
        "date": "27/05/25",
        "time": "9:39:15 PM",
        "sender": "Alice",
        "message": "Hey, how are you?"
    },
    {
        "date": "27/05/25",
        "time": "9:40:00 PM",
        "sender": "Bob",
        "message": "I'm good! Just working on a project.\nHow about you?"
    }
]
```

License

This project is licensed under the MIT License - see the `LICENSE` file for details.
