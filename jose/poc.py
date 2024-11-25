import argparse
import itertools

# Scans a memory dump file and returns candidates matching specific byte patterns
def get_candidates(dump_file):
    data = dump_file.read()
    
    # Initializes the list of candidate strings and a variable for tracking string lengths
    candidates = []
    str_len = 0
    i = 0

    # Loops through the data in the dump file
    while i < len(data)-1:
        # Checks for the pattern 0xCF 0x25 (potential start of a candidate string)
        if (data[i] == 0xCF) and (data[i + 1] == 0x25):
            str_len += 1
            i += 1
        elif str_len > 0:
            # Checks for valid printable characters followed by a null byte
            if (data[i] >= 0x20) and (data[i] <= 0x7E) and (data[i + 1] == 0x00):
                candidate = (str_len * b'\xCF\x25') + bytes([data[i], data[i + 1]])

                if not candidate in candidates:
                    candidates.append(candidate)
            
            str_len = 0
        
        i += 1
    
    return candidates


# Main entry point of the script
if __name__ == '__main__':
    # Parses the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('dump', type=str, help='The path of the memory dump to analyze')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='Enable debugging mode')
    args = parser.parse_args()

    # Opens the specified memory dump file for reading
    with open(args.dump, 'rb') as dump_file:
        candidates = get_candidates(dump_file)
        
        # Decodes the candidates to UTF-16-LE format
        candidates = [x.decode('utf-16-le') for x in candidates]

        groups = [[] for _ in range(max([len(i) for i in candidates]))]

        for candidate in candidates:
            groups[len(candidate) - 1].append(candidate[-1])
        
        for i in range(len(groups)):
            if len(groups[i]) == 0:
                groups[i].append(b'\xCF\x25'.decode('utf-16-le'))
        
        for password in itertools.product(*groups):
            password = ''.join(password)
            print(f'Possible password: {password}')
