# Technical Documentation

<a id="h.nsznsrzup7z_l"></a>

## Data File Format {#h.nsznsrzup7z}

The data.crypt file is a binary file with the following structure:

| **Size:** | 512 bits | 128 bits | 32 bits | 16 bits | 16 bits | 32 bits | 32 bits | Variable length |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Encrypted:** | No | No | Yes | Yes | Yes | Yes | Yes | Yes |
| **Content:** | Random salt value (salt is generated during changing of password or during initial setup) | Random Initialization Vector value | String "TRUE" (used to detect successful unlock) | Format version: constant *1* | Reserved: constant *0* | CRC-32 checksum of data | Size of data | **Data**. Gzipped XML content with category definitions and entries. |

The whole file contains either random data (the Salt and the Initialization Vector) or encrypted data (the rest after the Initialization Vector). There is no plain text content. The whole file seems to contain random data (encrypted data also cannot be distinguished from random data). 

All categories and data entries including favorite category info are stored in the last part of the data.crypt file and is encrypted. Therefore any information about the entries data, number of categories, category names, favorite category, or number of entries is encrypted too and therefore hidden.

<a id="h.hfg08jjzww31_l"></a>

## Supported algorithms {#h.hfg08jjzww31}

| **Algorithm** | **Key sizes (bits)** |
| --- | --- |
| AES | 128, 192, 256 |

<a id="h.5dnbps6kxupf_l"></a>

## Supported cipher mode of operation {#h.5dnbps6kxupf}

| **Mode** |
| --- |
| CBC - Cipher Block Chaining |
| CFB - Cipher Feedback |
| OFB - Output Feedback |

<a id="h.61kxkgt8tycg_l"></a>

## Unlocking data file with master password and salt {#h.61kxkgt8tycg}

The data.crypt file is loaded into RAM and its first 512 bits are used as a 'salt' value. The next 128 bits are the IV (initialization vector) used by the AES cipher. The salt and the master password are passed to the SHA-256 hash function as initial values. The result is iterated 1000 times using SHA-256 to produce the 256-bit AES cipher key. This hashed value is saved temporarily into RAM as the cipher key (not the user-provided master password). The key is then used together with the IV to decrypt the remaining data using AES-256.

If the 'TRUE' string from the data.crypt file (byte positions 80–83) is successfully decrypted using AES-256 with the derived key and IV, the unlock is considered successful. The CRC-32 checksum and data length are then verified. Finally, the XML data is decompressed using GZIP and loaded into RAM.
