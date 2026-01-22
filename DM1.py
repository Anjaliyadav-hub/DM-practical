import itertools

class SET:
    def __init__(self, elements):
        self.elements = set(elements)

   
    def is_member(self, x):
        return x in self.elements


    def power_set(self):
        pset = []
        elems = list(self.elements)
        for r in range(len(elems)+1):
            for comb in itertools.combinations(elems, r):
                pset.append(set(comb))
        return pset

   
    def is_subset(self, other):
        return self.elements.issubset(other.elements)

   
    def union(self, other):
        return self.elements.union(other.elements)

    def intersection(self, other):
        return self.elements.intersection(other.elements)

    
    def complement(self, universal_set):
        return universal_set.elements.difference(self.elements)


    def difference(self, other):
        return self.elements.difference(other.elements)

    def symmetric_difference(self, other):
        return self.elements.symmetric_difference(other.elements)

    
    def cartesian_product(self, other):
        return [(a, b) for a in self.elements for b in other.elements]



def main():
    print("Enter elements of Set A (space separated):")
    A = SET(list(map(int, input().split())))

    print("Enter elements of Set B (space separated):")
    B = SET(list(map(int, input().split())))

    print("\nEnter elements of Universal Set (space separated):")
    U = SET(list(map(int, input().split())))

    while True:
        print("\n---- MENU ----")
        print("1. Member Check")
        print("2. Power Set of A")
        print("3. Check Subset (A ⊆ B?)")
        print("4. Union and Intersection")
        print("5. Complement of A")
        print("6. Difference and Symmetric Difference")
        print("7. Cartesian Product (A × B)")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter element to check in Set A: "))
            print("Member:", A.is_member(x))

        elif choice == 2:
            print("Power Set of A:")
            print(A.power_set())

        elif choice == 3:
            print("A is subset of B:", A.is_subset(B))

        elif choice == 4:
            print("Union:", A.union(B))
            print("Intersection:", A.intersection(B))

        elif choice == 5:
            print("Complement of A (U - A):", A.complement(U))

        elif choice == 6:
            print("Difference (A - B):", A.difference(B))
            print("Symmetric Difference:", A.symmetric_difference(B))

        elif choice == 7:
            print("Cartesian Product A × B:")
            print(A.cartesian_product(B))

        elif choice == 8:
            print("Thank you!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
