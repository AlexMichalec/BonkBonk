import sys, random, time, bext

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

SIZE = 3
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    print("\nTry to relax while watching falling boxes ^^\n")
    time.sleep(1)
    print("How many colors do you want to use (1-7)")
    i = input()
    while i not in ("1234567"):
        i = input("\nGive me a number (1-7)\n")
    our_colors = random.sample(COLORS, int(i))
    print("\nChoose speed of falling down (1-5) (1-slow/5-fast)")
    i = input()
    while i not in ("12345"):
        i = input("\nGive me a number (1-5)\n")
    pause_amount = 0.2 - 0.04*int(i)

    bext.clear()
    boxes = []
    boxes.append({X: random.randint(SIZE, WIDTH - 4),
                  Y: 0,
                  COLOR: random.choice(our_colors)})
    boxes[-1][X] = boxes[-1][X] - boxes[-1][X] % SIZE
    cigd = {}
    cigd[(boxes[-1][X], boxes[-1][Y])] = False
    done = False
    while True:
        togo = []
        if not done and random.randint(1,10)>3:
            boxes.append({X: random.randint(SIZE,WIDTH-4),
                          Y: 0,
                          COLOR: random.choice(our_colors)})
            boxes[-1][X] = boxes[-1][X] - boxes[-1][X]%SIZE
            cigd [(boxes[-1][X],boxes[-1][Y])] = False

        for b in boxes:
            if (b[X],b[Y]+1) not in cigd.keys():
                cigd[(b[X],b[Y]+1)] = False
                cigd[(b[X], b[Y])] = True
                b[Y] += 1
            elif cigd[(b[X],b[Y]+1)]:
                cigd[(b[X], b[Y] + 1)] = False
                cigd[(b[X], b[Y])] = True
                b[Y] += 1
            else:
                togo.append(b)
                continue
            bext.goto(b[X], b[Y]-1)
            print("   ", end="")
            bext.goto(b[X], b[Y])
            bext.fg(b[COLOR])
            print("███", end="")

        boxes = [b for b in boxes if b[Y]<HEIGHT-1 and b not in togo]

        if len(boxes) == 0:
            bext.fg("white")
            bext.goto(0, 0)
            print("It's done, thanks for watching ^^")
            time.sleep(1)
            print("\nDo you want to start over? (Y/N)")
            if input().upper() == "Y":
                main()
            return

        for t in togo:
            if t[Y] == 1:
                done = True

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(pause_amount)

if __name__ == '__main__':
    main()
