import re
import json
import argparse
import sys

# WhatsApp format:
# [27/05/25, 9:39:15 PM] Name: Message
# Some lines begin with invisible LRM/U+200E, so we strip them.

line_pattern = re.compile(
    r'^.*\[(\d{1,2}\/\d{1,2}\/\d{2}),\s(\d{1,2}:\d{2}:\d{2}\s?[APap][Mm])\]\s(.+?):\s(.*)$'
)

def convert_whatsapp_to_json(input_file, output_file):
    chat_data = []
    current_message = None

    with open(input_file, 'r', encoding='utf-8') as f:
        for raw_line in f:
            # Remove newline, invisible chars, extra spaces
            line = raw_line.rstrip("\n")
            line = line.replace("\u200e", "").strip()

            match = line_pattern.match(line)

            if match:
                # If a previous message exists, finalize it
                if current_message:
                    chat_data.append(current_message)

                date, time, sender, message = match.groups()
                current_message = {
                    "date": date,
                    "time": time,
                    "sender": sender.strip(),
                    "message": message.strip()
                }
            else:
                # Continuation of previous message (multiline)
                if current_message:
                    current_message["message"] += "\n" + line

    # Add last message to JSON
    if current_message:
        chat_data.append(current_message)

    # Save as JSON
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(chat_data, out, indent=4, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Convert a WhatsApp chat export .txt file to JSON."
    )
    parser.add_argument("input", help="Path to WhatsApp txt export")
    parser.add_argument("output", help="Where to save JSON output")
    args = parser.parse_args()

    try:
        convert_whatsapp_to_json(args.input, args.output)
        print(f"Saved JSON to {args.output}")
    except Exception as e:
        print("Something exploded:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
