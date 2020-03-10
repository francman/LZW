import sys

def compress():
    """Compress a string to a list of output symbols."""
    inputFile = sys.argv[1]
    
    with open(inputFile, "r") as uncompressedFile:
        uncompressed = uncompressedFile.read()
    
    outputFile = open((inputFile + '.lz78'), "w")
    # Build the dictionary.
    dict_size = 256
    # dictionary = dict((chr(i), i) for i in range(dict_size))
    dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    result.append(dictionary[w])
    
    outputFile.write(str(result))

if __name__ == "__main__":
    compress()