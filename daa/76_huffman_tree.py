import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(chars, freqs):
    pq = [Node(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(pq)
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)
    return pq[0]
def generate_codes(root, current_code="", codes={}):
    if root is None: return
    if root.char is not None:
        codes[root.char] = current_code
        return
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes
def huffman_coding(chars, freqs):
    root = build_huffman_tree(chars, freqs)
    codes = {}
    generate_codes(root, "", codes)
    return sorted(codes.items())
print(f"Huffman Codes 1: {huffman_coding(['a','b','c','d'], [5,9,12,13])}")
print(f"Huffman Codes 2: {huffman_coding(['f','e','d','c','b','a'], [5,9,12,13,16,45])}")