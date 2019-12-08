import textwrap


def get_layers(img, x, y):
    return textwrap.wrap(img, x*y)


if __name__ == "__main__":
    f = open("../inputs/day8.txt", "r")

    image = f.readline()

    pix_wide = 25
    pix_tall = 6

    layers = get_layers(image, pix_wide, pix_tall)

    min_z = 9999999999999999
    min_layer = []
    res = 0

    # PART 1
    for layer in layers:
        if layer.count('0') < min_z:
            min_z = layer.count('0')
            min_layer = layer
            res = layer.count('1')*layer.count('2')

    # PART 2
    decoded = list('2'*(pix_wide*pix_tall))
    for layer in layers:
        for i in range(len(decoded)):
            if decoded[i] == '2':
                decoded[i] = layer[i]

    l = textwrap.wrap("".join(decoded), pix_wide)

    print('The answer for the PART 1 is:', res)
    print('The answer for the PART 2 is:')
    for r in l:
        print(r.replace('0', ' '))



