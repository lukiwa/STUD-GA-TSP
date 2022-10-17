from loader import load_locations_from_file, calculate_distances_matrix

def main():
    locations = load_locations_from_file("test_data/TSP/berlin11_modified.tsp")    
    distances = calculate_distances_matrix(locations)
    print(distances)


if __name__ == "__main__":
    main()
