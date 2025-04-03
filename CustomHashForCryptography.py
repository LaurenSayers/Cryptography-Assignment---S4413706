

S_BOX = [ #sbox implementation
    0xC, 0x5, 0x6, 0xB,
    0x9, 0x0, 0xA, 0xD,
    0x3, 0xE, 0xF, 0x8,
    0x4, 0x7, 0x1, 0x2
]

STATE_SIZE = 32 #32 bytes = 256 bits

def initialise_state(input_bytes): #initialise state for fixed size input
    state = bytearray(STATE_SIZE)
    for i in range(min(len(input_bytes), STATE_SIZE)):
        state[i] = input_bytes[i]
    return state

def apply_sbox(state): #applying sbox to each nibble
    new_state = bytearray(len(state))
    for i in range(len(state)):
        high_nibble = (state[i] >> 4) & 0xF
        low_nibble = (state[i] & 0xF)
        substituted = (S_BOX[high_nibble] << 4) | S_BOX[low_nibble]
        new_state[i] = substituted
    return new_state

def permute(state): #simple permutation
    perm = [
        0, 5, 10, 15, 20, 25, 30, 1,
        6, 11, 16, 21, 26, 31, 2, 7,
        12, 17, 22, 27, 3, 8, 13, 18,
        23, 28, 4, 9, 14, 19, 24, 29
    ]
    return bytearray([state[i] for i in perm])

NUM_ROUNDS = 10

def xor_with_round(state, round_num): #xor with round number
    return bytearray([(b ^ (round_num + i )) & 0xFF for i, b in enumerate(state)])

def custom_hash_function(input_data):#photon inspired custom hash
    state = bytearray(STATE_SIZE)

    for i in range(len(input_data)): #absorbing input in sponge-like structure
        state[i % STATE_SIZE] ^= input_data[i]

    for round_num in range(NUM_ROUNDS): #applying spn rounds
        state = apply_sbox(state)
        state = permute(state)
        state = xor_with_round(state, round_num)

    return state
