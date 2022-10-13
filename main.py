from loader import load_locations_from_file

def main():
    data = load_locations_from_file("test_data/TSP/berlin11_modified.tsp")
    print(data)
if __name__ == "__main__":
    main()
