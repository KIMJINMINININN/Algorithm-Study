import sys

n = map(int,sys.stdin.readline().split())
inputList = list(map(int,sys.stdin.readline().split()))

print(min(inputList), max(inputList))