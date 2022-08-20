# https://www.acmicpc.net/problem/1063
import sys
input = sys.stdin.readline


class Position:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        char_x = chr(self.x+65)  # ascii 알파벳 대문자로 변환
        return f'{char_x}{self.y+1}'


def main():
    commands = {
        "R": Position(0, 1),
        "RB": Position(-1, 1),
        "B": Position(-1, 0),
        "LB": Position(-1, -1),
        "L": Position(0, -1),
        "LT": Position(1, -1),
        "T": Position(1, 0),
        "RT": Position(1, 1),
    }
    k, s, move_cnt = input().strip().split()

    # ord(k[0] - 65 알파벳 대문자 -> Index  ex) 'A' -> 0
    k_pos = Position(int(k[1])-1, ord(k[0]) - 65)
    s_pos = Position(int(s[1])-1, ord(s[0]) - 65)

    # 이동 횟수 만큼 순환
    for _ in range(int(move_cnt)):
        command = input().strip()  # ex) 'T'
        ny = k_pos.y + commands[command].y  # ex) + 1
        nx = k_pos.x + commands[command].x  # ex) + 0

        # king이 체스판을 벗어 날 경우 이동하지 않음
        if ny < 0 or nx < 0 or ny >= 8 or nx >= 8:
            continue

        # king이 이동할 자리에 돌이 있다면
        if ny == s_pos.y and nx == s_pos.x:
            s_ny = s_pos.y + commands[command].y
            s_nx = s_pos.x + commands[command].x

            # 돌이 체스판을 벗어 날 경우 king, 돌 모두 이동하지 않음
            if s_ny < 0 or s_nx < 0 or s_ny >= 8 or s_nx >= 8:
                continue

            s_pos.y = s_ny
            s_pos.x = s_nx

        k_pos.y = ny
        k_pos.x = nx

    print(k_pos)
    print(s_pos)


if __name__ == "__main__":
    main()
