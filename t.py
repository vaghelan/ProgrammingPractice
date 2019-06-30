


def recommend_pair(product_pairs):
    bucket_num = 0
    category_buckets = {}

    product_to_bucket = {}

    for pair in product_pairs:
        if pair[0] in product_to_bucket:
            category_buckets[product_to_bucket[pair[0]]].add(pair[1])
            product_to_bucket[pair[1]] = product_to_bucket[pair[0]]
            continue
        if pair[1] in product_to_bucket:
            category_buckets[product_to_bucket[pair[1]]].add(pair[0])
            product_to_bucket[pair[0]] = product_to_bucket[pair[1]]
            continue

        category_buckets[bucket_num] = set()
        category_buckets[bucket_num].add(pair[0])
        category_buckets[bucket_num].add(pair[1])
        product_to_bucket[pair[0]] = bucket_num
        product_to_bucket[pair[1]] = bucket_num
        bucket_num = bucket_num + 1

    print (category_buckets)

    print (product_to_bucket)

    bucket_counts = {}
    for k in category_buckets:
        bucket_counts[k] = len(category_buckets[k])

    num_categories = len(category_buckets)

    print(bucket_counts)

    num_ways = 0

    for c in range(num_categories):
        for d in range(c+1, num_categories):
            num_ways = num_ways +  bucket_counts[c] * bucket_counts[d]

    return num_ways

input = [ (1, 3), (3, 5 ), (6, 7), (9, 10), (10,13)]

print(recommend_pair(input))

'''
def swap_bits(x, i , j):


    if x >> i & 1 != x >> j & 1:
        print("test")


swap_bits(1, )

'''