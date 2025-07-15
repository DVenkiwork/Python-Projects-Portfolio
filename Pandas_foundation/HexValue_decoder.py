import pandas as pd

"""
Objective: Automate the decoding of 32-bit hexadecimal values from a CSV file.

This script reads a CSV containing 32-bit hexadecimal strings, extracts specific
bit ranges based on a configurable list (using 1-based indexing), and converts
them into decimal, hexadecimal, and optionally octal formats. It also applies
custom scaling factors to certain decoded decimal values.

This tool is designed for efficiently parsing packed data from sources like
sensor logs, register values, or communication protocols, transforming raw hex
into meaningful numerical representations for analysis.
"""

# --- Configuration (UPDATE THESE VALUES) ---
CSV_FILE_PATH = 'TARA1_Display.csv' # Path to your CSV file
HEX_COLUMN_NAME = 'RawLabel' # Name of the column with 32-bit hex values

# SCALING_FACTORS dictionary has been removed as requested.

# Define a list of bit ranges you want to extract and decode
# IMPORTANT: Use 1-based indexing for 'lsb' and 'msb' here!
# Ensure 'include_octal' is always present for clarity.
BIT_RANGES_TO_DECODE = [
    {'name': 'Message_ID', 'lsb': 1, 'msb': 8, 'include_octal': True},
    {'name': 'Data_Length', 'lsb': 9, 'msb': 16, 'include_octal': False},
    {'name': 'Alert_Threshold', 'lsb': 20, 'msb': 24, 'include_octal': False},
    {'name': 'Vertical_Offset', 'lsb': 22, 'msb': 28, 'include_octal': False},
    {'name': 'Vertical_Sign', 'lsb': 29, 'msb': 29, 'include_octal': False},
    {'name': 'Object_Distance', 'lsb': 19, 'msb': 29, 'include_octal': False},
    {'name': 'Object_ID', 'lsb': 11, 'msb': 15, 'include_octal': False},
    {'name': 'Azimuth_Angle', 'lsb': 19, 'msb': 28, 'include_octal': False},
    {'name': 'Azimuth_Sign', 'lsb': 29, 'msb': 29, 'include_octal': False},
]

# --- Function to decode a single 32-bit hex value ---
def decode_hex_value(hex_str, lsb_1_based, msb_1_based):
    """
    Decodes a specific bit range (1-based LSB to 1-based MSB) from a 32-bit hex string.

    Args:
        hex_str (str): The 32-bit hex value (e.g., "0xABCD1234" or "ABCD1234").
        lsb_1_based (int): Least Significant Bit position (1-indexed).
        msb_1_based (int): Most Significant Bit position (1-indexed).

    Returns:
        tuple: (decoded_decimal, decoded_hex_str, decoded_octal_str)
               Returns (None, None, None) if hex_str or bit range is invalid.
    """
    if not isinstance(hex_str, str):
        return None, None, None

    hex_str = hex_str.lower().replace('0x', '')

    try:
        full_int_value = int(hex_str, 16)
    except ValueError:
        print(f"Warning: Invalid hex string '{hex_str}' found. Skipping.")
        return None, None, None

    lsb_0_based = lsb_1_based - 1
    msb_0_based = msb_1_based - 1

    if not (1 <= lsb_1_based <= 32 and 1 <= msb_1_based <= 32 and lsb_1_based <= msb_1_based):
        print(f"Warning: Invalid 1-based bit range ({lsb_1_based}-{msb_1_based}) for 32-bit value. Must be between 1 and 32, with LSB <= MSB.")
        return None, None, None

    bit_width = msb_0_based - lsb_0_based + 1
    mask = (1 << bit_width) - 1
    decoded_value = (full_int_value >> lsb_0_based) & mask

    decoded_hex_str = hex(decoded_value)
    decoded_oct_str = oct(decoded_value)

    return decoded_value, decoded_hex_str, decoded_oct_str

# --- Main Automation Logic ---
if __name__ == "__main__":
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(f"Successfully loaded {CSV_FILE_PATH}")
        print("Original DataFrame head:")
        print(df.head())

        if HEX_COLUMN_NAME not in df.columns:
            raise ValueError(f"Column '{HEX_COLUMN_NAME}' not found in CSV.")

        # Iterate through each defined bit range and add new columns
        for bit_range in BIT_RANGES_TO_DECODE:
            name = bit_range['name']
            lsb = bit_range['lsb']
            msb = bit_range['msb']
            include_octal = bit_range['include_octal']

            print(f"\nDecoding range: {name} (1-based LSB: {lsb}, 1-based MSB: {msb})")

            # Apply the decoding function. decoded_results_series is a Series of (dec, hex, oct) tuples.
            decoded_results_series = df[HEX_COLUMN_NAME].apply(lambda x: decode_hex_value(x, lsb, msb))

            # Assign Decimal column
            df[f'{name}_Decimal'] = decoded_results_series.apply(lambda x: x[0])

            # Assign Hex column
            df[f'{name}_Hex'] = decoded_results_series.apply(lambda x: x[1])

            # Conditionally assign Octal column
            if include_octal:
                df[f'{name}_Octal'] = decoded_results_series.apply(lambda x: x[2])

        print("\n--- Decoding Complete ---")
        print("Updated DataFrame head with decoded values:")
        print(df.head())

        # Optional: Save the results to a new CSV
        OUTPUT_CSV_PATH = 'decoded_data.csv'
        df.to_csv(OUTPUT_CSV_PATH, index=False)
        print(f"\nDecoded data saved to {OUTPUT_CSV_PATH}")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {CSV_FILE_PATH}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")