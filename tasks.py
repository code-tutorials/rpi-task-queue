import rsa

# hostname for the redis server
REDIS_HOST = 'silver'

def newkeys(bits):
    pub, pri = rsa.newkeys(bits)
    return pub, pri
