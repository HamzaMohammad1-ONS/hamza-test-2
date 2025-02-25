import requests
from database import create_database, insert_breed, read_breed_by_id, update_breed, delete_breed, search_breed_by_name

def fetch_dog_breeds():
    response = requests.get("https://api.thedogapi.com/v1/breeds")
    if response.status_code == 200:
        breeds = response.json()
        for breed in breeds:
            breed_data = (
                breed['name'],
                breed.get('breed_group', 'N/A'),
                breed.get('life_span', 'N/A'),
                breed.get('temperament', 'N/A'),
                breed.get('origin', 'N/A')
            )
            insert_breed(breed_data)
    else:
        print("Failed to fetch data")

def menu():
    while True:
        print("\n1. View all records")
        print("2. Search records by ID")
        print("3. Search records by name")
        print("4. Update a record")
        print("5. Delete a record")
        print("6. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            # You can implement a function to read and display all records
            pass
        elif choice == '2':
            breed_id = input("Enter breed ID: ")
            breed = read_breed_by_id(breed_id)
            print(breed)
        elif choice == '3':
            name = input("Enter breed name: ")
            breeds = search_breed_by_name(name)
            print(breeds)
        elif choice == '4':
            # Implement update functionality
            pass
        elif choice == '5':
            breed_id = input("Enter breed ID to delete: ")
            delete_breed(breed_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_database()
    fetch_dog_breeds()
    menu()