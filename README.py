# A.-Minutes-Before-the-New-Year
t = int(input())
for _ in range(t):
	h, m = map(int, input().split())
	th = 24 - h
	tm = (th * 60) - m
	print(tm)
