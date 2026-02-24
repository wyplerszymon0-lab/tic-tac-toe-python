class FileManager:
    def __init__(self, filename="stats.txt"):
        self.filename = filename

    def save_stats(self, stats):
        with open(self.filename, "w") as file:
            for key, value in stats.items():
                file.write(f"{key}:{value}\n")

    def load_stats(self):
        stats = {"X": 0, "O": 0}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    key, value = line.strip().split(":")
                    stats[key] = int(value)
        except FileNotFoundError:
            pass

        return stats
