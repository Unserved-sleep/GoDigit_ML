seconds: int = int(input())
hours: int = seconds // 3600
seconds %= 3600
minutes: int = seconds // 60
seconds %= 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")