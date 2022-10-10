import sys

from medusapy.message import read_message, write_answer
from medusapy import medusa


if __name__ == "__main__":
    models = medusa.load(sys.argv[1], sys.argv[2])

    while True:
        try:
            message = read_message()
        except EOFError:
            sys.exit()
        else:
            if message == []:
                write_answer([])
            else:
                answer = medusa.predict(models, message)
                write_answer(answer)
