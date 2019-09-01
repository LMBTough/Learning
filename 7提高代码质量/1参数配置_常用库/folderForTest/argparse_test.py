import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo", help="increase output verbosity", type=int)
parser.description="lalalalal"
args = parser.parse_args()

print(args.echo)