def get_loop_size(subject_number, public_key):
    val = 1
    loop_size = 0
    while val != public_key:
        val = val * subject_number
        val = val % 20201227
        loop_size += 1
    return loop_size


def get_encryption_key(subject_number, loop_size):
    val = 1
    for i in range(0, loop_size):
        val = val * subject_number
        val = val % 20201227
    return val


sub_num = 7
card_pub_key = 19241437
door_pub_key = 17346587
card_ls = get_loop_size(sub_num, card_pub_key)
door_ls = get_loop_size(sub_num, door_pub_key)
card_encryption_key = get_encryption_key(door_pub_key, card_ls)
door_encryption_key = get_encryption_key(card_pub_key, door_ls)
print(card_encryption_key)
print(door_encryption_key)
