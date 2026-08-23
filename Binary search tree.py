        else:
            print("Name | Time | Purpose")
            bst.preorder(root)

    elif choice == 6:
        print("\n--- Postorder Traversal ---")
        if root is None:
            print("Log book is empty.")
        else:
            print("Name | Time | Purpose")
            bst.postorder(root)

    elif choice == 7:
        total = bst.count(root)
        print("Total number of entries:", total)

    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
