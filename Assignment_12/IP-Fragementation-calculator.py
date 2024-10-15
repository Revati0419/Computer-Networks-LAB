def ip_fragmentation_calculator(total_packet_size, mtu, ip_header_size):
    # Constants
    max_payload_size = mtu - ip_header_size  # Maximum payload in each fragment
    fragment_payload_size = (max_payload_size // 8) * 8  # Ensure payload size is a multiple of 8
    total_payload_size = total_packet_size - ip_header_size  # Total payload size to fragment

    # Initialize variables
    fragment_list = []
    offset = 0  # Fragment offset in 8-byte blocks
    more_fragments = 1  # More fragments flag (1 = more fragments, 0 = last fragment)

    # Fragmentation process
    while total_payload_size > fragment_payload_size:
        fragment_size = fragment_payload_size + ip_header_size
        fragment_list.append({
            "Fragment Size": fragment_size,
            "Offset": offset,
            "MF": more_fragments
        })

        total_payload_size -= fragment_payload_size
        offset += fragment_payload_size // 8  # Update offset in 8-byte blocks

    # Add the last fragment
    more_fragments = 0  # Last fragment has MF = 0
    last_fragment_size = total_payload_size + ip_header_size
    fragment_list.append({
        "Fragment Size": last_fragment_size,
        "Offset": offset,
        "MF": more_fragments
    })

    return fragment_list


# Example usage with user input
def main():
    try:
        total_packet_size = int(input("Enter the total packet size (in bytes, including IP header): "))
        mtu = int(input("Enter the Maximum Transmission Unit (MTU) size (in bytes): "))
        ip_header_size = int(input("Enter the IP header size (in bytes): "))

        if total_packet_size <= 0 or mtu <= 0 or ip_header_size <= 0:
            print("All input values must be positive integers.")
            return

        if ip_header_size >= mtu:
            print("Error: IP header size must be smaller than the MTU.")
            return

        fragments = ip_fragmentation_calculator(total_packet_size, mtu, ip_header_size)

        # Output the fragmentation result
        print("\nFragmentation Details:")
        for i, fragment in enumerate(fragments):
            print(f"Fragment {i + 1}: Size = {fragment['Fragment Size']} bytes, "
                  f"Offset = {fragment['Offset']} (in 8-byte blocks), MF = {fragment['MF']}")

    except ValueError:
        print("Please enter valid integer values for packet size, MTU, and header size.")


if __name__ == "__main__":
    main()
