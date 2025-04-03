from CustomHashForCryptography import custom_hash_function


# avalanche effect test
def test_avalanche_effect():
    input1 = b"Temperature: 19.70 Humidity: 46.20 Sound: 239"
    input2 = b"Temperature: 19.70 Humidity: 46.20 Sound: 240"  # one character change

    hash1 = custom_hash_function(input1).hex()
    hash2 = custom_hash_function(input2).hex()

    print("avalanche test")
    print("input 1:", input1)
    print("hash 1 :", hash1)
    print("input 2:", input2)
    print("hash 2 :", hash2)

    # Count differing bits
    bin1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
    bin2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
    diff_bits = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
    print("differing bits:", diff_bits, "out of", len(bin1))


# collision resistance test
def test_collision_resistance():
    print("collision resistance")
    hashes = set()
    collision_found = False
    test_inputs = [f"test_input_{i}".encode() for i in range(1000)]

    for data in test_inputs:
        digest = custom_hash_function(data).hex()
        if digest in hashes:
            print("collision detected:", data)
            collision_found = True
            break
        hashes.add(digest)

    if not collision_found:
        print("no collisions detected in inputs")


# pre-image resistance test
def test_pre_image_resistance():
    print("pre-image resistance")
    target = custom_hash_function(b"secret message").hex()

    brute_force_found = False
    for i in range(100000):  # brute force
        test_input = str(i).encode()
        if custom_hash_function(test_input).hex() == target:
            print("pre-image found:", test_input)
            brute_force_found = True
            break

    if not brute_force_found:
        print("no pre-image found")


if __name__ == "__main__":
    test_avalanche_effect()
    test_collision_resistance()
    test_pre_image_resistance()
