import sys

from medusapy.message import read_message, write_answer
from medusapy import medusa


if __name__ == "__main__":
    model = medusa.load(sys.argv[1])

    while True:
        try:
            message = read_message()
        except EOFError:
            sys.exit()
        else:
            if message == []:
                write_answer([])
            else:
                answer = medusa.predict(model, message)
                write_answer(answer)
