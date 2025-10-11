from random import randint

# ---------- Basic math algorithms ----------
def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclidean algorithm"""
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a, b):
    """Extended Euclidean Algorithm for modular inverses"""
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

def mod_exp(base, exp, mod):
    """Modular exponentiation using fast exponentiation method"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# ---------- Miller-Rabin primality test ----------
def power_mod(b, e, m):
    """Alternative modular exponentiation (for Miller-Rabin)"""
    x = 1
    while e > 0:
        if e % 2 == 1:
            x = (b * x) % m
        b = (b * b) % m
        e //= 2
    return x

def is_strong_pseudoprime(n, a):
    """Strong pseudoprime test for a single base"""
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    t = power_mod(a, d, n)
    if t == 1 or t == n - 1:
        return True
    for _ in range(s - 1):
        t = (t * t) % n
        if t == n - 1:
            return True
    return False

def is_prime(n, rounds=8):
    """Miller-Rabin primality test with multiple rounds"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False
    for _ in range(rounds):
        a = randint(2, n - 2)
        if not is_strong_pseudoprime(n, a):
            return False
    return True

# ---------- Chinese Remainder Theorem ----------
def CRT(c, d, p, q):
    """Chinese Remainder Theorem for fast RSA decryption"""
    c1 = pow(c, d % (p - 1), p)
    c2 = pow(c, d % (q - 1), q)
    _, q_inv, _ = extended_euclid(q, p)
    q_inv %= p
    h = (q_inv * (c1 - c2)) % p
    m = c2 + h * q
    return m

# ---------- RSA Core Functions ----------
def generate_rsa_keys(key_size=16):
    """Generate RSA public and private keys"""
    while True:
        p = randint(2**(key_size-1), 2**key_size)
        if is_prime(p):
            break
    while True:
        q = randint(2**(key_size-1), 2**key_size)
        if is_prime(q) and q != p:
            break
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Common public exponent
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    
    # Calculate private exponent
    _, d, _ = extended_euclid(e, phi)
    d %= phi
    if d < 0:
        d += phi
    
    public_key = (n, e)
    private_key = (n, d, p, q)
    
    return public_key, private_key

def encrypt(message, public_key):
    """Encrypt a message using RSA public key"""
    n, e = public_key
    return mod_exp(message, e, n)

def decrypt(cipher, private_key):
    """Decrypt a cipher using RSA private key with CRT"""
    n, d, p, q = private_key
    return CRT(cipher, d, p, q)

# ---------- Text and File Utilities ----------
def text_to_number(text):
    """Convert text to integer for encryption"""
    return int.from_bytes(text.encode('utf-8'), 'big')

def number_to_text(number):
    """Convert integer back to text after decryption"""
    if number == 0:
        return ''
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, 'big').decode('utf-8')

def file_to_number(file_path):
    """Read file and convert to integer"""
    with open(file_path, 'rb') as f:
        return int.from_bytes(f.read(), 'big')

def number_to_file(number, file_path):
    """Convert integer back to file"""
    byte_length = (number.bit_length() + 7) // 8
    with open(file_path, 'wb') as f:
        f.write(number.to_bytes(byte_length, 'big'))

def save_key_to_file(key, filename):
    """Save RSA key to text file"""
    with open(filename, 'w') as f:
        f.write(','.join(str(x) for x in key))

def load_key_from_file(filename):
    """Load RSA key from text file"""
    with open(filename, 'r') as f:
        return tuple(map(int, f.read().split(',')))

# ---------- Safe Encryption with Validation ----------
def safe_encrypt_text(text, public_key):
    """Safely encrypt text with size validation"""
    n, e = public_key
    number_msg = text_to_number(text)
    
    # Check if message is too large
    if number_msg >= n:
        raise ValueError(f"Message too large for key. Max: {n.bit_length()} bits, Got: {number_msg.bit_length()} bits")
    
    return encrypt(number_msg, public_key)

def safe_decrypt_text(cipher, private_key):
    """Safely decrypt to text"""
    decrypted_number = decrypt(cipher, private_key)
    return number_to_text(decrypted_number)

# ---------- Key Information ----------
def get_key_info(key):
    """Get information about RSA key"""
    if len(key) == 2:  # Public key
        n, e = key
        return f"RSA Public Key - Bits: {n.bit_length()}, Exponent: {e}"
    else:  # Private key
        n, d, p, q = key
        return f"RSA Private Key - Bits: {n.bit_length()}, Primes: {p.bit_length()}/{q.bit_length()} bits"