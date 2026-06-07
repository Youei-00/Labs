import sys

def parse_args(args):
    options = {
        "V": False,
        "C": False,
        "N": False,
        "I": False
    }
    string = None
    files = []

    i = 0
    while i < len(args):
        arg = args[i]

        if arg.startswith('/'):
            opt = arg[1:].upper()
            if opt in options:
                options[opt] = True
        elif string is None:
            string = arg.strip('"')
        else:
            files.append(arg)
        i += 1

    return options, string, files


def process_file(filename, options, search_string):
    try:
        with open(filename, 'r', errors='ignore') as f:
            lines = f.readlines()
    except:
        print(f"FIND: Cannot open {filename}")
        return

    count = 0
    results = []

    for idx, line in enumerate(lines, start=1):
        text = line.rstrip('\n')

        if options["I"]:
            match = search_string.lower() in text.lower()
        else:
            match = search_string in text

        if options["V"]:
            match = not match

        if match:
            count += 1
            if not options["C"]:
                if options["N"]:
                    results.append(f"{idx}:{text}")
                else:
                    results.append(text)

    if options["C"]:
        print(f"{filename}:{count}" if filename else count)
    else:
        for r in results:
            print(r)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: FIND [/V] [/C] [/N] [/I] \"string\" filename")
        return

    options, search_string, files = parse_args(args)

    if search_string is None:
        print("FIND: Missing search string")
        return

    if not files:
        # read from stdin
        lines = sys.stdin.readlines()
        count = 0

        for idx, line in enumerate(lines, start=1):
            text = line.rstrip('\n')

            if options["I"]:
                match = search_string.lower() in text.lower()
            else:
                match = search_string in text

            if options["V"]:
                match = not match

            if match:
                count += 1
                if not options["C"]:
                    if options["N"]:
                        print(f"{idx}:{text}")
                    else:
                        print(text)

        if options["C"]:
            print(count)
    else:
        for file in files:
            process_file(file, options, search_string)


if __name__ == "__main__":
    main()