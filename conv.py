import binascii

p_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'
p = int(p_hex, 16)
compressed_key_hex = '03DFF1D77F2A671C5F36183726DB2341BE58FEAE1DA2DECED843240F7B502BA659'
x_hex = compressed_key_hex[2:66]
x = int(x_hex, 16)
prefix = compressed_key_hex[0:2]

y_square = (pow(x, 3, p)  + 7) % p
y_square_square_root = pow(y_square, (p+1)//4, p)
if prefix == "02":
    y = (-y_square_square_root) % p
else:
    y = y_square_square_root

computed_y_hex = hex(y)[2:66]
computed_uncompressed_key = "04" + x_hex + computed_y_hex

print(computed_uncompressed_key)
