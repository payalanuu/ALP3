import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code, huffman_codes):

    if root is None:
        return

    # If leaf node, store the code
    if root.char is not None:
        huffman_codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# Huffman Encoding Function
def huffman_encoding(chars, freq):

    heap = []

    # Insert characters into min heap
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freq[i]))

    # Build Huffman Tree
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)

        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    # Generate Huffman Codes
    root = heap[0]

    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    print("\nHuffman Codes:")

    for char in chars:
        print(char, ":", huffman_codes[char])


# Main Program
n = int(input("Enter number of characters: "))

if n <= 0:
    print("Number of characters must be positive.")

else:
    chars = input("Enter characters separated by space: ").split()

    if len(chars) != n or len(set(chars)) != n:
        print("Enter exactly", n, "unique characters.")

    else:
        freq = list(map(int, input("Enter frequencies: ").split()))

        if len(freq) != n or any(f <= 0 for f in freq):
            print("Enter exactly", n, "positive frequencies.")

        else:
            huffman_encoding(chars, freq)


#Input=
#Enter number of characters: 5
#Enter characters separated by space: A B C D E
#Enter frequencies: 5 9 12 13 16

#Output=
#Huffman Codes:
#A : 1100
#B : 1101
#C : 100
#D : 101
#E : 0