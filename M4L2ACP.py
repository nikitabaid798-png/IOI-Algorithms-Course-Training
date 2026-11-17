
# =================================
# SMART HOME: BIT CONTROL SYSTEM
# =================================
# Topics:
# Set Bits and Zero Bits
# Counting Set Bits
# First Set Bit
# Creating Bit Masks
# Checking Individual Bits

# Each binary position controls a smart device:
# Bit 0 = Living Room Light
# Bit 1 = Fan
# Bit 2 = Air Conditioner
# Bit 3 = Door Lock
# Bit 4 = Garden Light
# Bit 5 = Security Camera

device_code = 45  # Binary representation: 101101


def binary_display(value):
    return bin(value)[2:]


print("================================")
print("MY SMART SWITCH BIT MONITOR")
print("================================")

print("Switch Value:", device_code)
print("Binary Form:", binary_display(device_code))


# ---------------------------------
# PART 1 - SET BITS AND ZERO BITS
# ---------------------------------

binary_code = binary_display(device_code)

on_bits = binary_code.count("1")
off_bits = binary_code.count("0")

print("\nPART 1: Set Bits and Zero Bits")
print("Set Bits / ON Switches:", on_bits)
print("Zero Bits / OFF Switches:", off_bits)


# ---------------------------------
# PART 2 - COUNTING SET BITS
# ---------------------------------

one_count = 0
remaining_value = device_code

while remaining_value > 0:
    last_bit = remaining_value & 1

    if last_bit == 1:
        one_count += 1

    remaining_value >>= 1

print("\nPART 2: Counting Set Bits")
print("Number of ON switches:", one_count)


# ---------------------------------
# PART 3 - FINDING THE FIRST SET BIT
# ---------------------------------

switch_position = 1
remaining_value = device_code

while remaining_value > 0:
    if remaining_value & 1:
        break

    switch_position += 1
    remaining_value >>= 1

print("\nPART 3: The First Set Bit")
print("First ON switch is at position:", switch_position)


# ---------------------------------
# PART 4 - CREATING BIT MASKS
# ---------------------------------

print("\nPART 4: Building a Bit Mask")

for position in range(6):
    current_mask = 1 << position

    print("Bit", position,
          "Mask:", current_mask,
          "Binary:", binary_display(current_mask))


# ---------------------------------
# PART 5 - CHECKING INDIVIDUAL BITS
# ---------------------------------

devices = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera"
]

print("\nPART 5: Check if the Nth Bit is Set")

for position in range(6):
    current_mask = 1 << position

    if device_code & current_mask:
        print("Bit", position, "-", devices[position], "is ON")
    else:
        print("Bit", position, "-", devices[position], "is OFF")


# ---------------------------------
# FINAL SUMMARY
# ---------------------------------

print("\n================================")
print("SMART SWITCH SUMMARY")
print("================================")

print("Switch Value:", device_code)
print("Binary Form:", binary_display(device_code))
print("Total ON Switches:", one_count)
print("First ON Switch Position:", switch_position)

print("================================")
